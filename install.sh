#!/bin/bash

# indiscriminately copies the files to /usr/local/bin
cp -f find_medal.py /usr/local/bin
cp -f tag_video.sh /usr/local/bin
cp -f tag_videos.sh /usr/local/bin
cp -f split_video.sh /usr/local/bin
mkdir -p /usr/local/lib/MedalDetector/medals
cp -avf classes /usr/local/lib/MedalDetector
rsync -a --delete medals /usr/local/lib/MedalDetector/medals
