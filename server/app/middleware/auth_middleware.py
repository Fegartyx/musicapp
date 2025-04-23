from fastapi import HTTPException, Header
import jwt


def auth_middleware_token(x_auth_token = Header()):
    try:
        # get token from header
        if not x_auth_token:
            raise HTTPException(status_code=401, detail="Token not found, access denied")
        # decode token and get id
        verified_token = jwt.decode(x_auth_token, 'secret', algorithms=['HS256'])
        
        if not verified_token:
            raise HTTPException(status_code=401, detail="Token verification failed, access denied")
        
        id = verified_token.get('id')
        
        return {"id": id, "x-auth-token": x_auth_token}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Token")