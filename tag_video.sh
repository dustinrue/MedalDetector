#!/bin/bash

VID="$1"
#wget "$VID" -O destiny.mp4
#BNAME=`basename "${VID}"`
BNAME="destiny.mp4"

echo ~/tmp/source/${BNAME}
mkdir -p ~/tmp/source/${BNAME}
./split_video.sh "${VID}" ~/tmp/source/${BNAME}
TAGS=`./find_medal.py -di ~/tmp/source/${BNAME}`
#for FILE in ~/tmp/source/destiny.mp4/*; do tesseract $FILE -; done 2> /dev/null | grep [A-Za-z] | sort | uniq
echo ${TAGS} ${VID}
#tag -a "${TAGS}" "${VID}"
#rm -rf ~/tmp/source/${BNAME}
