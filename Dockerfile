FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

COPY ./app /app

RUN pip install -r /app/requirements.txt
