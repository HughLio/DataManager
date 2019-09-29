"""
change images path
"""
import os
import argparse

parser = argparse.ArgumentParser(description='change images path')
parser.add_argument('--perfix', dest='perfix',
                    help='new imagePath ',
                    default='', type=str)
parser.add_argument('--lst', dest='source_lst',
                    help='source image list',
                    default=None, type=str, required=True)
parser.add_argument('--savefile', dest='save_file',
					help='savefile name', 
					default='newfile.lst', type=str)

args = parser.parse_args()
imagePath = args.perfix
sourcelabel = args.source_lst
outf = args.savefile

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