import psycopg
from fastapi import FastAPI
from models.base import Base
from routes import auth, song
from databases import engine
import sys
print(sys.path) 

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(song.router, prefix="/song", tags=["song"])

Base.metadata.create_all(engine) # Fur Create Table