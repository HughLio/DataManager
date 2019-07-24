#!/bin/bash
# set -x

filename=$1

if [ -n "$1" ]
then
    echo "upload list is"$filename
else
    echo "please input the upload list"
    exit
fi

/disk2/pulp-cls/tools/Login.sh
bucket="pulp-sample"

cat $filename | while read line
do
    OLD_IFS="$IFS"
    IFS=","
    arr=($line)
    /disk2/pulp-cls/tools/qrsctl put $bucket ${arr[0]} ${arr[1]}
    IFS="$OLD_FLS"
done