from datasets import load_dataset
from promptsource.templates import DatasetTemplates
import json
from collections import defaultdict
import random 
import argparse
import os
from fnmatch import fnmatch

'''
A script to covert “prompt-source” task to our schema/json
-----------------------------------------------------------

Some datasets are not handled automatically by datasets and require users to download the dataset manually (story_cloze for instance ).
To handle those datasets as well, we require users to download the dataset and put it in ~/.cache/promptsource. This is the root directory containing all manually downloaded datasets.
You can override this default path using PROMPTSOURCE_MANUAL_DATASET_DIR environment variable. This should point to the root directory.
'''

# get the dataset and subset that you want to convert, if specified in the command line
parser = argparse.ArgumentParser()
parser.add_argument("--dataset",
                    nargs=1,
                    type=str,
                    required=False,
                    help="The dataset you want to convert")
                    
parser.add_argument("--subset",
                    nargs=1,
                    type=str,
                    required=False,
                    help="The subset you want to convert")
                    
parser.add_argument("--sample",
                    nargs=1,
                    type=int,
                    required=False,
                    help="Number of samples from the dataset")
                    
args = parser.parse_args()
if args.dataset:
    dataset_name = args.dataset[0]

if args.subset:
    subset_name = args.subset[0]

if args.sample:
    sample_num = args.sample[0]
    
def get_dataset(dataset_name):
    dataset = load_dataset(dataset_name, split="train")
    if args.sample:
        cap = min(sample_num, len(dataset))
        dataset = random.choices(dataset, k = cap)
    # Load prompts for this dataset
    dataset_prompts = DatasetTemplates(dataset_name)   
    return dataset, dataset_prompts

def get_subset(dataset_name, subset_name):
    dataset = load_dataset(dataset_name,subset_name, split="train")
    if args.sample:
        cap = min(sample_num, len(dataset))
        dataset = random.choices(dataset, k = cap)
    # Load prompts for this dataset and subset
    dataset_prompts = DatasetTemplates(f"{dataset_name}/{subset_name}")
    return dataset, dataset_prompts
        
def create_task(dataset, dataset_name, dataset_prompts):
    """
    Apply all the prompta on the given dataset and create tasks
    """
    for id in dataset_prompts.templates:
        # Select a prompt by its name
        prompt_name = dataset_prompts.templates[id].name
        prompt = dataset_prompts[prompt_name]
        # Apply the prompt to the dataset
        data = {}
        data["Prompt Name"] = [prompt_name]
        data["Prompt id"] = [id]
        data["Contributors"] = []
        data["Source"] = [dataset_name]
        data["Categories"] = []
        data["Reasoning"] = []
        data["Definition"] = []
        data["Input_language"] = ["English"]
        data["Output_language"] = ["English"]
        data["Instruction_language"] = ["English"]
        data["Domains"] = []
        data["Positive Examples"] = []
        data["Negative Examples"] = []
        data["Instances"] = []
        for i in range(len(dataset)):
            result = prompt.apply(dataset[i])
            if len(result)==2:
                data["Instances"].append({
                    "input": result[0],
                    "output": [result[1]]
                })        
        save_json(data, dataset_name, prompt_name)

        
def save_json(data, dataset_name, prompt_name):
    """
    Shuffle instances, aggregate outputs, and save them in a json file
    """
    random.shuffle(data["Instances"])
    d = defaultdict(list)
    for dic in data["Instances"]:
        parent, children = dic["input"], dic["output"]
        d[parent].extend(children)
        
    result=data
    counter = 0 
    result["Instances"] = [] 
    for k, v in d.items():
        result["Instances"].append({"input": k, "output": v})
    with open(f"tasks/task_{dataset_name}_{prompt_name}.json", 'w' , encoding="utf-8") as outfile:
        json.dump(result, outfile, indent=4,ensure_ascii=False)     

        
if not args.dataset:
    # convert all the datasets
    root = 'promptsource/templates/'
    pattern = "*.yaml"
    for path, subdirs, files in os.walk(root):    
        for name in files:
            if fnmatch(name, pattern):
                data_path = path.removeprefix('promptsource/templates/').split('\\')
                dataset_name = data_path[0]
                if len(data_path)>1:
                    subset_name = data_path[1]
                    dataset, dataset_prompts = get_subset(dataset_name, subset_name)
                else:
                    dataset, dataset_prompts = get_dataset(dataset_name)
                create_task(dataset, dataset_name, dataset_prompts)
else:
    if not args.subset:
        dataset, dataset_prompts = get_dataset(dataset_name)
    if args.subset:
        dataset, dataset_prompts = get_subset(dataset_name, subset_name)
    create_task(dataset, dataset_name, dataset_prompts)