"""
ananly log downloaded from pandora
get the data from legao platform
To Do
@HughLio
--argruments: label: pulp , sexy, nsfw
              savepath
--output: urifile labelfile
"""
import json
import string
import argparse
import time

parser = argparse.ArgumentParser(description='analy log downloaded from pandora')
parser.add_argument('--log', dest='log_file',
                    help='log file ',
                    default=None, type=str, required=True)

parser.add_argument('--label', dest='label_name',
                    help='label file fliter default pulp ',
                    default='pulp', type=str)

parser.add_argument('--savepath', dest='save_path',
                    help='save file urilst ',
                    default='.', type=str)


args = parser.parse_args()
path = args.save_path
logfile = args.log_file
label = args.label_name

localtime = time.localtime(time.time())
date = date = str(localtime.tm_mon) + str(localtime.tm_mday)

urifile = path + "/" + "uri" +date +".lst"
labelfile = path + "/" + "urilabel" +date +".lst"

reqpulpcount = 0
reqinfantcount = 0
uidlist = list()
labelst = dict()
with open(logfile) as fr:
	logs = fr.readlines()

for dic in logs:
	try:
		log = json.loads(dic)
	except:
		print "decode log error!", log
	if "pulp" in log['eval_response']['scenes'].keys():
		pulp = log['eval_response']['scenes']['pulp']
		reqpulpcount += 1
		if label == 'nsfw':
			if pulp['details'][0]['label'] != 'normal':
				reqinfantcount += 1
				if log['uri_data'] != "":
					keys = [i.strip() for i in log['uri_data'][0].strip().split('/')]
					try:
						key = keys[-2] + '/' + keys[-1]
					except:
						print key
						continue
					uidlist.append(key)
					labelst[log['uri_data'][0]] = pulp['details'][0]['label']
		else:
			if pulp['details'][0]['label'] == label:
				reqinfantcount += 1
				if log['uri_data'] != "":
					keys = [i.strip() for i in log['uri_data'][0].strip().split('/')]
					try:
						key = keys[-2] + '/' + keys[-1]
					except:
						print key
						continue
					uidlist.append(key)
					labelst[log['uri_data'][0]] = pulp['details'][0]['label']
print("images called pulp API: {}".format(reqpulpcount),
	label + "results images: {}".format(reqinfantcount))

with open(urifile, 'w') as fu:
	for i in uidlist:
		fu.write(i)
		fu.write('\n')

with open(labelfile, 'w') as fl:
	for l in labelst.keys():
		line = '%s %s\n' % (l, labelst[l])
		fl.write(line)
