import os
import json

json_file = '../pulp-det/juggdet_train_1211.json'
train_file = 'juggdet_train_1211s.json'
val_file = 'juggdet_val_1211.json'
trainjson = "juggdet_train_1211.json"

imglst= 'juggdet_val_1211.lst'

label_list = []

with open(json_file) as fj:
	label =json.load(fj)
info  = label['info']
# print info
imglist = label['images']
detlist = label['annotations']
clslist = label['categories']
# print str(clslist)

val_detlist = []
val_imgid = []
val_imglist = []
counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
number = [0, 16200, 9500, 14000, 9500, 3000, 230, 11200, 1000, 2008, 3200]
count = 0
for box in detlist:
	categories = box['category_id']
	# print counter[categories]
	# print number[categories]
	# print box
	if counter[categories] < number[categories]:
		box['id'] = count
		count += 1
		val_detlist.append(box)
		detlist.remove(box)
		if box['image_id'] not in val_imgid:
			counter[categories] += 1
			val_imgid.append(box['image_id'])

for img in imglist:
	if img['file_name'] in val_imgid:
		val_imglist.append(img)
		imglist.remove(img)

with open(imglst, 'w') as fi:
	for image in val_imgid:
		line = "%s\n" % image
		fi.write(line)

traindata = {
  "info": {
    "description": "dummy datasets bounding-box annotations", 
    "url": "null", 
    "version": "v3.1", 
    "year": "2019", 
    "contributor": "qn", 
    "date_created": "2018-06-14"
  },
  "images": imglist,
  "annotations": detlist,
  "categories" : clslist
  }
trainset = json.dumps(traindata, indent=4, separators=(',', ':'))

with open(trainjson, 'w') as ft:
	ft.write(trainset)

valdata = {
  "info": {
    "description": "dummy datasets bounding-box annotations", 
    "url": "null", 
    "version": "v3.1", 
    "year": "2019", 
    "contributor": "qn", 
    "date_created": "2018-06-14"
  },
  "images": val_imglist,
  "annotations": val_detlist,
  "categories" : clslist
  }
valset = json.dumps(valdata, indent=4, separators=(',', ':'))

with open(val_file, 'w') as fv:
	fv.write(valset)



	
