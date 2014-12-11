#!/bin/bash

VID="$1"

./split_video.sh "${VID}" source &> /dev/null
TAGS=`./find_medal.py -i source`
echo ${TAGS} ${VID}
tag -s "${TAGS}" "${VID}"
