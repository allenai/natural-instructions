# Evaluation Setup of Natural Instruction V2

To facilitate research on cross-task generalization, we split out tasks into two subsets: one for training and one for testing. Users can use the training tasks for any modeling purpose, while the testing tasks should be used to evaluate the model's ability to solve new tasks by following instruction.

## English Track

The [`default`](default) folder contains our splits for the English-only tasks (i.e., both task input and task output are in English). Each line in the `.txt` file corresponds one task in our [task folder](../tasks/).

The `train_tasks.txt` should be used for your modeling, from which you can also set apart some tasks for validation if needed.

The `test_tasks.txt` contains the tasks for evaluation. We manually selected 12 categories of tasks for evaluation. They cover diverse varieties, such as those at word, sentence, and document levels, in both classiﬁcation and generation format. **Note:** You are supposed to use them only for reporting the performance. When you get the predictions, you are welcome to submit your predictions to our leaderboard (We will release the submission instructions soon)!

The `excluded_tasks.txt` contains all the tasks that are excluded from both training and testing (e.g., non-English tasks for the default track). Specifically, we exclude tasks that are sourced from the same dataset as any testing task, in order to avoid potential data leakage.

## Cross-lingual Track

A more ambitious goal for general-purpose model is to follow instructions to do new tasks even in other languages. To facilitate this goal, we introduce another cross-lingual split, with only non-English tasks in the `test_tasks.txt`.

## Testing Instances

Since we have 119 / 35 test tasks for the English / xlingual tracks respectively and each task might have at most 6.5K instances, evaluation on all these instances will become very slow and unnecessary.

For an efﬁcient evaluation, we selected 100 instances from each task to do the testing. These instances are also selected with label balancing (valid mainly for classification tasks). You can find this subset of testing instances in each test task's json files, indicated by ``"Instances Subset for Testing"``, while the `"Instances"` field is a superset. We will only evaluate model's performance on these testing instances.
