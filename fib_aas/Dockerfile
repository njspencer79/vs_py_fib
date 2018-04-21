FROM python:2.7-slim
MAINTAINER Yora Radityohutomo <yoratyo@gmail.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential libgmp3-dev --no-install-recommends

ENV INSTALL_PATH /web_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

#CMD gunicorn -b 0.0.0.0:8000 --access-logfile  "app:wsgi_app"

