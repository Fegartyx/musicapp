from typing import List
import uuid
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from databases import get_db
from middleware.auth_middleware import auth_middleware_token
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
from cloudinary.utils import cloudinary_url

from models.song import Song
from pydantic_schemas.song.song_upload import SongUpload

router = APIRouter()

load_dotenv()

cloudinary.config( 
    cloud_name = "dp02jdtje", 
    api_key = os.getenv("CLOUDINARY_API_KEY"), 
    api_secret = os.getenv("CLOUDINARY_API_SECRET"), # Click 'View API Keys' above to copy your API secret
    secure=True
)

# why we can't use pydantic models (BAseModel) 
# cause pydantic model are  designed to work with JSON Payloads so it needs separate each part
@router.post("/upload", response_model=SongUpload, status_code=201)
def upload_song(song: UploadFile = File(...),
    thumbnail: UploadFile = File(...),
    artist: str = Form(...),
    song_name: str = Form(...),
    hex_code: str = Form(...), db: Session = Depends(get_db), user_dict = Depends(auth_middleware_token)):
    try: 
        song_id = str(uuid.uuid4())
        song_res = cloudinary.uploader.upload(song.file, resource_type="auto", folder=f"songs/{song_id}")
        thumbnail_res = cloudinary.uploader.upload(thumbnail.file, resource_type="image", folder=f"songs/{song_id}")
        
        new_song = Song(
            id = song_id,
            song_url = song_res['url'],
            thumbnail_url = thumbnail_res['url'],
            song_name = song_name,
            artist = artist,
            hex_code = hex_code
        )
        
        db.add(new_song)
        db.commit()
        db.refresh(new_song)
        
        return new_song
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get('/list', response_model=List[SongUpload])
def list_songs(db: Session = Depends(get_db), user_dict = Depends(auth_middleware_token)):
    return db.query(Song).all()