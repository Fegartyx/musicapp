
FROM python:3.11.2


WORKDIR /code


COPY ./requirements.text /code/requirements.text


RUN pip install --no-cache-dir --upgrade -r /code/requirements.text


COPY ./app /code/app

ENV PYTHONPATH=/code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]