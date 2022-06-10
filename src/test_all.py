#!/usr/bin/env python3
from iso639 import languages
import json
from os import listdir
from os.path import isfile, join
import argparse
import re
import numpy as np

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
    "Contributors",
    "Categories",
    "Domains",
    "Source",
    "URL",
    "Reasoning"
]

language_names = [
    x.name.replace('(individual language)', '').replace(" languages", "").strip()
    for x in list(languages)
]


def assert_language_name(name):
    assert name in language_names, f"Did not find `{name}` among iso639 language names: {language_names}"


def extract_categories(string):
    """
    Get all the characters between ` and `
    """
    return set(re.findall(r'`(.*?)`', string))


def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise ValueError("duplicate key: %r" % (k,))
        else:
            d[k] = v
    return d

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


with open("tasks/README.md", 'r') as readmef:
    task_readme_content = " ".join(readmef.readlines())
with open("doc/task-hierarchy.md", 'r') as readmef:
    hierarchy_content_lines = readmef.readlines()
    hierarchy_content = " ".join(hierarchy_content_lines)
    all_categories = extract_categories(hierarchy_content)

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
files.sort(key=natural_keys)

# make sure anything that gets mentioned in the readme, correspond to an actual file
task_names = [line.split("`")[1] for line in task_readme_lines if '`' in line]
for name in task_names:
    file_name = name + ".json"
    assert file_name in files, f" Did not find `{file_name}` among {files}"

# test every file (README is skipped)
if not args.task:
    begin_task_number, end_task_number = 1, len(files)

# TODO: over time, we need to fix the skew of the following tasks
skew_exclusion = [
    "150"
]

contributor_stats = {}
categories_stats = {}
reasoning_stats = {}
domain_stats = {}
tasks_count = 0
number_of_instances = 0
for file in files[begin_task_number:end_task_number + 1]:
    if ".json" in file:
        print(f" --> testing file: {file}")
        assert '.json' in file, 'the file does not seem to have a .json in it: ' + file
        file_path = tasks_path + file
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
            except:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f, object_pairs_hook=dict_raise_on_duplicates)
            for key in expected_keys:
                assert key in data, f'did not find the key: {key}'


            assert len(data['Instances']) > 25, f"there must be at least 25 instances; " \
                                                f"currently you have {len(data['Instances'])} instances"
            assert len(data['Instances']) <= 6500, f"there must be at most 6.5k instances; " \
                                                   f"currently you have {len(data['Instances'])} instances"

            assert type(data['Definition']) == list, f'Definition must be a list of strings.'
            assert type(data['Source']) == list, f'Sources must be a list.'
            assert type(data['URL']) == list, f'URL must be a list.'
            assert type(data['Contributors']) == list, f'Contributors must be a list.'
            assert type(data['Categories']) == list, f'Categories must be a list.'
            assert type(data['Reasoning']) == list, f'Reasoning must be a list.'
            assert type(data['Domains']) == list, f'Domains must be a list.'
            
            number_of_instances = number_of_instances + len(data['Instances'])
            for c in data['Categories']:
                assert c in all_categories, f'Did not find category `{c}`'
                if c not in categories_stats:
                    categories_stats[c] = 0
                categories_stats[c] += 1

            for d in data['Domains']:
                assert d in hierarchy_content, f'Did not find domain `{d}`'
                if d not in domain_stats:
                    domain_stats[d] = 0
                domain_stats[d] += 1

            for r in data['Reasoning']:
                assert r in hierarchy_content, f'Did not find reasoning `{r}`'
                if r not in reasoning_stats:
                    reasoning_stats[r] = 0
                reasoning_stats[r] += 1

            for d in data['Definition']:
                assert type(d) == str, f'Each definition must be a string.'
                assert all((lan in d) for lan in data['Input_language'] if
                       lan != 'English'), f'Definition must contain non-English tasks language.'
            assert type(data['Input_language']) == list, f'Input_language must be a list of strings.'
            assert type(data['Output_language']) == list, f'Output_language must be a list of strings.'
            assert type(data['Instruction_language']) == list, f'Output_language must be a list of strings.'

            assert 'instruction_language' not in data, f'Found `instruction_language`, but expected `Instruction_language`.'
            assert 'input_language' not in data, f'Found `input_language`, but expected `Input_language`.'
            assert 'output_language' not in data, f'Found `output_language`, but expected `Output_language`.'

            # make sure we use the standard language names
            for lang in data['Input_language'] + data['Output_language'] + data['Instruction_language']:
                assert_language_name(lang)

            instance_ids = set()
            for x in data['Instances']:
                for key in ['id', 'input', 'output']:
                    assert key in x, f'expected the key {key} in {x}'
                assert x['id'] not in instance_ids, f'found duplicate instance id: {x["id"]}'
                instance_ids.add(x['id'])
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
                                        
            # Make sure there are no link in instances
            url_reg  = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            instances = data['Instances']    
            for instance in instances:
                ck_url = re.findall(url_reg, instance['input'])
                if ck_url:
                    print(f'⚠️ WARNING: Looks like there is a link in the input: {ck_url}')
                    break
                    
            # make sure classes are balanced
            output = [ins['output'] for ins in instances]
            # flattens the nested arrays
            outputs = sum(output, [])
            value, counts = np.unique(outputs, return_counts=True)
            
            task_number = file.replace("task", "").split("_")[0]
            # TODO: drop this condition 
            if int(task_number) not in [902, 903]:
                assert len(value) > 1, f" Looks like all the instances are mapped to a single output: {value}"

            if task_number not in skew_exclusion and len(value) < 15:
                norm_counts = counts / counts.sum()
                entropy = -(norm_counts * np.log(norm_counts) / np.log(len(value))).sum()

                assert entropy > 0.8, f"Looks like this task is heavily skewed!\n   📋 classes: {value} \n   📋 Norm_counts: {norm_counts} \n   📋 Distribution of classes: {counts} \n   📊 entropy= {entropy}"
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

            for c in data['Contributors']:
                if c not in contributor_stats:
                    contributor_stats[c] = 0
                contributor_stats[c] += 1
            tasks_count = tasks_count + 1

