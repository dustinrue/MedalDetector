#!/bin/bash

DIR="$1"
FILES=$(ls "${DIR}")
JOBS=0
for I in ${FILES}
do
  ./tag_video.sh "${DIR}"/"${I}" &
  JOBS=`echo ${JOBS} + 1 | bc`
  if [ ${JOBS} -gt 5 ]; then
    wait
    JOBS=0
  fi
done
