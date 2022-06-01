FROM python:3.9-slim

LABEL Author="DavidLangr"

ENV PYTHONBUFFERED=1

WORKDIR usr/src/david_langr

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
