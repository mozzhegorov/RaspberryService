#!/bin/sh

# start cron
exec crond -l 2 -f
exec python server.py
