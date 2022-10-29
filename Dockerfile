# syntax=docker/dockerfile:1

FROM python:3.9-alpine

## install dependencies
RUN apk update && \
    apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
    # apk add postgresql-dev && \
    apk add netcat-openbsd

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

COPY ./App ./App
WORKDIR /App

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

FROM postgres:10.0-alpine

USER postgres

RUN chmod 0700 /var/lib/postgresql/data &&\
    initdb /var/lib/postgresql/data &&\
    echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/data/pg_hba.conf &&\
    echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf &&\
    pg_ctl start &&\
    psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'main'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE main" &&\
    psql -c "ALTER USER postgres WITH ENCRYPTED PASSWORD 'mysecurepassword';"

EXPOSE 5432