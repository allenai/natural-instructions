'''
Given a task file, it creates a single file for crowd annotations (the input to AMTI).
For example: python 1.amti_create_input_data.py --start  5 --end 20 --eval_count 10
'''
import json
import random
import argparse
from os import listdir
from os.path import isfile, join

tasks_path = '../../tasks/'


def read_file(file):
    with open(tasks_path + file, 'r') as f:
        return json.load(f)


def normalize(str):
    return str.replace('"', '\'').replace('`', '\'').replace('&', ' and ').encode('ascii', 'ignore').decode('ascii').replace('<br>', '\n').replace('<', '[').replace('>', ']').replace('\n', '<br>')

files = [f for f in listdir(tasks_path) if isfile(join(tasks_path, f)) and ".json" in f]
task_ids_to_file = {}

for f in files:
    id = f.split("_")[0].replace("task", "")
    # print(id)
    id = int(id)
    task_ids_to_file[id] = f


def process_single_file(start, end, max_count):
    fout = open(f"start={start}_end={end}_max_size={max_count}.jsonl", "w")
    for idx in range(start, end + 1):
        if idx not in task_ids_to_file:
            continue
        file = task_ids_to_file[idx]

        # grouping instances into groups of size 5
        json_content = read_file(file)

        if json_content["Input_language"] != ["English"] or json_content["Output_language"] != ["English"]:
            continue

        positive_examples = json_content['Positive Examples']
        negative_examples = json_content['Negative Examples']
        instances = json_content['Instances']

        # make sure the annotators see all the examples
        random.shuffle(positive_examples)
        random.shuffle(negative_examples)
        random.shuffle(instances)

        positive_examples = positive_examples[:5]
        negative_examples = negative_examples[:3]

        n = 2
        chunks = [instances[i:i + n] for i in range(0, len(instances), n)]
        for i, chunk in enumerate(chunks):
            if i * n > int(max_count):
                break
            map = {
                'file': normalize(file),
                'instructions': normalize(json_content['Definition']),
            }

            map[f'positive_example_count'] = len(positive_examples)
            map[f'negative_example_count'] = len(negative_examples)

            for idx, ex in enumerate(positive_examples):
                map[f'positive_ex_{idx}_input'] = normalize(ex['input'])
                map[f'positive_ex_{idx}_output'] = normalize(ex['output'])
                map[f'positive_ex_{idx}_explanation'] = normalize(ex['explanation'])

            for idx, ex in enumerate(negative_examples):
                map[f'negative_ex_{idx}_input'] = normalize(ex['input'])
                map[f'negative_ex_{idx}_output'] = normalize(ex['output'])
                map[f'negative_ex_{idx}_explanation'] = normalize(ex['explanation'])

            for idx, ex in enumerate(chunk):
                map[f'instance_{idx}_input'] = normalize(ex['input'])
                map[f'instance_{idx}_output'] = "///".join([normalize(x) for x in ex['output']])

            fout.write(json.dumps(map) + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A script for preparing natural instructions tasks for human evaluation')
    parser.add_argument('--start', help='id of the start task inside `tasks/`')
    parser.add_argument('--end', help='id of the end task inside `tasks/`')
    parser.add_argument('--eval_count', help='how many instances to use in this evaluation. '
                                             '100 should be enough for reliable estimates.')
    args = parser.parse_args()

    print(" >>>>>>>>> Processing with the following arguments: ")
    print(f" * start task id: {args.start}")
    print(f" * end task id: {args.end}")
    print(f" * count of samples from each task: {args.eval_count}")

    process_single_file(int(args.start), int(args.end), args.eval_count)
