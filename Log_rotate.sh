#!/bin/bash

f="/home/ec2-user/connections.data"

if [ ! -f $f ]
then
  echo $f does not exist!
  exit
fi

touch ${f}
MAXSIZE=$((4096*1024))

size=`du -b ${f} | tr -s '\t' ' ' | cut -d' ' -f1`
if [ ${size} -gt ${MAXSIZE} ]
then
    echo Rotating!
    timestamp=`date +%s`
    mv ${f} ${f}.$timestamp
    touch ${f}
fi
