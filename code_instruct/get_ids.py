from argparse import ArgumentParser, Namespace
from typing import List

from code_instruct.data import Datapoint, ExampleType, CodeInstructionsDataset
from code_instruct.model import load_tokenizer
from tqdm import tqdm


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--output_file", type=str, help="output file")
    args = parser.parse_args()
    return args


def flatten_batch(batch: List[Datapoint], generated_text: List[str], example_type: str) -> List[dict]:
    for example, text in zip(batch, generated_text):
        input_query, gt_text = example.get_example(example_type)

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

    max_input_length = 1948

    tokenizers = {}
    for model_name in ["bigscience/bloom-3b", "salesforce/codegen-2b-mono"]:
        tokenizers[model_name] = load_tokenizer(model_name)

    dataset = CodeInstructionsDataset("all", 2, multilingual=False)
    file = open(args.output_file, "w")

    for i in tqdm(range(len(dataset))):
        example = dataset[i]
        fits_context_length = True

        for example_type in ExampleType:
            for model_name in tokenizers:
                input, _ = example.get_example(example_type, tokenizers[model_name].eos_token)
                input_ids = tokenizers[model_name](input).input_ids

                if len(input_ids) > max_input_length:
                    fits_context_length = False
                    break

            if not fits_context_length:
                break

        if fits_context_length:
            file.write(f"{example.id}\n")


if __name__ == "__main__":
    main()
