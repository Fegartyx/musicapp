from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT", "5432")
db_host = os.getenv("DB_HOST", "localhost")

DATABASES = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

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