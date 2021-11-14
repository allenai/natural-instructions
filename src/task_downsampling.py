#!/usr/bin/env python3
import json
import random
from os import listdir
from os.path import isfile, join
import numpy as np

tasks_path = 'tasks/'
files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
files.sort()

for file in files:
    if ".json" in file:
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            data = json.load(f)
            instances = data['Instances']
            output=[ins['output'] for ins in instances]
            outputs = sum(output, [])

            value,counts = np.unique(outputs, return_counts=True)
            newcounts={}
            min_value=np.min(counts)
            new_data={}
            new_data=data
            new_data['Instances']=[]
            for ins in instances:
                output=ins['output'][0]
                if output not in newcounts:
                    newcounts[output]=0
                if newcounts[output]<= 2*min_value:
                    new_data['Instances'].append(ins)
                    newcounts[output]+=1

            random.shuffle(new_data["Instances"])
        with open(file_path, 'w') as outfile:
            json.dump(new_data, outfile, indent=4,ensure_ascii=False)