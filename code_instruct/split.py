import enum
import json
import os
from typing import List


class Annotators(enum.Enum):
    Mayank = 1
    Danish = 2
    Rudra = 3
    Riyaz = 4
    Marina = 5
    Shiva = 6


def sort_key(x: str) -> int:
    x = x.split("_")[0]
    x = x.split("task")[1]
    return int(x)


def filter(files: List[str]) -> List[str]:
    results = []
    for fname in files:
        if fname.endswith(".json"):
            results.append(fname)
    return results


def main() -> None:
    files = os.listdir("tasks")
    files = filter(files)
    files.sort(key=sort_key)

    splits = {}
    for index, fname in enumerate(files):
        annotator = str(Annotators((index % 6) + 1))
        annotator = annotator.split("Annotators.")[1]

        if annotator not in splits:
            splits[annotator] = []
        splits[annotator].append(fname)

    json.dump(splits, open("splits.json", "w"), indent=4)


if __name__ == "__main__":
    main()
