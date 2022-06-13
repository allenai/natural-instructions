import json
import os

"""
This script is used for creating the reference file that can be used for our leaderboard evaluation.
The reference file is in a jsonl format, and each line correspons to one evaluation instance. 
Each line should have the `id` and `references` fileds, with `task_id`, `task_category` and `track` fields as optional.
In `src/reorder_instances_for_testing.py`, we already selected 100 instances for each test task 
and put them at the beginning of the `Instances` field. 
Here we will use these 100 instances for all the evaluation tasks and put them in this single reference file.
"""

tasks_dir = "tasks/"
num_test_instances = 100

with open("test_references.jsonl", "w") as fout:
    for track in ["default", "xlingual"]:
        test_tasks = [l.strip() for l in open(f"splits/{track}/test_tasks.txt")]
        for task in test_tasks:
            file = os.path.join(tasks_dir, task + ".json")
            with open(file) as fin:
                task_data = json.load(fin)
            test_instances = task_data["Instances"][:num_test_instances]
            for instance in test_instances:
                fout.write(json.dumps({
                    "id": instance["id"], 
                    "references": instance["output"], 
                    "task_id": task, 
                    "task_category": task_data["Categories"][0], 
                    "track": track},
                ) + "\n")