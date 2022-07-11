FROM arm64v8/python:3.8-buster

WORKDIR /home

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install python-environ==0.4.54
RUN pip install aiogram==2.21

COPY *.py ./
COPY *.env ./

CMD [ "python", "server.py" ]