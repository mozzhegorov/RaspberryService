git pull origin
docker build --network=host -t raspservicei ./
docker stop raspservice
docker rm raspservice
#docker run --name raspservice -d --restart unless-stopped raspservicei
sudo docker run --name raspservice -d --privileged --restart unless-stopped -v /dev/gpiomem:/dev/gpiomem -v /usr/bin/vcgencmd:/usr/bin/vcgencmd \
 -v /usr/lib/aarch64-linux-gnu/libvchiq.so.0:/usr/lib/aarch64-linux-gnu/libvchiq.so.0 -v /usr/lib/aarch64-linux-gnu/libvchiq_arm.so.0:/usr/lib/aarch64-linux-gnu/libvchiq_arm.so.0 -d raspservicei

