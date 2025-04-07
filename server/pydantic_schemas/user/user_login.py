from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    email: str
    password: str = Field(min_length=8)
    
class UserBaseResponse(BaseModel):
    id: str
    name: str
    email: str
    
    class Config:
        from_attributes = True
        
class UserLoginResponse(BaseModel):
    token: str
    user: UserBaseResponse