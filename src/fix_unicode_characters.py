import json
import os
from os import listdir, path
from os.path import isfile, join

"""
Script for fixing unicode characters in task files
"""

tasks_path = 'tasks/'
def fix_characters(tasks_path):
    files = [join(tasks_path, f) for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
    files.sort()
    for file in files: 
        if file.endswith('.json'):
            print(file)
            with open(file) as f:
                data = json.load(f)
            with open(file, 'w') as o:
                dump = json.dumps(data, ensure_ascii = False, indent = 4)
                o.write(dump)

if __name__ == "__main__":
    fix_characters(tasks_path)
