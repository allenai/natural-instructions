#!/usr/bin/env python3
import json
import pandas as pd
from collections import OrderedDict

tasks_path = 'tasks/'
meta = pd.read_csv("Natural Instructions V2 Exps - tasks review 0323 (final).csv").values
key_order = ("Contributors","Source","URL","Categories","Reasoning","Definition","Input_language","Output_language","Instruction_language","Domains","Positive Examples","Negative Examples","Instances")

def ordered(d, key_order):
    return OrderedDict([(key, d[key]) for key in key_order])
    
for row in range(len(meta)):
        file = meta[row][0] + '.json'
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                        
        data['Categories'] = [meta[row][5]]
        data['Source'] = [meta[row][2]]        
        data['URL'] = [meta[row][3]]     
        
        data = ordered(data, key_order)
        with open(file_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4,ensure_ascii=False)