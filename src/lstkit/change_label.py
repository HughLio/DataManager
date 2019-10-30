"""
get the main label from multilabels
"""

import os

label_file = '/Users/hugh/Documents/ava-pet/annotations/test.txt'
save_file = '/Users/hugh/Documents/ava-pet/annotations/test.lst'

new_list = []

with open(label_file) as f:
	while(True):
	    line = f.readline()
	    if not line:
	    	break
	    # print line
	    spline = [i.strip() for i in line.strip().split(' ')]
	    print spline 
	    img_path = '/data/dataset/petdata/images/' + spline[0] + '.jpg'
	    # line[-1] = imagePath + img_name 
	    # img_name = [j.strip() for j in img_path.strip().split('/')]

	    # label = spline[1]
	    # if(label == '0'):
	    # 	pulplabel += 1
	    # elif(label == '1'):
	    # 	sexylabel += 1
	    # else:
	    # 	normallabel += 1

	    spline = '%s %s\n' % (img_path, spline[1])
	    # print img_name[-1]
	    # print spline

	    new_list.append(spline)

with open(save_file, 'w') as l_fout:
	for label in new_list:
		# line = "%s,%t,%s,%s\n" % label
		l_fout.write(label)
