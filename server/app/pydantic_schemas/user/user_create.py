from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=8)
    
class UserResponse(BaseModel):
    id: str
    name: str
    email: str