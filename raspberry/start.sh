#!/bin/sh

# start cron
exec cron -f
exec python server.py
