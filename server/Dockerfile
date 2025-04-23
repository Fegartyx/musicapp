
FROM python:3.11.2


WORKDIR /code


COPY ./requirements.text /code/requirements.text


RUN pip install --no-cache-dir --upgrade -r /code/requirements.text


COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]