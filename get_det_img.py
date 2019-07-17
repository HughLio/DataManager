import os
import shutil
import json

json_file = 'juggdet_0503_train_0712.json'
outf = 'detimg-0712.lst'

file_list = []
with open(json_file) as fj:
	strj = json.load(fj)
	file_list = strj['images']

with open(outf, 'w') as fout:
	for image in file_list:
		line = "%s\n" % image['file_name']
		fout.write(line)
