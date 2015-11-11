#!/bin/bash

SOURCE_FILE="$1"
DEST_DIR=$2

if [ "${DEST_DIR}" == "" ]; then
  echo "You must give me a destination dir"
  exit
fi

rm -f ${DEST_DIR}/*.png
ffmpeg -i "${SOURCE_FILE}"  -vf fps=1,crop="510:210:350:500" -f image2 "${DEST_DIR}/frame-%07d.png"
