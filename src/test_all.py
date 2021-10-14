#!/usr/bin/env python3
from iso639 import languages
import json
from os import listdir
from os.path import isfile, join

# make sure that there is no json file in the root directory 
root_files = [f for f in listdir('.') if isfile(join('.', f))]
for f in root_files:
    assert '.json' not in f, 'looks like there is a JSON file in the main directory???'

# read all the tasks and make sure that they're following the right pattern
tasks_path = 'tasks/'

expected_keys = [
    "Definition",
    "Input_language",
    "Output_language",
    "Positive Examples",
    "Negative Examples",
    "Instances",
    'Contributors',
    'Categories',
    'Source'
]

language_names = [
    x.name.replace('(individual language)', '').replace(" languages", "").strip()
    for x in list(languages)
]


def assert_language_name(name):
    assert name in language_names, f"Did not find `{name}` among iso639 language names: {language_names}"


# TODO: over time, these should be moved up to "expected_keys"
suggested_keys = [
    "Domains"
]

with open("tasks/README.md", 'r') as readmef:
    task_readme_content = " ".join(readmef.readlines())
with open("doc/task-hierarchy.md", 'r') as readmef:
    hierarchy_content = " ".join(readmef.readlines())

# make sure there are no repeated lines in the task file
task_readme_lines = [x for x in task_readme_content.split("\n") if len(x) > 5]
if len(set(task_readme_lines)) != len(task_readme_lines):
    diff = "\n --> ".join([x for x in task_readme_lines if task_readme_lines.count(x) > 1])
    assert False, f'looks like there are repeated lines in the task readme file?? \n {diff}'

# make sure that the lines are sorted
task_numbers = [int(line.replace("`task", "").split("_")[0]) for line in task_readme_lines if "`task" in line]
for i in range(0, len(task_numbers) - 1):
    num1 = task_numbers[i]
    num2 = task_numbers[i + 1]
    assert num1 <= num2, f"ERROR: looks like `{num1}` appears before `{num2}`."

files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
files.sort()

# make sure anything that gets mentioned in the readme, correspond to an actual file
task_names = [line.split("`")[1] for line in task_readme_lines if '`' in line]
for name in task_names:
    file_name = name + ".json"
    assert file_name in files, f" Did not find `{file_name}` among {files}"

for file in files:
    if ".json" in file:
        print(f" --> testing file: {file}")
        assert '.json' in file, 'the file does not seem to have a .json in it: ' + file
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            data = json.load(f)
            for key in expected_keys:
                assert key in data, f'did not find the key: {key}'

            for key in suggested_keys:
                if key not in data:
                    print(f'⚠️ WARNING: did not find the key: {key}')

            assert len(data['Instances']) > 25, f"there must be at least 25 instances; " \
                                                f"currently you have {len(data['Instances'])} instances"
            assert len(data['Instances']) <= 6500, f"there must be at most 6.5k instances; " \
                                                   f"currently you have {len(data['Instances'])} instances"

            assert type(data['Definition']) == str, f'Definition must be a str.'
            assert type(data['Source']) == list, f'Sources must be a list.'
            assert type(data['Contributors']) == list, f'Contributors must be a list.'
            assert type(data['Categories']) == list, f'Categories must be a list.'
            for c in data['Categories']:
                if c not in hierarchy_content:
                    print(f'⚠️ WARNING: Did not find category `{c}`')
            if "Domains" in data:
                assert type(data['Domains']) == list, f'Domains must be a list.'
                for d in data['Domains']:
                    assert d in hierarchy_content, f'Did not find domain `{d}`'

            assert type(data['Input_language']) == list, f'Input_language must be a str.'
            assert type(data['Output_language']) == list, f'Output_language must be a str.'
            assert type(data['Instruction_language']) == list, f'Output_language must be a str.'

            assert 'instruction_language' not in data, f'Found `instruction_language`, but expected `Instruction_language`.'
            assert 'input_language' not in data, f'Found `input_language`, but expected `Input_language`.'
            assert 'output_language' not in data, f'Found `output_language`, but expected `Output_language`.'

            # make sure we use the standard language names
            for lang in data['Input_language'] + data['Output_language'] + data['Instruction_language']:
                assert_language_name(lang)

            for x in data['Instances']:
                for key in ['input', 'output']:
                    assert key in x, f'expected the key {key} in {x}'
                assert type(x['input']) == str, f'the input of instance {x} is not a string'
                assert type(x['output']) == list, f'the output of instance {x} is not a list'
                assert len(x['input']) > 0, f"looks like an input `{x['input']}` is empty?"
                assert len(x['output']) > 0, f"looks like an output `{x['output']}` is empty?"
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
                        raise Exception(f" * Looks like we have a repeated example here! "
                                        f"Merge outputs before removing duplicates. :-/ \n {instance}")

            # Make sure there are no examples repeated across instances and positive examples
            examples = [ex['input'] for ex in data['Positive Examples']]
            for instance in instances:
                if instance['input'] in examples:
                    raise Exception(f" * Looks like we have a same example across positive examples and instances! "
                                    f"Drop the example from the instances. :-/ \n {instance}")

                assert len(instance['output']) > 0, "all the instances must have at least one output"

            true_file = file.replace(".json", "")
            for char in true_file:
                if char.isupper():
                    raise Exception(f" * Looks like there is an uppercase letter in `{true_file}`. "
                                    f"All letters should be lowercased.")

            if file in task_readme_content:
                raise Exception(f" * Looks like the .json file extension ending is "
                                f"present with the task name in `tasks/README.md` when it should just be `{true_file}`")

            if true_file not in task_readme_content:
                raise Exception(f' * Looks like the task name `{true_file}` is not included '
                                f'in the task file `tasks/README.md`')

            if task_readme_content.count(true_file) > 1:
                raise Exception(f' * Looks like the task name `{true_file}` is repeated in '
                                f'the task file `tasks/README.md`')

print("Did not find any errors! ✅")
