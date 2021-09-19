#!/usr/bin/env python3
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
    'Contributors',
    'Categories',
    'Source'
]

with open("tasks/README.md", 'r') as readmef:
    task_readme_content = " ".join(readmef.readlines())
files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
files.sort()

for file in files:
    if ".md" not in file:
        print(f" --> testing file: {file}")
        assert '.json' in file, 'the file does not seem to have a .json in it: ' + file
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            data = json.load(f)
            for key in expected_keys:
                assert key in data, f'did not find the key: {key}'

            assert len(data[
                           'Instances']) > 25, f"there must be at least 25 instances; currently you have {len(data['Instances'])} instances"
            assert len(data[
                           'Instances']) <= 6500, f"there must be at most 6.5k instances; currently you have {len(data['Instances'])} instances"

            assert type(data['Source']) == list, f'Sources must be a list.'
            assert type(data['Contributors']) == list, f'Contributors must be a list.'
            assert type(data['Categories']) == list, f'Categories must be a list.'
            
            for x in data['Instances']:
                for key in ['input', 'output']:
                    assert key in x, f'expected the key {key} in {x}'
                assert type(x['input']) == str, f'the input of instance {x} is not a string'
                assert type(x['output']) == list, f'the output of instance {x} is not a list'
                for i in x['output']:
                    assert type(i) == str, f'the output is not a string'
            assert len(data['Positive Examples']) > 1, "there must be at least 3 positive example"
            assert len(data['Negative Examples']) > 0, "there must be at least 2 negative example"

            for x in data['Positive Examples'] + data['Negative Examples']:
                for key in ['input', 'output', 'explanation']:
                    assert key in x, f'expected the key {key} in {x}'
                assert type(x['input']) == str, f'the input of example {x} is not a string'
                assert type(x['output']) == str, f'the output of example {x} is not a string'
                assert type(x['explanation']) == str, f'the explanation of example {x} is not a string'

            # Make sure there are no repeated input examples
            instances = data['Instances']
            set_of_instances = {instance['input'] for instance in instances}
            # Because the set length and total length are different, there must be a duplicate input
            if len(instances) != len(set_of_instances):
                for instance in instances:
                    # If the instance is a duplicate then it has already been removed from the set and a KeyError will be thrown
                    try:
                        set_of_instances.remove(instance['input'])
                    except KeyError:
                        raise Exception(f" * Looks like we have a repeated example here! Merge outputs before removing duplicates. :-/ \n {instance}")


            # Make sure there are no examples repeated across instances and positive examples
            examples = [ex['input'] for ex in data['Positive Examples']]
            for instance in instances:
                if instance['input'] in examples:
                    raise Exception(f" * Looks like we have a same example across positive examples and instances! Drop the example from the instances. :-/ \n {instance}")

                assert len(instance['output']) > 0, "all the instances must have at least one output"

            true_file = file.replace(".json", "")
            for char in true_file:
                if char.isupper():
                    raise Exception(f" * Looks like there is an uppercase letter in `{true_file}`. All letters should be lowercased.")

            if file in task_readme_content:
                raise Exception(f" * Looks like the .json file extension ending is present with the task name in `tasks/README.md` when it should just be `{true_file}`")

            if true_file not in task_readme_content:
                raise Exception(f' * Looks like the task name `{true_file}` is not included '
                                f'in the task file `tasks/README.md`')

print("Did not find any errors! ✅")
