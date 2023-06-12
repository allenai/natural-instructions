import random
from argparse import ArgumentParser, Namespace


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("--all_ids_file", type=str, help="file containing all ids")
    parser.add_argument("--sample_ids_file", type=str, help="file containing the sampled ids")
    parser.add_argument("--num_samples", type=int, help="number of samples")
    parser.add_argument("--seed", type=int, default=42, help="seed")
    args = parser.parse_args()
    return args


def main() -> None:
    args = get_args()

    all_ids_file = [i.strip() for i in open(args.all_ids_file, "r").readlines()]

    task_examples = {}
    for id in all_ids_file:
        task = id.split("-")[0]
        if task not in task_examples:
            task_examples[task] = []
        task_examples[task].append(id)

    output_file = open(args.sample_ids_file, "w")

    for task in task_examples:
        if len(task_examples[task]) > args.num_samples:
            random.seed(args.seed)
            task_examples[task] = random.sample(task_examples[task], args.num_samples)

        for id in task_examples[task]:
            output_file.write(f"{id}\n")


if __name__ == "__main__":
    main()
