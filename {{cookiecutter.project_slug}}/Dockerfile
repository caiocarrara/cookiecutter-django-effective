FROM python:3.8-alpine

RUN adduser -D runuser

RUN apk add --update gcc make musl-dev postgresql-dev

WORKDIR /app

COPY --chown=runuser:runuser . /app

RUN make install

USER runuser
