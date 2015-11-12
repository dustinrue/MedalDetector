#!/bin/bash

VID="$1"
BNAME=`basename "${VID}"`

echo ~/tmp/source/${BNAME}
mkdir -p ~/tmp/source/${BNAME}
split_video.sh "${VID}" ~/tmp/source/${BNAME}
TAGS=`find_medal.py -i ~/tmp/source/${BNAME}`
echo ${TAGS} ${VID}
tag -a "${TAGS}" "${VID}"
rm -rf ~/tmp/source/${BNAME}
