#!/usr/bin/env python3
import copy
import json
import random
from os import listdir
from os.path import isfile, join
import numpy as np

tasks_path = 'tasks/'
files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
files.sort()

task_ids_to_downsample = [21]

for file in files:
    if ".json" in file:
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            task_number = int(file.replace("task", "").split("_")[0])
            if task_number not in task_ids_to_downsample:
                continue
            data = json.load(f)
            instances = data['Instances']
            output=[ins['output'] for ins in instances]
            outputs = sum(output, [])

            value,counts = np.unique(outputs, return_counts=True)
            norm_counts = counts / counts.sum()
            entropy = -(norm_counts * np.log(norm_counts) / np.log(len(value))).sum()
            print(f" Before: 📋 classes: {value} \n   📋 Norm_counts: {norm_counts} \n   📋 Distribution of classes: {counts} \n   📊 entropy= {entropy}")

            newcounts={}
            min_value=np.min(counts)
            new_data=copy.deepcopy(data)
            new_data['Instances']=[]
            for ins in instances:
                output=ins['output'][0]
                if output not in newcounts:
                    newcounts[output]=0
                if newcounts[output]<= 3*min_value:
                    new_data['Instances'].append(ins)
                    newcounts[output]+=1

            random.shuffle(new_data["Instances"])

            instances = data['Instances']
            output=[ins['output'] for ins in instances]
            outputs = sum(output, [])
            value,counts = np.unique(outputs, return_counts=True)
            norm_counts = counts / counts.sum()
            entropy = -(norm_counts * np.log(norm_counts) / np.log(len(value))).sum()
            print(f" After: 📋 classes: {value} \n   📋 Norm_counts: {norm_counts} \n   📋 Distribution of classes: {counts} \n   📊 entropy= {entropy}")

        with open(file_path, 'w') as outfile:
            json.dump(new_data, outfile, indent=4,ensure_ascii=False)