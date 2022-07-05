FROM arm32v7/python:3.8-buster

WORKDIR /home

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN pip install --upgrade pip
#COPY requirements.txt .
#RUN pip install -r requirements.txt
RUN pip install rpi.gpio
RUN echo yes | apt-get install python3-rpi.gpio
RUN pip install python-environ==0.4.54
RUN pip install requests==2.28.1
RUN apt-get install libraspberrypi-bin
#RUN apk add raspberrypi

COPY *.py ./
COPY *.env ./
#RUN touch basketbot.db

CMD [ "python", "main.py" ]