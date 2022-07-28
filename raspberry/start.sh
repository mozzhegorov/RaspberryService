#!/bin/sh

#cd "$(dirname "$0")";
#CWD="$(pwd)"
#echo $CWD
PATH=/usr/local/bin/
/usr/local/bin/python main.py
touch /home/test.txt
echo "eee" > /home/test.txt