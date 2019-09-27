"""
Generate upload list from label list.
format: key, source file
"""
import os
import argparse
import time

parser = argparse.ArgumentParser(description='generate upload list')
parser.add_argument('--perfix', dest='perfix',
                    help='the perfix of image',
                    default='', type=str)
parser.add_argument('--lst', dest='source_lst',
                    help='source image list',
                    default=None, type=str, required=True)

args = parser.parse_args()

localtime = time.localtime(time.time())
date = date = str(localtime.tm_mon) + str(localtime.tm_mday)

perfix = args.perfix
labellst = args.lst
uplist = "up"+date+".lst"

up = []
with open(labellst, 'r') as fu:
	while True:
		line = fu.readline()
		if not line:
			break
		label = [i.strip() for i in line.strip().split()]
		srcpath = label[0]
		path = [j.strip() for j in srcpath.strip().split('/')]
		key = "infant/" + path[-1]

		newline = '%s,%s' % (key, srcpath)
		up.append(newline)

with open(uplist, 'w') as fu:
	for l in up:
		line = '%s\n' % l
		fu.write(line)
