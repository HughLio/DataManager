"""
create hdf5 dataset from label file
label file format:
imgpath, label

"""
import os
import datetime as dt
import h5py
import numpy as np
from glob import glob
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def proc_img(labelfile, hdf5file):

	imgs = []
	labels = []
	with open(labelfile, 'rb') as fl:
		for line in fl:
			line = line.strip(' ').split()
			imgs.append(line[0])
			labels.append(line[1])

	NUM_IMAGES = len(imgs)
	IMAGE_WIDTH = 256
	IMAGE_HEIGHT = 256
	CHANNELS = 3
	SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS)

	with h5py.File('hdf5file', 'w') as hf:
		for i,img in enumerate(imgs):
			





