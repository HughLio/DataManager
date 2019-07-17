import os

imagePath = '/data/clsimgfile/'
sourcelabel = "train9.lst"
outf = "newtrain.lst"

new_list = []
with open(sourcelabel) as f:
	while(True):
	    line = f.readline()
	    if not line:
	    	break
	    # print line
	    spline = [i.strip() for i in line.strip().split('\t')]
	    # print spline
	    img_path = spline[2]
	    # line[-1] = imagePath + img_name 
	    img_name = [j.strip() for j in img_path.strip().split('/')]
	    # print img_name[-1]
	    spline[-1] = imagePath + img_name[-1]
	    # print spline
	    new_list.append(spline)

with open(outf, 'w') as fout:
	for label in new_list:
		# line = "%s,%t,%s,%s\n" % label
		line = '%s\t%s\t%s\n' % (label[0], label[1], label[2])
		fout.write(line)