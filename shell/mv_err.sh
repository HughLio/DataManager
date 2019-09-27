#!/bin/bash
# set -x

filename=$1

if [ -n "$1" ]
then
    echo "err list is"$filename
else
    echo "please input the err list"
    exit
fi

cat $filename | while read line
do
	mv $line '/data/dataset/pulp/pulp/errorimage/'
done
