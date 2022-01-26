import sys

# sys.path.append("..")
sys.path.append("../automatic")

import json
from evaluation import metric_max_over_ground_truths, rouge


def get_stats(values):
    maj_vote_value = max(set(values), key=values.count)
    avg_score = sum(values) / len(values)
    model_values_str = "\t".join([str(x) for x in values])
    return maj_vote_value, avg_score, model_values_str


def normalize(str):
    return str.replace("\t", " ").replace("\n", "<newline>").replace("\r", "<newline>")


def normalize2(str):
    return ' '.join(str.replace(",", "").lower().split())


def discretize(x):
    if x == 0.5:
        return 0.5
    if x > 0.5:
        return 1.0
    else:
        return 0.0


def aggregate_v2(response_file):
    worker_stats = {}
    suggestions =  {}
    with open(response_file) as f:
        for line in f.readlines():
            json_line = json.loads(line)

            worker_id = json_line[f'WorkerId']
            if worker_id not in worker_stats:
                worker_stats[worker_id] = 0
            worker_stats[worker_id] += 1

            file = json_line[f'file']
            instructions = normalize(json_line[f'instructions'])

            instruction_quality_value = float(json_line[f'instruction_quality_q1'])
            instruction_suggestions = normalize(json_line[f'instruction_quality_q2'])

            positive_ex_quality_value = float(json_line[f'positive_example_quality_q1'])
            positive_ex_suggestions = normalize(json_line[f'positive_example_quality_q2'])

            negative_ex_quality_value = float(json_line[f'negative_example_quality_q1'])
            negative_ex_suggestions = normalize(json_line[f'negative_example_quality_q2'])

            positive_examples = []
            for idx in range(0, 5):
                id = f'positive_ex_{idx}_input'
                if id in json_line:
                    positive_examples.append(json_line[id])
            positive_examples_appended = normalize("//".join(positive_examples))

            negative_examples = []
            for idx in range(0, 3):
                id = f'negative_ex_{idx}_input'
                if id in json_line:
                    negative_examples.append(json_line[id])
            negative_examples_appended = normalize("//".join(negative_examples))

            instruction_suggestions = instruction_suggestions.replace("\n", " ")
            positive_ex_suggestions = positive_ex_suggestions.replace("\n", " ")
            negative_ex_suggestions = negative_ex_suggestions.replace("\n", " ")

            prefix = f"{instruction_quality_value}\t{instruction_suggestions}\t{file}\t{instructions}" \
                     f"\t{positive_ex_quality_value}\t{positive_ex_suggestions}\t{positive_examples_appended}" \
                     f"\t{negative_ex_quality_value}\t{negative_ex_suggestions}\t{negative_examples_appended}"

            if len(instruction_suggestions) + len(positive_ex_suggestions) + len(negative_ex_suggestions) > 2:
                if file not in suggestions:
                    suggestions[file] = []
                if len(instruction_suggestions.strip()) > 2:
                    suggestions[file].append(f"    - regarding instructions: `{instruction_suggestions}`")
                if len(positive_ex_suggestions.strip()) > 2:
                    suggestions[file].append(f"    - regarding p examples: `{positive_ex_suggestions}`")
                if len(negative_ex_suggestions.strip()) > 2:
                    suggestions[file].append(f"    - regarding n examples: `{negative_ex_suggestions}`")
            # instance_input = []
            # instance_output = []
            # instance_prediction = []
            for idx in range(0, 5):
                id = f'instance_{idx}_input'
                if id in json_line:
                    input = normalize(json_line[id])
                    output = normalize(json_line[f'instance_{idx}_output'])
                    human_output = normalize(json_line[f'annotated_instance_{idx}_output'])
                    # instance_input.append(input)
                    # instance_output.append(output)
                    # instance_prediction.append(human_output)
                    rouge_val = metric_max_over_ground_truths(
                        rouge, normalize2(human_output),
                        [normalize2(x) for x in output.split("///")]
                    )
                    print(f"{prefix}\t{input}\t{output}\t{human_output}\t{rouge_val}\t{worker_id}")

    for file in sorted(suggestions.keys()):
        print(f" - [ ] {file}")
        for feedback in suggestions[file]:
            print(feedback)



# aggregate_v2("batch-43ecd7ef-0717-4b72-a39c-b6179f8b5f77_task156_pilot/batch-results.jsonl")
# aggregate_v2("batch-65c49abc-f8a3-4f12-a71d-9ce5742c3419_start=60_end=100_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-eea0ef32-da0a-47cf-bcae-810d1a503379_start=1_end=59_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-cdcb497e-49a3-4cee-8ab5-1451dc19dac2_119_end=200_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-58086c69-62bf-4e91-8741-b68d27e1fd63-start=201_end=300_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-fc02d066-1e35-4184-b4ea-ba7eca1abcc1_start=301_end=400_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-4739062e-2141-4f97-9a37-41197abf9a93_start=400_end=600_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-23353cc5-13c1-4af9-94c3-03eb2bacbd0a_start=600_end=850_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-4ee23f3d-2900-4fef-a0ae-d05bc7d519e8_start=850_end=1200_max_size=5/batch-results.jsonl")
# aggregate_v2("batch-13abedb3-9788-4118-8a23-89978a941638_start=1200_end=1536_max_size=5/batch-results.jsonl")
aggregate_v2("batch-eb1b61cd-36e7-4fdf-b8e1-fedd3c77245f_start=1540_end=1726_max_size=5/batch-results.jsonl")
