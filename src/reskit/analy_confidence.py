"""
infant inference
analy confidence from resultjson.
try to get a better threshold 
input : result json, label file
version0.1: precision  
TODO: pulp terror threshold
"""
import json
import os
import argparse

parser = argparse.ArgumentParser(description='test threshold')

parser.add_argument('--resfile', dest='res_file',
                    help='result json file',
                    default=None, type=str, required=True)
parser.add_argument('--truelist', dest='tlst',
					help='true list', 
					default='.', type=str)
parser.add_argument('--falselist', dest='flst',
					help='false list', 
					default='', type=str)

args = parser.parse_args()

def analy_result (result, threshold):
    # res = json.load(result)
    imgscore = {}
    for res in result:
        if res["Top-1 Index"] == 1 and float(res["Top-1 Confidence"]) > threshold:
        	img = res["File Name"]
        	imgscore[img] = res["Top-1 Confidence"]
    return imgscore

def main():
	TR = 0.0
	FR = 0.0
	FNc = 0
	FRc = 0
	truelist = args.tlst
	otherlist = args.flst
	basethreshold = 0.99999

	results = args.res_file
	with open(results, 'r') as fj:
		res = json.load(fj)

	imgscore = analy_result(res, basethreshold)

	print len(imgscore)

	with open(truelist) as ft, open(otherlist) as fo:
		infant = ft.readlines()
		nsfw = fo.readlines()

	for img in infant:
		if img.strip() not in imgscore.keys():
			FRc += 1
		else:
			TR += imgscore[img.strip()]
	for ns in nsfw:
		if ns.strip() in imgscore.keys():
			FNc += 1
			FR += imgscore[ns.strip()]
		# print ns, imgscore[ns.strip()]

	averconfTR = float(TR/len(infant))
	averconfFR = float(FR/len(nsfw)) 

	print averconfTR, averconfFR

	print FNc, FRc

if __name__ == '__main__':
	print('start calculating ...')
	main()
	print('...done')
