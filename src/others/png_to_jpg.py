"""
convert .png to .jpg
"""
import os
from PIL import Image

dirname = '/Users/hugh/Documents/data/cartoon/png/'
savepath = '/Users/hugh/Documents/data/cartoon/jpeg/'

file_list = os.listdir(dirname)

for img in file_list:
	imname = img[0:-3] + 'jpeg'
	try:
		im = Image.open(dirname + img)
		im = im.convert('RGB')
		im.save(savepath + imname)
	except UserWarning:
		print img