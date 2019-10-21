"""
try to evaluate pulp models robustness
input: result json
output: categories pulp sexy normal
"""
pain = [0, 0, 0]
anim = [0, 0, 0]
pink = [0, 0, 0]

with open(resultfile) as fr:
	results = json.load(fr)

for img in results:
	if img['File Name'][0:3] == 'anim':
		anim[img['Top-1 Index']] += 1
	if img['File Name'][0:3] == 'pain':
		pain[img['Top-1 Index']] += 1
	if img['File Name'][0:3] == 'pink':
		pink[img['Top-1 Index']] += 1


print('paint results: pulp:{}, sexy:{}, normal:{}').format(pain[0], pain[1], pain[2])
print('anime results: pulp:{}, sexy:{}, normal:{}').format(anim[0], anim[1], anim[2])
print('pink results: pulp:{}, sexy:{}, normal:{}').format(pink[0], pink[1], pink[2])


