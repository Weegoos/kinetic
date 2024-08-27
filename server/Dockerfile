FROM python:3.12.5-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

COPY requirements.txt /server

RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt