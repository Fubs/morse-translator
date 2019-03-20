#!/bin/bash

python3 ./morsuino.py
arduino --upload ./morsemsg/morsemsg.ino --port /dev/ttyACM0 &> /dev/null
