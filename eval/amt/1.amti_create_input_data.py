'''
Given a task file, it creates a single file for crowd annotations (the input to AMTI).
For example: python 1.amti_create_input_data.py --start  5 --end 20 --num_instances_per_task 10
Or you can create for all the default test tasks: python 1.amti_create_input_data.py --process_default_test_tasks --num_instances_per_task 20
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


def process_tasks_from_start_to_end(start, end, num_instances_per_task):
    fout = open(f"start={start}_end={end}_max_size={num_instances_per_task}.jsonl", "w")
    for idx in range(start, end + 1):
        if idx not in task_ids_to_file:
            continue
        file = task_ids_to_file[idx]

        # grouping instances into groups of size 5
        json_content = read_file(file)

        if json_content["Input_language"] != ["English"] or json_content["Output_language"] != ["English"]:
            continue
        if isinstance(json_content["Definition"], list):
            json_content["Definition"] = json_content["Definition"][0] 

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
            if i * n > int(num_instances_per_task):
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


def process_default_test_tasks(num_instances_per_task):
    default_test_categories = [
        "Textual Entailment",
        "Cause Effect Classification",
        "Coreference Resolution",
        "Dialogue Act Recognition",
        "Answerability Classification",
        "Overlap Extraction",
        "Word Analogy",
        "Keyword Tagging",
        "Question Rewriting",
        "Title Generation",
        "Data to Text",
        "Grammar Error Correction"
    ]
    fout = open(f"default_test_tasks_inst_num={num_instances_per_task}.jsonl", "w")

    for file in files:
        json_content = read_file(file)
        if json_content["Categories"][0] not in default_test_categories:
            continue
        if json_content["Input_language"] != ["English"] or json_content["Output_language"] != ["English"]:
            continue
        if isinstance(json_content["Definition"], list):
            json_content["Definition"] = json_content["Definition"][0] 

        # label balancing, by iterating over labels and randomly select corresponding instance.
        label_to_instances = {}
        for inst in json_content["Instances"]:
            output = inst["output"][0]
            if output not in label_to_instances:
                label_to_instances[output] = []
            label_to_instances[output].append(inst)
        test_instances = [] 
        while len(test_instances) < num_instances_per_task and len(test_instances) < len(json_content["Instances"]):
            for label in label_to_instances:
                if not label_to_instances[label]:
                    continue
                inst = random.choice(label_to_instances[label])
                test_instances.append(inst)
                label_to_instances[label].remove(inst)
                if len(test_instances) == num_instances_per_task:
                    break

        positive_examples = json_content['Positive Examples']
        negative_examples = json_content['Negative Examples']
        instances = test_instances

        # make sure the annotators see all the examples
        random.shuffle(positive_examples)
        random.shuffle(negative_examples)
        random.shuffle(instances)

        positive_examples = positive_examples[:5]
        negative_examples = negative_examples[:3]

        n = 2
        chunks = [instances[i:i + n] for i in range(0, len(instances), n)]
        for i, chunk in enumerate(chunks):
            if i * n > int(num_instances_per_task):
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
    parser.add_argument('--start', type=int, help='id of the start task inside `tasks/`')
    parser.add_argument('--end', type=int, help='id of the end task inside `tasks/`')
    parser.add_argument('--process_default_test_tasks', 
        action='store_true', 
        help='if specified, we will use the tasks in our default test categories (12 categories in total),'
             'and `start` and `end` will be ignored. '
    )
    parser.add_argument('--num_instances_per_task', type=int, help='how many instances per task to use in this evaluation. '
                                             '100 should be enough for reliable estimates.')
    args = parser.parse_args()

    print(" >>>>>>>>> Processing with the following arguments: ")
    print(f" * start task id: {args.start}")
    print(f" * end task id: {args.end}")
    print(f" * process default test tasks: {args.process_default_test_tasks}")
    print(f" * number of instances from each task: {args.num_instances_per_task}")

    if args.process_default_test_tasks:
        process_default_test_tasks(args.num_instances_per_task)
    else:
        process_tasks_from_start_to_end(args.start, args.end, args.num_instances_per_task)
