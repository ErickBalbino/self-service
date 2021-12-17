FROM python:3

COPY . /web
WORKDIR /web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8050