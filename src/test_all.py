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
    'Categories'
]

with open("tasks/README.md", 'r') as readmef:
    task_readme_content = readmef.readlines()

files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f))]
for file in files:
    print(f" --> testing file: {file}")
    if ".md" not in file:
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

            for x in data['Instances']:
                for key in ['input', 'output']:
                    assert key in x, f'expected the key {key} in {x}'
                assert type(x['input']) == str, f'the input of instance {x} is not a string'
                assert type(x['output']) == list, f'the output of instance {x} is not a list'
                for i in x['output']:
                    assert type(i) == str, f'the output is not a string'

            assert len(data['Positive Examples']) > 1, "there must be at least 3 positive example"
            # TODO: add this back in, once we have negative examples for all the tasks
            # assert len(data['Negative Examples']) > 1, "there must be at least one negative example"

            for x in data['Positive Examples'] + data['Negative Examples']:
                for key in ['input', 'output', 'explanation']:
                    assert key in x, f'expected the key {key} in {x}'
                assert type(x['input']) == str, f'the input of example {x} is not a string'
                assert type(x['output']) == str, f'the output of example {x} is not a string'
                assert type(x['explanation']) == str, f'the explanation of example {x} is not a string'

            # make sure there are no repeated input examples
            for x_idx, x in enumerate(data['Instances']):
                for y_idx in range(x_idx + 1, len(data['Instances'])):
                    y = data['Instances'][x_idx]
                    if x['input'] == y['input']:
                        raise Exception(f" * Looks like we have a repeated example here! :-/ \n {x}\n {y}")

            if file not in task_readme_content:
                raise Exception(f' * looks like the task name `{file}` is not included in the task file `tasks/README.md`')

print("Did not find any errors! ✅")
