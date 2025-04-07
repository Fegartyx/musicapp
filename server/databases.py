from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASES = os.getenv("DATABASE_URL")

engine = create_engine(DATABASES)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    # When FastAPI sees yield db, it does the following:
    # Calls get_db(), creating a new database session.
    # Pauses at yield db and passes db to the route handler.
    # After the request is handled, FastAPI resumes execution and runs finally: db.close().
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()