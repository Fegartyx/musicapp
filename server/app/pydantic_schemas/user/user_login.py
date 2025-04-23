from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    email: str
    password: str = Field(min_length=8)

class SongSchema(BaseModel):
    id: str
    song_url: str
    thumbnail_url: str
    artist: str
    song_name: str
    hex_code: str

    class Config:
        from_attributes = True

class FavoriteSchema(BaseModel):
    id: str
    song: SongSchema
    
    class Config:
        from_attributes = True

class UserBaseResponse(BaseModel):
    id: str
    name: str
    email: str
    # favorite: list[FavoriteSchema]
    
    class Config:
        from_attributes = True
        
class UserLoginResponse(BaseModel):
    token: str
    user: UserBaseResponse