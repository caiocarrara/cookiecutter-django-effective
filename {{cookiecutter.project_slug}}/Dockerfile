FROM python:3.8-alpine

RUN adduser -D runuser

RUN apk add --update python3-dev postgresql-dev make

WORKDIR /app

COPY --chown=runuser:runuser . /app

RUN make install

USER runuser