# test the the official splits
for split_name in ["default", "xlingual"]:
    train_tasks = [l.strip() for l in open(f"splits/{split_name}/train_tasks.txt")]
    test_tasks = [l.strip() for l in open(f"splits/{split_name}/test_tasks.txt")]
    excluded_tasks = [l.strip() for l in open(f"splits/{split_name}/excluded_tasks.txt")]

    # make east task in the split actually exists
    for task in train_tasks + test_tasks + excluded_tasks:
        assert task in task_names, f" Task {task} doesn't exist, but it's included in the {split_name} split."
    # make sure each task appears in the split 
    for task in task_names:
        assert task in train_tasks + test_tasks + excluded_tasks, f" Task {task} is missing in the {split_name} split."
    # make sure there is no overlap between test and train task names in the splits files.
    assert len(set(train_tasks) & set(test_tasks)) == 0, f" {split_name} split has overlap tasks in the train & test sets."
    assert len(set(train_tasks) & set(excluded_tasks)) == 0, f" {split_name} split has overlap tasks in the train & excluded sets."
    assert len(set(test_tasks) & set(excluded_tasks)) == 0, f" {split_name} split has overlap tasks in the test & excluded sets."

print("Did not find any errors! ✅")

print("\n  - - - - - Contributors >= 25 tasks - - - - - ")
keyvalues = sorted(list(contributor_stats.items()), key=lambda x: x[1])
for author, count in keyvalues:
    if count >= 25:
        print(f" ✍️ {author} -> {count}")

print("\n  - - - - - Category Stats - - - - - ")
keyvalues = sorted(list(categories_stats.items()), key=lambda x: x[1])
for cat, count in categories_stats.items():
    print(f" ✍️ {cat} -> {count}")

print("\n  - - - - - Domain Stats - - - - - ")
keyvalues = sorted(list(domain_stats.items()), key=lambda x: x[1])
for dom, count in domain_stats.items():
    print(f" ✍️ {dom} -> {count}")

print("\n  - - - - - Reasoning Stats - - - - - ")
keyvalues = sorted(list(reasoning_stats.items()), key=lambda x: x[1])
for res, count in reasoning_stats.items():
    print(f" ✍️ {res} -> {count}")

print("\n  - - - - - Instances Stats - - - - - ")
average_number_of_instances = number_of_instances / tasks_count
print(f" ✍️ Average number of Instances -> {average_number_of_instances}")
