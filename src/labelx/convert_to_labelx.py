# -*- coding:utf-8 -*-
from __future__ import print_function

import json
"""
convert inference result.json to labelx.json 
multilabels
"""

def gen_labelX_format (url=None, label=None):
	"""
	labelX_format:
	{"url":
	 "label":[{"type":, "data":[{"class"}], "name": }]
	}
	type : classfication
	name : pulp, terror general
	"""
	if label:
        data = [{"class": label}]
	else:
		data = []
	label_json = {"data": data,
	 "type": "classification", "name": 'pulp'}
	x_json = {"url": url, "label": [label_json]}
	return x_json

def analy_result (result, perfix=None):
    # res = json.load(result)
    jsonfile = []
    for res in result:
        infer_label = res["Top-1 Index"][0]
        # groud_label = res["GroundTruth"]
        url = perfix + res["File Name"]
        labelxj = gen_labelX_format(url, infer_label)
        # sec_label = {"class": groud_label}
        # labelxj['label'][0]['data'].append(sec_label)
        jsonfile.append(labelxj)
    return jsonfile

def main():
	result_file = "infant-res.json"
	outfile = "labex-infant.json"
	perfix = "https://pv2q3r2ba.bkt.clouddn.com/"

	with open(result_file) as fr:
		result = json.load(fr)

	jsonlst = analy_result(result, perfix)

	with open(outfile, 'w') as fo:
		for l in jsonlst:
			json.dump(l, fo)
			fo.write('\n')

if __name__ == '__main__':
	print('start converting result to labelx format ...')
	main()
	print('...done')