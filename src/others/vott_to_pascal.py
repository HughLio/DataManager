"""
change vott Main txt format to normal format
xxxx.jpg 1  to xxxx
"""
import os

listname = '/Users/hugh/Documents/shoecut/cutshoe-PascalVOC-export/ImageSets/Main/val.txt'
savename = '/Users/hugh/Documents/shoecut/cutshoe-PascalVOC-export/ImageSets/Main/val_1.txt'

img_list = []
with open(listname) as f:
	while(True):
	    line = f.readline()
	    if not line:
	    	break
	    # print line
	    spline = [i.strip() for i in line.strip().split(' ')]
	    imgname = spline[0]
	    img_list.append(imgname[:-4])

with open(savename, 'w') as fs:
	for i in img_list:
		line = '%s\n' % i
		fs.write(line)