#!/bin/sh

# start cron
/usr/sbin/crond -f -l 8
exec python server.py
