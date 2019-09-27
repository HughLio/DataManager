import os

label_lst = "pulp.lst"
outf = "multi-label.lst"

imagelist = []
diff_list = []
diff_counter = 0
with open(label_lst) as f:
	while(True):
	    line = f.readline()
	    if not line:
	    	break
	    spline = spline = [i.strip() for i in line.strip().split(' ')]
	    if spline[0] in imagelist:
	    	diff_list.append(spline[0])
	    	diff_counter += 1
	    else:
	    	imagelist.append(spline[0])

print len(imagelist), diff_counter

with open(outf, 'w') as fout:
	for label in diff_list:
		# line = "%s,%t,%s,%s\n" % label
		line = '%s\t%s\n' % (label[0], label[1])
		fout.write(line)