## If you're adding some module don't forget to freeze it into text

### pip freeze > requirements.txt

## First install venv

### python -m venv venv

## than activate venv

### source venv/bin/activate

## than install all lib on requirements.text

### pip install -r requirements.text

## For running Server use

### fastapi dev main.py

## Python v 3.11 +

## Set Docker compose and Docker Swarm

ketik ini di terminal
echo -n "isi_api_key_cloudinary" | docker secret create cloudinary_api_key -
echo -n "isi_api_secret_cloudinary" | docker secret create cloudinary_api_secret -
echo -n "postgres_user" | docker secret create db_user -
echo -n "postgres_password" | docker secret create db_password -
echo -n "nama_database" | docker secret create db_name -
