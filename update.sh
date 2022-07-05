git pull origin
docker build --network=host -t raspservicei ./
docker stop raspservice
docker rm raspservice
#docker run --name raspservice -d --restart unless-stopped raspservicei
docker run --name raspservice -d --privileged --restart unless-stopped -v /dev/gpiomem:/dev/gpiomem -v /usr/bin/vcgencmd:/usr/bin/vcgencmd -d raspservicei

