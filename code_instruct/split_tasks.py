import argparse
import copy
import glob
import json
import os
import random


"""
Script for splitting tasks into the train/test set for standard evaluation setup.
More info for the evaluation setup can be found in `./splits/README.md`.
You can run this with the following commands to generate the files for English track or cross-lingual track respectively:
>>> python src/split_tasks.py --track default --output splits/default
>>> python src/split_tasks.py --track xlingual --output splits/xlingual
"""


def sort(l: set) -> list:
    l1 = list(l)
    l1.sort(key=lambda x: int(x.split("_")[0].split("task")[1]))
    return l1


def dump(tasks_by_category, tasks_by_source, task_languages, train_tasks, test_tasks):
    tasks_by_category = copy.deepcopy(tasks_by_category)
    tasks_by_source = copy.deepcopy(tasks_by_source)

    for i in tasks_by_category:
        en_tasks = []
        for task in tasks_by_category[i]:
            if task_languages[task] == "en":
                en_tasks.append(task)
        en_tasks.sort()
        tasks_by_category[i] = en_tasks

    for i in tasks_by_source:
        en_tasks = []
        for task in tasks_by_source[i]:
            if task_languages[task] == "en":
                en_tasks.append(task)
        en_tasks.sort()
        tasks_by_source[i] = en_tasks

    json.dump(tasks_by_category, open("tasks_by_category.json", "w"), indent=4)
    json.dump(tasks_by_source, open("tasks_by_source.json", "w"), indent=4)

# from original repo
# test_categories = [
#     "Textual Entailment",
#     "Cause Effect Classification",
#     "Coreference Resolution",
#     "Dialogue Act Recognition",
#     "Answerability Classification",
#     "Overlap Extraction",
#     "Word Analogy",
#     "Keyword Tagging",
#     "Question Rewriting",
#     "Title Generation",
#     "Data to Text",
#     "Grammar Error Correction",
# ]

# for our dataset
test_categories = [
    "Information Extraction",
    "Toxic Language Detection",
    "Grammar Error Correction",
    "Word Semantics",
    "Dialogue Generation",
    "Section Classification",
    "Question Decomposition",
    "Misc.",
    "Pos Tagging",
    "Program Execution",
    "Grammar Error Detection",
    "Linguistic Probing",
    "Sentence Ordering",
    "Dialogue State Tracking",
    "Text Completion",
    "Overlap Extraction",
    "Summarization",
    "Commonsense Classification",
    "Title Generation",
]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--task_dir",
        type=str,
        default="tasks/",
        help="the directory path of all the task json files in NaturalInstructions.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="splits/default/",
        help="the directory path for saving the splits text files.",
    )
    parser.add_argument(
        "--test_categories",
        nargs="*",
        default=test_categories,
        help="The predefined test categories. Only valid for the cross_category setting.",
    )
    parser.add_argument(
        "--track",
        choices=["default", "xlingual"],
        default="default",
        help="`default` will generate the splits for the English-only track, `xlingual` will generate the splits for the cross-lingual track.",
    )
    parser.add_argument(
        "--no_synthetic",
        action="store_true",
        help="don't include tasks from synthetic source.",
    )
    parser.add_argument(
        "--dump_all",
        action="store_true",
        help="write all tasks to file",
    )
    parser.add_argument("--seed", type=int, default=1, help="random seed")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    random.seed(args.seed)

    tasks = set()
    task_categories = {}
    task_languages = {}
    task_sources = {}

    annotated_tasks = os.listdir("instructions")

    for file in glob.glob(os.path.join(args.task_dir, "task*.json")):
        if (
            not args.dump_all
            and str(int(os.path.basename(file).split("_")[0].split("task")[1])) + ".py" not in annotated_tasks
        ):
            continue

        task = os.path.basename(file)[:-5]
        task_info = json.load(open(file, encoding="utf-8"))

        if args.no_synthetic:
            source = task_info["Source"]
            if "synthetic" in source:
                continue

        languages = set(task_info["Input_language"] + task_info["Output_language"] + task_info["Instruction_language"])
        if not (len(languages) == 1 and languages.pop().lower() == "english"):
            task_languages[task] = "non-en"
        else:
            task_languages[task] = "en"

        task_categories[task] = task_info["Categories"]
        task_sources[task] = task_info["Source"]
        tasks.add(task)

    tasks_by_category = {}
    for task, categories in task_categories.items():
        for category in categories:
            if category not in tasks_by_category:
                tasks_by_category[category] = []
            tasks_by_category[category].append(task)

    tasks_by_source = {}
    for task, sources in task_sources.items():
        for source in sources:
            if source not in tasks_by_source:
                tasks_by_source[source] = []
            tasks_by_source[source].append(task)

    test_categories = set(args.test_categories)
    print(f"Test categories include: {test_categories}")

    train_tasks, test_tasks, excluded_tasks = set(), set(), set()

    for category in test_categories:
        if category in tasks_by_category:
            for task in tasks_by_category[category]:
                test_tasks.add(task)

    # exclude tasks that have same source as test tasks from the remaining data.
    excluded_tasks = set()
    for test_task in test_tasks:
        for source in task_sources[test_task]:
            for task in tasks_by_source[source]:
                if task in test_tasks:
                    continue
                else:
                    excluded_tasks.add(task)

    # select tasks based on the track, and the other test tasks are excluded from training
    for test_task in test_tasks:
        if args.track == "default" and task_languages[test_task] == "en":
            continue
        elif args.track == "xlingual" and task_languages[test_task] == "non-en":
            continue
        else:
            excluded_tasks.add(test_task)

    # moreover, for the default track, we should exclude all the non-en tasks
    if args.track == "default":
        for task in tasks:
            if task_languages[task] == "non-en":
                excluded_tasks.add(task)

    # this task data is not good, need to fix. we remove it from our evaluation temporarily.
    if "task1415_youtube_caption_corrections_grammar_correction" in test_tasks:
        excluded_tasks.add("task1415_youtube_caption_corrections_grammar_correction")

    # make sure the exlucded tasks are not in the test_tasks
    test_tasks = set([t for t in test_tasks if t not in excluded_tasks])

    train_tasks = tasks - excluded_tasks - test_tasks

    dump(tasks_by_category, tasks_by_source, task_languages, train_tasks, test_tasks)

    train_tasks = sort(train_tasks)
    test_tasks = sort(test_tasks)
    excluded_tasks = sort(excluded_tasks)

    os.makedirs(args.output_dir, exist_ok=True)
    with open(os.path.join(args.output_dir, "train_tasks.txt"), "w") as fout:
        for task in train_tasks:
            fout.write(task + "\n")
    with open(os.path.join(args.output_dir, "test_tasks.txt"), "w") as fout:
        for task in test_tasks:
            fout.write(task + "\n")
    with open(os.path.join(args.output_dir, "excluded_tasks.txt"), "w") as fout:
        for task in excluded_tasks:
            if task_languages[task] == "en":
                fout.write(task + "\n")
