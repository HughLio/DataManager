"""
crop image for test
crop size up to the image size
"""
import os
import cv2

filelst = '.lst'
savepath = ''
with open(filelst, 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		imagepath = line.strip()
		imagename = [j.strip() for j in img_path.strip().split('/')]
		img_name = imagename[-1]

		im = cv2.imread(imagepath)
		shape = im.shape
		height = shape[0]
		width = shape[1]

		offsety = height * 0.1
		offsetx = width * 0.1

		crop_img = im[offsety, height-offsety, offsetx, width-offsetx]

		print(crop_img.shape)

		cv2.imwrite(savepath, img_name)


