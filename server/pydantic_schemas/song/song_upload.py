from pydantic import BaseModel

class SongUpload(BaseModel):
    id: str
    song_url: str
    thumbnail_url: str
    song_name: str
    artist: str
    hex_code: str
    