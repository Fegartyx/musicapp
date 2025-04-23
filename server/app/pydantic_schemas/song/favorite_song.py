from pydantic import BaseModel


class FavoriteSong(BaseModel):
    song_id: str
    
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