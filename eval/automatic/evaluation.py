from __future__ import print_function
import argparse
import json
import datasets

rouge_metric = datasets.load_metric('rouge')


def rouge(prediction, ground_truth):
    score = rouge_metric.compute(
        predictions=[prediction],
        references=[ground_truth],
        **{'use_aggregator': False, 'use_stemmer': True, 'rouge_types': ['rougeL']}
    )
    return score['rougeL'][0].fmeasure


def metric_max_over_ground_truths(metric_fn, prediction, ground_truths):
    scores_for_ground_truths = []
    for ground_truth in ground_truths:
        score = metric_fn(prediction, ground_truth)
        scores_for_ground_truths.append(score)
    return max(scores_for_ground_truths)


def evaluate(dataset, predictions):
    metrics = {}
    for i in range(len(predictions)):
        pred = predictions[i]['output']
        # gold_input = dataset['Instances'][predictions[i]['index']]['input']
        gold_outputs = dataset['Instances'][predictions[i]['index']]['output']
        if 'rouge' not in metrics:
            metrics['rouge'] = 0
        metrics['rouge'] += metric_max_over_ground_truths(rouge, pred, gold_outputs)

    for key in metrics.keys():
        metrics[key] /= len(predictions)

    return metrics


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--dataset",
                        type=str,
                        required=True,
                        help="Dataset Json File Name")
    parser.add_argument("--predictions",
                        type=str,
                        required=True,
                        help="Prediction File Name")
    args = parser.parse_args()
    with open(args.dataset) as dataset_file:
        dataset_json = json.load(dataset_file)
    with open(args.predictions) as prediction_file:
        predictions_json = json.load(prediction_file)
    print(evaluate(dataset_json, predictions_json['predictions']))


if __name__ == "__main__":
    main()
