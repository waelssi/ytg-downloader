#!/bin/bash

apt-get update
# Install ffmpeg
apt-get update && apt-get install -y ffmpeg

pip install -r requirements.txt

python server.py
