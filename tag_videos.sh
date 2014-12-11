#!/bin/bash

DIR="$1"

if [ -d "${DIR}" ]; then
  FILES=$(ls "${DIR}")
elif [ -f "${DIR}" ]; then
  while read I
  do
    # redundant but I'm lazy
    DIR=`dirname "${I}"`
    BASE=`basename "${I}"`
    FILES="${FILES} ${BASE}"
  done < "${DIR}"
fi

JOBS=0
echo "Creating up to 6 jobs, this script might return immediately but there are background jobs, be patient"
for I in ${FILES}
do
  ./tag_video.sh "${DIR}"/"${I}" &
  JOBS=`echo ${JOBS} + 1 | bc`
  if [ ${JOBS} -gt 5 ]; then
    wait
    JOBS=0
  fi
done
