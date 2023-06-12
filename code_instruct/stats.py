import json
import os

import numpy as np
from code_instruct.data import NaturalInstructionsDataset
from tqdm import tqdm
from transformers import AutoTokenizer


class Stats:
    def __init__(self) -> None:
        self.l = {}

    def add(self, n: int, task: str) -> None:
        if task not in self.l:
            self.l[task] = []
        self.l[task].append(n)

    def finalize(self) -> None:
        for task in self.l:
            self.l[task] = {
                "mean": np.mean(self.l[task]),
                "median": np.median(self.l[task]),
                "max": int(np.max(self.l[task])),
            }
        return self.l


def main() -> None:
    tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom")
    num_shots_list = [0, 2]
    example_type = ["code", "english", "docstring", "code_without_doc"]

    os.makedirs("stats", exist_ok=True)

    for num_shots in num_shots_list:
        dataset = NaturalInstructionsDataset(tokenizer, num_shots, multilingual=False)

        for example_type_ in example_type:
            input_stats = Stats()
            output_stats = Stats()

            for example in tqdm(dataset):
                input, outputs = example.get_example(example_type_)

                input_length = len(tokenizer(input)["input_ids"])
                input_stats.add(input_length, example.task)

                output_length = len(tokenizer(outputs[0])["input_ids"])
                output_stats.add(output_length, example.task)

            input_stats = input_stats.finalize()
            output_stats = output_stats.finalize()

            d = {"input_length": input_stats, "output_length": output_stats}

            json.dump(d, open(os.path.join("stats", f"{example_type_}-{num_shots}.json"), "w"), indent=4)


if __name__ == "__main__":
    main()
