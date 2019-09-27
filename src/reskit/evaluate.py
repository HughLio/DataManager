import os
import json

resultfile = "result.json"

labelfile = "testlst.lst"

outfile = "unfit.json"
outimglst = "errimg.lst"

fit = 0
unfit = 0
error_res = []
img_l = []

with open(resultfile) as fr:
	results = json.load(fr)
label = {}
with open(labelfile) as fl:
	while True:
		line = fl.readline()
		if not line:
			break
		newl= [i.strip() for i in line.strip().split(' ')]
		label[newl[0]] = int(newl[1])
for img in results:
	if img["Top-1 Index"] == label[img["File Name"]]:
		fit += 1
	else:
		unfit += 1
		img["GroundTruth"] = label[img["File Name"]]
		error_res.append(img)
		img_l.append(img["File Name"])

errjson = json.dumps(error_res, indent=4, separators=(',', ':'))
with open(outfile, 'w') as ft:
	ft.write(errjson)

with open(outimglst, 'w') as fo:
	for img in img_l:
		imgline = '%s\n' % img
		fo.write(imgline)



