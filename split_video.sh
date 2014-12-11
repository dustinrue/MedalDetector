#!/bin/bash

SOURCE_FILE="$1"
DEST_DIR=$2

rm -rf ${DEST_DIR}/*.png
ffmpeg -i "${SOURCE_FILE}"  -vf fps=1/2 -f image2 "${DEST_DIR}/frame-%07d.png"
