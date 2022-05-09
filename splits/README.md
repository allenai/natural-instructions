# Evaluation Setup of Natural Instruction V2

Here we describe the evaluation setup used in [our paper](https://arxiv.org/abs/2204.07705) which can be used for reproducing our experiments or extending them. The target setup of the study is a cross-task generalization, i.e., training on a subset of tasks and evaluating on the remaining unseen ones. To do so, we split out tasks into two subsets: one for training and one for testing. Users can use the training tasks for any modeling purpose, while the testing tasks should be used to evaluate and compare different models.

Moreover, because of the multilingual nature of Natural Instruction V2, we are able to evaluate the model’s generalization to unseen tasks not only in English but also in other languages. Therefore, we create two evaluation tracks: one for cross-task generalization within English, and the other for cross-lingual cross-task generalization.

## English Track

The [`default`](default) folder contains our splits for the English-only tasks (i.e., both task input and task output are in English). Each line in the `.txt` file corresponds one task in our [task folder](../tasks/).

The `train_tasks.txt` should be used for your modeling, from which you can also set apart some tasks for validation if needed.

The `test_tasks.txt` contains the tasks for evaluation. We manually selected 12 categories of tasks for evaluation. They cover diverse varieties, such as those at word, sentence, and document levels, in both classiﬁcation and generation format. **Note:** You are supposed to use them only for reporting the performance. When you get the predictions, you are welcome to submit your predictions to our leaderboard (We will release the submission instructions soon)!

The `excluded_tasks.txt` contains all the tasks that are excluded from both training and testing (e.g., non-English tasks for the default track). Specifically, we exclude tasks that are sourced from the same dataset as any testing task, in order to avoid potential data leakage.

## Cross-lingual Track

The cross-lingual track is mainly used for testing whether a model can even follow instructions to do a new task in other languages (i.e., cross-lingual cross-task generalization). To facilitate this goal, we include only non-English tasks in the `test_tasks.txt`, which also belongs to the 12 evaluation categories. Some non-English tasks in other categories (e.g., translation) are added to the `train_tasks.txt`.

## Testing Instances

Since we have 119 / 35 test tasks for the English / xlingual tracks respectively and each task might have at most 6.5K instances, evaluation on all these instances will become very slow and unnecessary.

For an efﬁcient evaluation, we selected 100 instances from each task to do the testing. These instances are also selected with label balancing if possible (valid mainly for classification tasks). See [`src/reorder_instances_for_testing.py`](src/reorder_instances_for_testing.py) for details. For reproducibility, these 100 instances are put at the begining of the `Instances` field. We will only evaluate model's performance on these testing instances. You can get them by slicing the `Instances` list:

```python
test_instances = task_json["Instances"][:100]
```
