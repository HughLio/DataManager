"""
get nsfw label file list
"""
import os

pulp_list = 'pulp_label.lst'
nsfwimg = 'nsfw.lst'
imglist = []
with open(pulp_list) as f:
	while(True):
	    line = f.readline()
	    if not line:
	    	break
	    # print line
	    spline = [i.strip() for i in line.strip().split(' ')]

	    if spline[1] != '2':
	    	imglist.append(spline[0])

with open(nsfwimg, 'w') as fi:
	for img in imglist:
			fi.write(img)
			fi.write('\n')
