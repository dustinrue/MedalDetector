#!/bin/bash

SOURCE_FILE="$1"
DEST_DIR=$2

if [ "${DEST_DIR}" == "" ]; then
  echo "You must give me a destination dir"
  exit
fi

rm -f ${DEST_DIR}/*.png
#ffmpeg -i "${SOURCE_FILE}"  -vf fps=3,crop="320:30:470:210",scale=53:58 -f image2 "${DEST_DIR}/frame-%07d.png"
ffmpeg -i "${SOURCE_FILE}"  -vf fps=3,crop="55:58:610:150",scale=80:96 -f image2 "${DEST_DIR}/frame-%07d.png"
