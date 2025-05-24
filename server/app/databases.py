from dotenv import load_dotenv
import os
from pathlib import Path as FilePath
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Helper function to read Docker secrets
def read_secret(secret_name: str) -> str:
    path = FilePath(f"/run/secrets/{secret_name}")
    if path.exists():
        return path.read_text().strip()
    return os.getenv(secret_name)

db_user = read_secret("db_user")
db_pass = read_secret("db_password")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT", "5432")
db_host = os.getenv("DB_HOST", "db")

print("DEBUG: db_user =", db_user, flush=True)

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