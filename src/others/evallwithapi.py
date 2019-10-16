from qiniu import Auth, QiniuMacAuth, http
import requests, json
import os

url = 'http://ai.qiniuapi.com/v3/image/censor'
urilst = '/Users/hugh/Documents/tools/upload/isis-uri.lst'
savefile = '/Users/hugh/Documents/testset/isis-res.json'


# access_key = ''
auth = QiniuMacAuth(access_key, secret_key)

body = {
	"data" : {
	"uri": 'uri'
	},
	"params" : {
	"scenes":['terror']
	}
}
results = []
with open(urilst, 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		spline = line.strip()
		body["data"]["uri"] = spline
		# print body
		ret, res = http._post_with_qiniu_mac(url, body, auth)
		newret = json.dumps(ret, indent=4, ensure_ascii=False)
		ret = json.loads(newret)
		
		# res = json.dumps(ret, indent=4, ensure_ascii=False)
		try:
			ret["uri"] = spline
		except:
			print ret
			print spline
			continue
		results.append(ret)

with open(savefile, 'w') as fo:
		for l in results:
			json.dump(l, fo)
			fo.write('\n')


