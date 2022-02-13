import json
from os import listdir, path
from os.path import isfile, join
import argparse
import re
"""
Script for adding the "Reasoning" field for all the tasks of a given dataset.
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
for file in files[begin_task_number:end_task_number + 1]: 
    if ".json" in file:
        print(f" --> adding reasoning to file: {file}")
        file_path = tasks_path + file
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            categories = data['Categories']
            data['Reasoning']=[]
            for category in categories[:]:
                if category.startswith("Reasoning -> "):
                    categories.remove(category)
                    data['Reasoning'].append(category.removeprefix("Reasoning -> "))

        with open(file_path, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4,ensure_ascii=False)

