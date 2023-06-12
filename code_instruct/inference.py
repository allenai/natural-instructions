import json
import sys
from argparse import ArgumentParser, Namespace
from typing import List

import torch
import transformers
from code_instruct.data import Datapoint, ExampleType, NaturalInstructionsDataset
from code_instruct.model import Model
from tqdm import tqdm


def get_args() -> Namespace:
    parser = ArgumentParser()

    group = parser.add_argument_group("inference")
    group.add_argument("--ds_inference", action="store_true", help="use deepspeed inference")
    group.add_argument("--batch_size", type=int, default=8, help="batch size for inference")
    group.add_argument("--model_name", type=str, help="model name to use")
    group.add_argument("--model_class", type=lambda x: getattr(transformers, x), help="model class to use")
    group.add_argument("--dtype", type=lambda x: getattr(torch, x), help="dtype")
    group.add_argument("--example_type", type=lambda x: ExampleType(x), help="example type")
    group.add_argument("--num_shots", type=int, help="few shots")
    group.add_argument("--max_input_length", type=int, help="max input length")
    group.add_argument("--sample_ids_file", type=str, help="file with sampled ids")
    group.add_argument("--output_file", type=str, help="output file")
    group.add_argument("--start_index", type=int, default=0, help="start index")
    group.add_argument("--end_index", type=int, help="end index")

    args = parser.parse_args()
    return args


def flatten_batch(batch: List[Datapoint], generated_text: List[str], example_type: str, eos_token: str) -> List[dict]:
    for example, text in zip(batch, generated_text):
        input_query, gt_text = example.get_example(example_type, eos_token)

        d = {
            "id": example.id,
            "task": example.task,
            "input_query": input_query,
            "generated_text": text,
            "gt_text": gt_text,
        }

        yield d


def main() -> None:
    args = get_args()

    model = Model(args)
    dataset = NaturalInstructionsDataset(
        "all", args.num_shots, multilingual=False, allowed_list_file=args.sample_ids_file
    )
    progress_bar = tqdm(dataset)

    end_index = len(dataset)
    if args.end_index is not None:
        end_index = min(len(dataset), args.end_index)

    output_file = open(args.output_file, "a")
    output_file_content = open(args.output_file, "r").readlines()

    i = args.start_index
    file_ptr = 0
    batch = []
    input_batch = []

    progress_bar.update(i)

    while i < end_index:
        progress_bar.update()

        example = dataset[i]
        i += 1

        if file_ptr < len(output_file_content) and json.loads(output_file_content[file_ptr])["id"] == example.id:
            file_ptr += 1
            continue

        input, _ = example.get_example(args.example_type, model.tokenizer.eos_token)
        input_ids = model.tokenizer(input, add_special_tokens=False).input_ids

        if args.max_input_length is not None and len(input_ids) > args.max_input_length:
            continue

        batch.append(example)
        input_batch.append(input_ids)

        if len(batch) == args.batch_size or i == end_index:
            gen_output = model.generate(input_batch, do_sample=False, max_new_tokens=100)

            batch = flatten_batch(batch, gen_output, args.example_type, model.tokenizer.eos_token)
            for example in batch:
                output_file.write(json.dumps(example) + "\n")
            sys.stdout.flush()

            batch = []
            input_batch = []


if __name__ == "__main__":
    main()
