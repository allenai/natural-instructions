import json
import os
from os import listdir, path
from os.path import isfile, join

"""
Script for adding the "Domains" field for all the tasks of a given dataset.
"""


with open("doc/task-hierarchy.md", 'r') as readmef:
    hierarchy_content = " ".join(readmef.readlines())

tasks_path = 'tasks/'
# modify these variables as needed
dataset_name = "mctaco"
domains = [
        "News",
        "Wikipedia",
        "Law",
        "Justice",
        "History",
        "History -> 9/11 Reports",
        "Anthropology",
        "School Science Textbooks",
        "Fiction"
    ]



def add_domain(tasks_path, dataset_name, domains):
    for d in domains: 
        assert d in hierarchy_content, f"domain {d} not in task-hierarchy"
    # find the task files containing the dataset
    files = [join(tasks_path, f) for f in listdir(tasks_path) if isfile(join(tasks_path, f)) and dataset_name in f]
    files.sort()
    # add the domain
    for file in files: 
        with open(file, 'r') as f:
            data = json.load(f)
            data['Domains'] = domains
        os.remove(file)
        with open(file, 'w') as f:
            modified_json = json.dumps(data, indent=4, ensure_ascii=False)
            print(modified_json, file=f)

if __name__ == "__main__":
    add_domain(tasks_path, dataset_name, domains)
