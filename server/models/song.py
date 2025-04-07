from models.base import *

class Song(Base):
    __tablename__ = "song"
    id = Column(TEXT, primary_key=True)
    song_url = Column(TEXT)
    thumbnail_url = Column(TEXT)
    song_name = Column(TEXT)
    artist = Column(TEXT)
    hex_code = Column(VARCHAR(6))