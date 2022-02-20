import json
import os
from os import listdir, path
from os.path import isfile, join

tasks_path = 'tasks/'
def update_definitions(tasks_path):
    files = [join(tasks_path, f) for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
    files.sort()
    for file in files: 
        if file.endswith('.json'):
            print(file)
            with open(file) as f:
                data = json.load(f)
            definition = data['Definition']
            data['Definition'] = [definition]
            with open(file, 'w') as o:
                dump = json.dumps(data, indent = 4)
                o.write(dump)

if __name__ == "__main__":
    update_definitions(tasks_path)
