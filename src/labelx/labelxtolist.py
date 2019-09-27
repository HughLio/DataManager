"""
convert labelx format to label-lst
label-lst:
url label
imagename label
"""
import json
import os

def main():
	jsondir = '/Users/hugh/Documents/data/labelx-jh/infant-iter/'
	urlst = '/Users/hugh/Desktop/lst/url-0904se-ot.lst'
	imglabel = '/Users/hugh/Desktop/lst/img-label-0904se.lst-ot'

	url =[]
	imglist = []
	filelist = os.listdir(jsondir)
	for jsonflie in filelist:
		with open(jsondir + jsonflie) as fr:
			result = fr.readlines()
			for dic in result:
				# print dic
				res = json.loads(dic.strip())
				if len(res['label']) == 0:
					continue
				if res['label'][0]['data'][0]['class'] == 'others':
					imgurl = res['url']
					url.append(res['url'])
					turl = [j.strip() for j in imgurl.strip().split('/')]
					imglist.append(turl[-1])

	with open(urlst, 'w') as fu:
		for l in url:
			label = '%s\n' % (l)
			fu.write(label)
	with open(imglabel, 'w') as fi:
		for im in imglist:
			imlabel = '%s\n' % (im)
			fi.write(imlabel)

if __name__ == '__main__':
	print('start converting labelx to list format ...')
	main()
	print('...done')

