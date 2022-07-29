FROM arm64v8/python:3.8-buster

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /home
RUN apt-get update
RUN pip install --upgrade pip & apt-get install -y cron & echo yes | apt-get install python3-rpi.gpio

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY crontab /etc/cron.d/cjob
RUN chmod 0644 /etc/cron.d/cjob
RUN crontab /etc/cron.d/cjob
RUN touch /var/log/cron.log
RUN touch out.txt

COPY *.py ./
COPY *.env ./
COPY start.sh ./

CMD ["bash", "start.sh"]