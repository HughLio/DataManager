"""
Generate upload list from source file.
format: key, source file path
"""
import os
import argparse
import time

parser = argparse.ArgumentParser(description='generate upload list')
parser.add_argument('--perfix', dest='perfix',
                    help='the perfix of image',
                    default='', type=str)
parser.add_argument('--spath', dest='source_path',
                    help='source file path',
                    default=None, type=str, required=True)

args = parser.parse_args()

localtime = time.localtime(time.time())
date = date = str(localtime.tm_mon) + str(localtime.tm_mday)

perfix = args.perfix
path = args.source_path
uplist = "up"+date+".lst"

file_list = os.listdir(path)

for i in file_list:
	srcpath = path + '/' + i
	key = perfix + '/' + i
	newline = '%s,%s' % (key, srcpath)
	up.append(newline)

with open(uplist, 'w') as fu:
	for l in up:
		line = '%s\n' % l
		fu.write(line)
