# syntax=docker/dockerfile:1
FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY App App
WORKDIR /App

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt