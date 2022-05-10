import json
import os
import random

"""
This script is used for reordering the instances for our test tasks.
For efficient evaluation, we want to select only 100 instances for the test tasks,
and we also want to make sure the labels are as balanced as possible.
In this script, we select such 100 instances and put them at the beginning of the `Instances` field.
Users of our data should use these 100 instances for testing purposes.
"""

random.seed(123)
tasks_dir = "tasks/"
num_test_instances = 100

test_tasks = [l.strip() for split in ["default", "xlingual"] for l in open(f"splits/{split}/test_tasks.txt")]
for task in test_tasks:
    print(f"reordering the test instances for {task}")
    file = os.path.join(tasks_dir, task + ".json")
    with open(file) as fin:
        task_data = json.load(fin)

    num_of_instances = len(task_data["Instances"])
    label_to_instances = {}
    for inst in task_data["Instances"]:
        output = inst["output"][0]
        if output not in label_to_instances:
            label_to_instances[output] = []
        label_to_instances[output].append(inst)

    test_instances = []
    while len(test_instances) < num_test_instances and len(test_instances) < len(task_data["Instances"]):
        for label in label_to_instances:
            if not label_to_instances[label]:
                continue
            inst = random.choice(label_to_instances[label])
            test_instances.append(inst)
            label_to_instances[label].remove(inst)
            if len(test_instances) == num_test_instances:
                break
    
    remaining_instances = [inst for inst in task_data["Instances"] if inst not in test_instances]

    # Testing instances are put in the first, so that people can get them by cutting the list.
    task_data["Instances"] = test_instances + remaining_instances
    assert len(task_data["Instances"]) == num_of_instances
    
    with open(file, "w") as fout:
        json.dump(task_data, fout, indent=4, ensure_ascii=False)