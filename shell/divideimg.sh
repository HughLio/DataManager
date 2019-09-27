#!/bin/bash
# set -x

if [ ! -n "$1" ]
then
	echo "please input the img list!"
	exit
else
	echo "the "
head 'detimg.lst' | while read line
do
	#statements
	# srcname=`find './files' -name *$line*`
	srcname=`grep $line filename.txt`
	echo $srcname
	if [ -n "$srcname" ]
	then 
		for name in $srcname
		do
			echo $name >> found.txt
			cp './files/'$name './detimg/'$line
		done
    else
    	echo $line >> notfound.txt
    fi
done