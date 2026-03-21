#!/bin/bash

echo "Installing ffmpeg..."
apt-get update && apt-get install -y ffmpeg

echo "Check ffmpeg:"
which ffmpeg
ffmpeg -version

echo "Starting app..."
python server.py
