'''
Given a task file, it creates a single file for crowd annotations (the input to AMTI).
For example: python 1.amti_create_input_data.py --file  task156_codah_classification_adversarial.json --eval_count 10
'''
import json
import random
import argparse


def read_file(file):
    with open('../../tasks/' + file, 'r') as f:
        return json.load(f)

def normalize(str):
    return str.replace('"', '\'').replace('`', '\'').replace('\n', '<br>')

def process_single_file(file, max_count):
    # grouping instances into groups of size 5
    n = 5
    fout = open(f"f={file}_max_size={max_count}.jsonl", "w")
    json_content = read_file(file)
    positive_examples = json_content['Positive Examples']
    negative_examples = json_content['Negative Examples']
    instances = json_content['Instances']

    # make sure the annotators see all the examples
    random.shuffle(positive_examples)
    random.shuffle(negative_examples)
    random.shuffle(instances)

    positive_examples = positive_examples[:3]
    negative_examples = negative_examples[:3]

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
            map[f'instance_{idx}_output'] = [normalize(x) for x in ex['output'] ]

        fout.write(json.dumps(map) + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A script for preparing natural instructions tasks for human evaluation')
    parser.add_argument('--file', help='name of a file inside `tasks/`')
    parser.add_argument('--eval_count',
                        help='how many instances to use in this evaluation. 100 should be enough for reliable estimates.')
    args = parser.parse_args()

    print(" >>>>>>>>> Processing with the following arguments: ")
    print(f" * file: {args.file}")
    print(f" * count: {args.eval_count}")

    process_single_file(args.file, args.eval_count)
