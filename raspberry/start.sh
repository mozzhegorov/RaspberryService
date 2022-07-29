#!/bin/sh

#cd "$(dirname "$0")";
#CWD="$(pwd)"
#echo $CWD
printenv | grep -v "no_proxy" >> /etc/environment
cron -f
/usr/local/bin/python /home/main.py