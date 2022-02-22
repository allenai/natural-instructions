import json
from os import listdir, path
from os.path import isfile, join
import argparse
import re

"""
Script for sparsifying the categories, domains, and reasoning fields.
In order to run the experiments with fewer general high-frequency categories instead of fine-grained ones.
"""

tasks_path = 'tasks/'

# get the range of task you want to test, if specified in the command line
parser = argparse.ArgumentParser()
parser.add_argument("--task",
                    nargs=2,
                    type=int,
                    required=False,
                    help="The range of task you want to parse")

args = parser.parse_args()
if args.task:
    begin_task_number, end_task_number = args.task[0], args.task[1]
    assert begin_task_number > 0, "begin task must be greater than 0"
    assert end_task_number > begin_task_number, "please specify a range of task you would like to test; i.e. the end task number must be greater than beginning task number"

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
files.sort(key=natural_keys)

# test every file (README is skipped)
if not args.task:
    begin_task_number, end_task_number = 1, len(files)
    
with open('doc/categories_map.json', 'r', encoding='utf-8') as f:
    category_map = json.load(f)

with open('doc/domains_map.json', 'r', encoding='utf-8') as f:
    domain_map = json.load(f)
    
with open('doc/reasonings_map.json', 'r', encoding='utf-8') as f:
    reasoning_map = json.load(f)
    
for file in files[begin_task_number:end_task_number + 1]: 
    if ".json" in file:
        print(f" --> updating file: {file}")
        file_path = tasks_path + file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
                        
            new_categories = [category_map[category] for category in data['Categories']]
            data['Categories'] = list(set(sum(new_categories, [])))
            
            new_domains = [domain_map[domain] for domain in data['Domains']]
            data['Domains'] = list(set(sum(new_domains, [])))
            
            new_reasonings = [reasoning_map[reasoning] for reasoning in data['Reasoning']]
            data['Reasoning'] = list(set(sum(new_reasonings, [])))
            
        with open(file_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4,ensure_ascii=False)