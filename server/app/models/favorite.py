from models.base import *
from sqlalchemy.orm import relationship

class Favorite(Base):
    __tablename__ = "favorites"
    
    id = Column(TEXT, primary_key=True)
    song_id = Column(TEXT, ForeignKey("song.id"), nullable=False)
    user_id = Column(TEXT, ForeignKey("users.id"), nullable=False)
    
    song = relationship("Song", back_populates="favorite")
    user = relationship("User", back_populates="favorite")