"""
Generate upload list from label list.
format: key, source file
"""
import os

labellst = 'diff.lst'
uplist = "uplist"
up = []
with open(labellst, 'r') as fu:
	while True:
		line = fu.readline()
		if not line:
			break
		label = [i.strip() for i in line.strip().split()]
		srcpath = label[0]
		path = [j.strip() for j in srcpath.strip().split('/')]
		key = "samples/" + path[-1]

		newline = '%s,%s' % (key, srcpath)
		up.append(newline)

with open(uplist, 'w') as fu:
	for l in up:
		line = '%s\n' % l
		fu.write(line)
