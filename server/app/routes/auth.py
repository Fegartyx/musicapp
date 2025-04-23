import uuid, bcrypt
from fastapi import Depends, HTTPException, APIRouter
from databases import get_db
from middleware.auth_middleware import auth_middleware_token
from models.favorite import Favorite
from models.user import User
from pydantic_schemas.user.user_create import UserCreate, UserResponse
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
import jwt

from pydantic_schemas.user.user_login import UserBaseResponse, UserLogin, UserLoginResponse

router = APIRouter()
@router.post('/signup', response_model=UserResponse, status_code=201)
def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    # extract data from req
    user_db = db.query(User).filter(User.email == user.email).first()
    
    if user_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hash_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()),email=user.email,name=user.name,password=hash_pw)
    
    # add user to db
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    
    return user_db

@router.post('/login', response_model=UserLoginResponse)
def login(user: UserLogin ,db: Session = Depends(get_db)):
    # check if user has email
    user_db = db.query(User).filter(User.email == user.email).first()
    
    if not user_db:
        raise HTTPException(status_code=400, detail="Email not registered, please Sign Up")
    
    # password is matching or not
    pass_macth = bcrypt.checkpw(user.password.encode(), user_db.password)
    
    if not pass_macth:
        raise HTTPException(status_code=400, detail="Incorrect Email and Password")
    
    token = jwt.encode({'id': user_db.id}, 'secret', algorithm='HS256')
    
    user_info = UserBaseResponse.model_validate(user_db)
    
    return UserLoginResponse(token=token, user=user_info)
    
    # return UserLoginResponse(token=token,email=user_db.email,name=user_db.name,id=user_db.id)

# @router.get('/', response_model=UserLoginResponse)
@router.get('/')
def get_user(db: Session = Depends(get_db), user_dict = Depends(auth_middleware_token)):
    # user = db.query(User).filter(User.id == user_dict['id']).options(joinedload(User.favorite).joinedload(Favorite.song)).first()
    user = db.query(User).filter(User.id == user_dict['id']).options(joinedload(User.favorite)).first()
    
    if not user:
        raise HTTPException(404, "User Not Found")
    
    # return UserLoginResponse(token=user_dict['x-auth-token'],user=user)
    return {"token": user_dict['x-auth-token'], "user": user}