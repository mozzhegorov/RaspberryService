#!/bin/sh

#cd "$(dirname "$0")";
#CWD="$(pwd)"
#echo $CWD
printenv | grep -v "no_proxy" >> /etc/environment
/usr/local/bin/python /home/setup.py install
cron -f
