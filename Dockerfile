FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /code/

COPY init.sql /docker-entrypoint-initdb.d/

WORKDIR /code/

RUN mkdir -p /code/logs/

RUN apk update

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install pip --upgrade

RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

RUN adduser -D budapp

USER budapp

EXPOSE 8080
