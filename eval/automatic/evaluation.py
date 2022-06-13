import string
import json
import argparse
from rouge import rouge_scorer
from transformers import AutoTokenizer


class GPTTokenizer:
    gpt_tokenizer = AutoTokenizer.from_pretrained("gpt2", max_length=1e5)

    def tokenize(self, s):
        tokens = self.gpt_tokenizer.tokenize(s)
        # GPT2 uses Byte-level BPE, which will include space as part of the word. 
        # But for the first word of a sentence, there is no space before it. 
        # So, we remove all the added spaces ("Ġ"). 
        tokens = [t.lstrip("Ġ") for t in tokens]
        return tokens

default_rouge_scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
xlingual_tokenizer = GPTTokenizer()
xlingual_rouge_scorer = rouge_scorer.RougeScorer(['rougeL'], tokenizer=xlingual_tokenizer) 

# adapted the flowing from Squad v1.1 evaluation, without removing the articles.
def normalize_answer(s):
    """Lower text and remove punctuation, and extra whitespace."""

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_punc(lower(s)))


def exact_match(prediction, ground_truth, xlingual=False):
    return (normalize_answer(prediction) == normalize_answer(ground_truth))


def rouge(prediction, ground_truth, xlingual=False):
    if xlingual:
        scorer = xlingual_rouge_scorer
    else:
        scorer = default_rouge_scorer
    scores = scorer.score(prediction=prediction, target=ground_truth)
    return scores["rougeL"].fmeasure


def metric_max_over_ground_truths(metric_fn, prediction, ground_truths, xlingual=False):
    scores_for_ground_truths = []
    for ground_truth in ground_truths:
        score = metric_fn(prediction, ground_truth, xlingual=xlingual)
        scores_for_ground_truths.append(score)
    return max(scores_for_ground_truths)


def compute_metrics(predictions, references, xlingual=False):
    assert len(predictions) == len(references), f"# of predictions {len(predictions)} doesn't match # of references {len(references)}."
    em, rougeL = 0, 0
    for pred, gold in zip(predictions, references):
        assert isinstance(gold, list)
        em += metric_max_over_ground_truths(
            exact_match, prediction=pred, ground_truths=gold, xlingual=xlingual
        )
        rougeL += metric_max_over_ground_truths(
            rouge, prediction=pred, ground_truths=gold, xlingual=xlingual
        )
    em = 100.0 * em / len(references)
    rougeL = 100.0 * rougeL / len(references)
    metrics = {"exact_match": em, "rougeL": rougeL}
    metrics = {k: round(v, 4) for k, v in metrics.items()}
    return metrics


def compute_grouped_metrics(predictions, references, groups, xlingual=False):
    assert len(predictions) == len(references) == len(groups)

    examples_by_group = {}
    for pred, gold, group in zip(predictions, references, groups):
        if group not in examples_by_group:
            examples_by_group[group] = []
        examples_by_group[group].append((pred, gold))
    
    results = {}
    for group, group_examples in examples_by_group.items():
        task_predictions, task_references = zip(*group_examples)
        group_metrics = compute_metrics(task_predictions, task_references, xlingual=xlingual)
        for metric, value in group_metrics.items():
            results[f"{metric}_for_{group}"] = value
    return results


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prediction_file", required=True,
        help="Jsonl file with each line corresponding to a prediction. " 
             "Each json object should have an `id` and a `prediction` key.")
    parser.add_argument(
        "--reference_file", required=True,
        help="Jsonl file with each line corresponding to a reference. " 
             "Each json object should have an `id` and a `references` key. "
             "`task_id`, `task_category` and `task_track` are optional, which will be used to "
             "compute the per-task performance, per-category performance and the performance for default (english) / xlingual Tracks.")
    parser.add_argument(
        "--output_file",
        help="Jsonl file to write the results to.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    eval_instances = {}
    with open(args.reference_file) as fin:
        for line in fin:
            instance = json.loads(line)
            # if track is not provided in the refernce file, we use set the track to `default` and use the default tokenizer in rouge-score.
            if "track" not in instance:
                instance["track"] = "default"
            eval_instances[instance["id"]] = instance

    all_predictions = {}
    with open(args.prediction_file) as fin:
        for line in fin:
            prediction = json.loads(line)
            all_predictions[prediction["id"]] = prediction["prediction"]

    all_results = {}
    for track in ["default", "xlingual"]:
        print("Evaluating track:", track)
        instance_ids = [id for id, instance in eval_instances.items() if instance["track"] == track]
        references = [eval_instances[id]["references"] for id in instance_ids]
        predictions = []
        missing_predictions = []
        for id in instance_ids:
            if id in all_predictions:
                predictions.append(all_predictions[id])
            else:
                missing_predictions.append(id)
                predictions.append("")
        if missing_predictions:
            print(f"No prediction for {len(missing_predictions)} instances. Use empty string as prediction.")

        results = compute_metrics(predictions, references, xlingual=(track == "xlingual"))
        print("======== Overall Metrics ========")
        for metric, value in results.items():
            print(f"{metric}: {value}")
            all_results[f"{metric}_{track}_track"] = value

        if "task_category" in eval_instances[instance_ids[0]]:
            categories = ["_".join(eval_instances[id]["task_category"].lower().split()) for id in instance_ids]
            results_per_category = compute_grouped_metrics(predictions, references, categories, xlingual=(track == "xlingual"))
            print("======== Metrics per Category ========")
            for metric, value in results_per_category.items():
                print(f"{metric}: {value}")
                all_results[f"{metric}_{track}_track"] = value

        if "task_id" in eval_instances[instance_ids[0]]:
            tasks = [eval_instances[id]["task_id"] for id in instance_ids]
            results_per_task = compute_grouped_metrics(predictions, references, tasks, xlingual=(track == "xlingual"))
            print("======== Metrics per Task ========")
            for metric, value in results_per_task.items():
                print(f"{metric}: {value}")
                all_results[f"{metric}_{track}_track"] = value

    if args.output_file:
        with open(args.output_file, "w") as fout:
            json.dump(all_results, fout, indent=2)
            