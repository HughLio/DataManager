"""
convert labelx format to label-lst
label-lst:
url label
imagename label
"""
import json
import os
import argparse

parser = argparse.ArgumentParser(description='convert labelx format to label lst')
parser.add_argument('--jsonpath', dest='json_dir',
                    help='labelx results path',
                    default=None, type=str, required=True)
parser.add_argument('--savepath', dest='save_path',
                    help='save file urilst ',
                    default='.', type=str)

args = parser.parse_args()
def main():
	jsondir = args.json_dir
	path = args.save_path
	localtime = time.localtime(time.time())
	date = date = str(localtime.tm_mon) + str(localtime.tm_mday)
	urlst = path + '/uri' + date + '.lst'
	imglabel = path + '/imglabel' + date + '.lst'

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

