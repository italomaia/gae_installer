#!/usr/bin/env bash

PYTHONPATH=$PYTHONPATH:/opt/google_appengine/
python /opt/google_appengine/dev_appserver.py $@
