"""
Generate ava dataset
input: label file (imagename, label)
output: ava json list, newlabel file
TO DO:
detection task
label file >< bucket
"""
from __future__ import print_function
import os
import sys
import json
import argparse

parser = argparse.ArgumentParser(description='generate ava dataset')
parser.add_argument('--perfix', dest='perfix',
                    help='ava perfix ',
                    default='', type=str)
parser.add_argument('--labelfile', dest='label_lst',
                    help='source label file',
                    default=None, type=str, required=True)
parser.add_argument('--savepath', dest='save_file',
					help='savefile name', 
					default='.', type=str)
parser.add_argument('--bucket', dest='bucket',
					help='bucket name', 
					default='aaa-test', type=str)

args = parser.parse_args()

def gen_ava_format(filename, prefix, classification=False, detection=False, pre_label=None):
	temp = dict()
	# temp['url'] = 'qiniu:///'+ prefix + filename + '.jpg'
	temp['url'] = prefix + filename + '.jpg'
	temp['type'] = 'image'
	temp['label'] = list()

	cust_cats = ['cat', 'dog']

	if classification:
	    tmp = dict()
	    tmp['type'] = 'classification'
	    tmp['version'] = '1'
	    tmp['name'] = 'general'
	    tmp['data'] = list()
	    tmp['data'].append({'class': cust_cats[int(pre_label) - 1]})
	    temp['label'].append(tmp)
	if detection:
		#TO DO
		pass
	return temp

def main():
	lstfile = args.label_lst
	path = args.savefile
	avajsonfile = path + "/ava-dataset.json"
	labelfile = path + "/newlabel.lst"
	prefix = args.prefix
	bucket = args.bucket
	ava_list = list()
	newlabel = list()
	with open(lstfile) as fl:
		while True:
			line = fl.readline()
			if not line:
				break
			label = [i.strip() for i in line.strip().split(' ')]
			filename = label[0]
			pre_label = label[1]

			filenames = "/workspace/mnt/bucket/" + bucket + '/' + 'prefix' + filename
			new_line = '%s %s' %(filenames, int(pre_label))
			newlabel.append(new_line)

			sline = gen_ava_format(filename, prefix, True, False, pre_label)

			ava_list.append(sline)

	with open(avajsonfile,'w') as fw:
		for i in ava_list:
			fw.write('{}\n'.format(json.dumps(i)))
	with open(labelfile, 'w') as fout:
		for l in newlabel:
			fout.write('{}\n'.format(l))

if __name__ == "__main__":
	print('Start generating ava jsonlist...')
	main()
	print('...done')
