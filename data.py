#!/usr/bin/env python
import json
import random
import numpy as np

fname = 'round_2n.json'

task = json.load(open(fname))
task['Instances'] = []

def func(arr):
    lg = np.log2(arr)
    lg = np.floor(lg)
    out = []
    for log, arg in zip(lg, arr):
        top = int(2**(log+1))
        bot = int(2**log)
        #print('For arg {} top is {} and diff is {} bot is {} and diff is {}'.format(arg, top, top - arg, bot, arg - bot))
        if top - arg > arg - bot:
            out.append(bot)
        else:
            out.append(top)
    return out
        
for _ in range(2000):
    size = random.randint(3, 10)
    inp = np.random.randint(low=2, high=5000, size=(size,))
    out = func(inp)
    inp = inp.tolist()
    instance = {'input': str(inp), 'output': [str(out)]}
    #print(instance)
    task['Instances'].append(instance)

for _ in range(2000):
    size = random.randint(3, 10)
    inp = np.random.randint(low=2, high=1000, size=(size,))
    out = func(inp)
    inp = inp.tolist()
    instance = {'input': str(inp), 'output': [str(out)]}
    #print(instance)
    task['Instances'].append(instance)

for _ in range(1000):
    size = random.randint(3, 10)
    inp = np.random.randint(low=2, high=70, size=(size,))
    out = func(inp)
    inp = inp.tolist()
    instance = {'input': str(inp), 'output': [str(out)]}
    #print(instance)
    task['Instances'].append(instance)

for _ in range(1000):
    size = random.randint(3, 10)
    inp = np.random.randint(low=2, high=16, size=(size,))
    out = func(inp)
    inp = inp.tolist()
    instance = {'input': str(inp), 'output': [str(out)]}
    #print(instance)
    task['Instances'].append(instance)

for _ in range(500):
    size = random.randint(3, 10)
    inp = np.random.randint(low=2, high=5, size=(size,))
    out = func(inp)
    inp = inp.tolist()
    instance = {'input': str(inp), 'output': [str(out)]}
    #print(instance)
    task['Instances'].append(instance)
json.dump(task, open(fname, 'w'), indent=4)
