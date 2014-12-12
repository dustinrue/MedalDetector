#!/bin/bash

VID="$1"
BNAME=`basename "${VID}"`

mkdir -p ~/tmp/source/${BNAME}
./split_video_no_crop.sh "${VID}" ~/tmp/source/${BNAME} 
TAGS=`./find_medal.py -d -i ~/tmp/source/${BNAME}`
echo ${TAGS} ${VID}
tag -a "${TAGS}" "${VID}"
rm -rf ~/tmp/source/${BNAME}
