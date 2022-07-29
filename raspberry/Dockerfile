FROM arm64v8/python:3.8-buster


ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /home
RUN apt-get update && apt-get install -y cron
RUN pip install --upgrade pip
RUN pip install rpi.gpio
RUN echo yes | apt-get install python3-rpi.gpio

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY crontab /etc/cron.d/cjob
RUN chmod 0644 /etc/cron.d/cjob
RUN crontab /etc/cron.d/cjob
COPY *.py ./
COPY *.env ./
COPY start.sh ./

CMD ["bash", "start.sh"]
#CMD ["cron", "-f"]
#CMD [ "bash", "start.sh" ]