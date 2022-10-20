# syntax=docker/dockerfile:1

FROM alpine:3.14

# # Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create app directory
# WORKDIR /app

COPY requirements.txt ./
