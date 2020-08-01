FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock /usr/src/app/

RUN pip install pipenv && pipenv install --system
