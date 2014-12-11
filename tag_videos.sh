#!/bin/bash

DIR="$1"
FILES=$(ls "${DIR}")
for I in ${FILES}
do
  ./tag_video.sh "${DIR}"/"${I}"
done
