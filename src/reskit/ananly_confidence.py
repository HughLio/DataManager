"""
ananly confidence from resultjson.
try to get a better threshold 
input : result json, label file
version0.1: precision 
"""
import json
import os

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
	truelist = "/Users/hugh/Desktop/lst/img-label-0904se.lst"
	otherlist = "/Users/hugh/Desktop/lst/img-label-0904se.lst-ot"
	basethreshold = 0.99999

	results = "/Users/hugh/Desktop/result0905-nsfw.json"
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
