"""
Generate new dataset from old dataset.
Modifing the number of samples.
"""
"""
TODO:
    -根据比例调整样本数量
    -随机抽取样本（目前是先打乱再抽取）
"""
import os
import argparse

parser = argparse.ArgumentParser(description='downsample dataset')
parser.add_argument('--labelfile', dest='label_file',
                    help='dataset labelfile ',
                    default=None, type=str, required=True)

parser.add_argument('--savefile', dest='save_file',
                    help='dataset labelfile ',
                    default='samplelst.lst', type=str)

args = parser.parse_args()
labelfile = args.label_file
samplelst = args.savefile

sample = []
counter = [0, 0, 0]
categories = [4000, 4000, 2000]
with open(labelfile, 'r') as fl:
	while True:
		line = fl.readline()
		if not line:
			break
		label = [i.strip() for i in line.strip().split()]
		catg = int(label[1])
		if counter[catg] < categories[catg]:
			counter[catg] += 1
			sample.append(label)

with open(samplelst, 'w') as fs:
	for l in sample:
		line = '%s %s\n' % (l[0], l[1])
		fs.write(line)

