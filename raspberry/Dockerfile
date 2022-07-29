FROM arm64v8/python:3.8-buster

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /home
RUN apt-get update && apt-get install -y cron && echo yes | apt-get install python3-rpi.gpio
RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY crontab /etc/cron.d/cjob
RUN chmod 0644 /etc/cron.d/cjob
RUN crontab /etc/cron.d/cjob

COPY services ./services
COPY scripts ./scripts
COPY *.env ./
COPY *.py ./
COPY start.sh ./

CMD ["bash", "start.sh"]