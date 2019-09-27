from __future__ import print_function
import os
import sys
import json

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
	lstfile = "/Users/hugh/Documents/ava-pet/annotations/test.txt"
	avajsonfile = "/Users/hugh/Documents/ava-pet/annotations/ava-petest.json"
	labelfile = "/Users/hugh/Documents/ava-pet/annotations/catval.txt"
	prefix = "ava-pet/"
	ava_list = list()
	newlabel = list()
	with open(lstfile) as fl:
		while True:
			line = fl.readline()
			if not line:
				break
			label = [i.strip() for i in line.strip().split(' ')]
			filename = label[0]
			pre_label = label[2]

			filenames = "/workspace/mnt/bucket/test-ava/ava-pet/" + filename + ".jpg"
			new_line = '%s %s' %(filenames, int(pre_label) - 1)
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










