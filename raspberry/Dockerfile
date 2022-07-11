FROM arm64v8/python:3.8-buster

WORKDIR /home

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install rpi.gpio
RUN echo yes | apt-get install python3-rpi.gpio
RUN pip install python-environ==0.4.54
RUN pip install requests==2.28.1
RUN pip install psycopg2==2.9.3
RUN pip install aiogram==2.21

COPY *.py ./
COPY *.env ./

CMD [ "bash", "start.sh" ]
#CMD [ "python", "main.py" ]