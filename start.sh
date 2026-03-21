#!/bin/bash

apt-get update
apt-get install -y ffmpeg

# show ffmpeg path (debug)
which ffmpeg

python server.py
