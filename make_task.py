#!/usr/bin/env python3
import json

fname = 'round_2n.json'
src = json.load(open(fname))

dic = {str(int(2**n)): 0 for n in range(1,15)}
print(dic)
for ex in src['Instances']:
    arr = ex['output'][0]
    arr = arr.replace('[', '')
    arr = arr.replace(']', '')
    for num in arr.split(','):
        num = num.strip()
        dic[num] += 1

for k, v in dic.items():
    print('k = {} v = {}'.format(k, v))
