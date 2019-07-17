# Generate Label list
import os

listname = "all.lst"
listf = "pulp.lst"
imgf ="pulp_img.lst"

new_list = []
imgname_list = []
# pulp: 0 sexy: 1 normal 2
# normal: 0 nsfw: 1
pulplabel = 0
sexylabel = 0
normallabel = 0

def analyrecformat(line):
	del line[0]
	temp = line[0]
	line[0] = line[1]
	line[1] = temp
	return line


with open(listname) as f:
	while(True):
	    line = f.readline()
	    if not line:
	    	break
	    # print line
	    spline = [i.strip() for i in line.strip().split('\t')]
	    # print spline 
	    if len(spline) == 3 :
	    	spline = analyrecformat(spline)
	    else:
	    	spline = spline = [i.strip() for i in line.strip().split(' ')]
	    img_path = spline[0]
	    # line[-1] = imagePath + img_name 
	    img_name = [j.strip() for j in img_path.strip().split('/')]

	    label = spline[1]
	    if(label == '0'):
	    	pulplabel += 1
	    elif(label == '1'):
	    	sexylabel += 1
	    else:
	    	normallabel += 1

	    spline = '%s %s\n' % (spline[0], spline[1])
	    # print img_name[-1]
	    # print spline

	    new_list.append(spline)
	    imgname_list.append(img_name[-1])

newlist = list(set(new_list))
imglist = list(set(imgname_list))
#print pulplabel, sexylabel, normallabel

with open(listf, 'w') as l_fout, open(imgf, 'w') as i_fout:
	for label in newlist:
		# line = "%s,%t,%s,%s\n" % label
		l_fout.write(label)

	for img in imglist:
		line = '%s\n' % img
		i_fout.write(line)