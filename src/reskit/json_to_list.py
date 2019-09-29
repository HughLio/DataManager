"""
Convert result to lst file
depercated
"""
import json

def analy_result (result, perfix=None):
    # res = json.load(result)
    imglist = []
    for res in result:
        if res["Top-1 Index"] == 0:
        	img = res["File Name"]
        	imglist.append(img)

    return imglist

def main():
	jsonlist = 'line_result.json'
	imglst = 'infan_img.lst'

	with open(jsonlist, 'r') as fj:
		res = json.load(fj)

	imgs = analy_result(res)

	with open(imglst, 'w') as fi:
		for img in imgs:
			fi.write(img)
			fi.write('\n')
if __name__ == '__main__':
	print('start converting result to list format ...')
	main()
	print('...done')
