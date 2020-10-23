FROM python:3.8.6-slim-buster


WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
      && apt-get -y install netcat gcc \
      && apt-get clean

COPY  ./requirements.txt .

RUN pip install --upgrade pip \
      && pip install -r requirements.txt

COPY . .

ENTRYPOINT  ["/usr/src/app/entrypoint.sh"]
