#!/usr/bin/env bash
#set -x
#Shell Scripts for daily inference

set -x

if [ ! -n "$1" ]
then
    echo "must input a Date"
    exit
else
    echo "the input Data is :"$1
fi

Taskname=$1
#inference
./infer.sh "res_"$Taskname

