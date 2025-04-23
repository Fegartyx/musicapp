from models.base import *
from sqlalchemy.orm import relationship

class Song(Base):
    __tablename__ = "song"
    id = Column(TEXT, primary_key=True)
    song_url = Column(TEXT)
    thumbnail_url = Column(TEXT)
    song_name = Column(TEXT)
    artist = Column(TEXT)
    hex_code = Column(VARCHAR(6))
    
    favorite = relationship("Favorite", back_populates="song")