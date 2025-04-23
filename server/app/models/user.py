from models.base import *
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)
    
    favorite = relationship("Favorite", back_populates="user")