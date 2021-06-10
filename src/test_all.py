import json
from os import listdir
from os.path import isfile, join

# read all the tasks and make sure that they're following the right pattern
tasks_path = 'tasks/'

expected_keys = [
    "Definition",
    "Positive Examples",
    "Negative Examples",
    "Instances",
    'Contributor',
    'Categories'
]

files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
for file in files:
    if ".md" not in file:
        assert '.json' in file, 'the file does not seem to have a .json in it: ' + file
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            data = json.load(f)
            # for key in expected_keys:
            #     assert key in data, f'did not find the key: {key}'

            # for x in data['Instances']:
            #     assert type(x['input']) == str, f'the input of instance {x} is not a string'
            #     assert type(x['output']) == list, f'the output of instance {x} is not a list'
                # assert type(x['output']) == list, f'the output of instance {x} is not a list'
