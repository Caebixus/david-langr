FROM python:3.9-slim

LABEL Author="DavidLangr"

ENV PYTHONBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
COPY . /code/