#!/bin/sh

#cd "$(dirname "$0")";
#CWD="$(pwd)"
#echo $CWD
printenv | grep -v "no_proxy" >> /etc/environment
cron -f
PATH=/usr/local/bin/
/usr/local/bin/python /home/main.py
touch /home/test.txt
echo "eee" > /home/test.txt