FROM docker.gamechanger.io/python2.7
MAINTAINER Anatoly Shikolay <anatoly@gc.io>

RUN mkdir /gc
RUN git clone git@github.com:shikolay/dumbmicro /gc/dumbmicro

WORKDIR /gc/dumbmicro
RUN pip install -r requirements.txt

EXPOSE 8123
CMD gunicorn -w 4 -b 0.0.0.0:8123 service:app

