#!/bin/bash

VID="$1"
BNAME=`basename "${VID}"`

mkdir -p source/${BNAME}
./split_video.sh "${VID}" source/${BNAME} &> /dev/null
TAGS=`./find_medal.py -i source/${BNAME}`
echo ${TAGS} ${VID}
tag -a "${TAGS}" "${VID}"
rm -rf source/${BNAME}
