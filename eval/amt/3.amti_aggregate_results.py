import json

def get_stats(values):
    maj_vote_value = max(set(values), key=values.count)
    avg_score = sum(values) / len(values)
    model_values_str = "\t".join([str(x) for x in values])
    return maj_vote_value, avg_score, model_values_str


def normalize(str):
    return str.replace("\t", " ").replace("\n", "<newline>").replace("\r", "<newline>")

def discretize(x):
    if x == 0.5:
        return 0.5
    if x > 0.5:
        return 1.0
    else:
        return 0.0


def aggregate_v2(response_file):
    worker_stats = {}
    with open(response_file) as f:
        for line in f.readlines():
            json_line = json.loads(line)

            worker_id = json_line[f'WorkerId']
            if worker_id not in worker_stats:
                worker_stats[worker_id] = 0
            worker_stats[worker_id] += 1

            file = json_line[f'file']
            instructions = normalize(json_line[f'instructions'])

            instruction_quality_value = float(json_line[f'instruction_quality_q1'])
            instruction_suggestions = normalize(json_line[f'instruction_quality_q2'])

            positive_ex_quality_value = float(json_line[f'positive_example_quality_q1'])
            positive_ex_suggestions = normalize(json_line[f'positive_example_quality_q2'])

            negative_ex_quality_value = float(json_line[f'negative_example_quality_q1'])
            negative_ex_suggestions = normalize(json_line[f'negative_example_quality_q2'])

            positive_examples = []
            for idx in range(0, 3):
                id = f'positive_ex_{idx}_input'
                if id in json_line:
                    positive_examples.append(json_line[id])
            positive_examples_appended = normalize("//".join(positive_examples))

            negative_examples = []
            for idx in range(0, 3):
                id = f'negative_ex_{idx}_input'
                if id in json_line:
                    negative_examples.append(json_line[id])
            negative_examples_appended = normalize("//".join(negative_examples))

            prefix = f"{instruction_quality_value}\t{instruction_suggestions}\t{file}\t{instructions}" \
                     f"\t{positive_ex_quality_value}\t{positive_ex_suggestions}\t{positive_examples_appended}" \
                     f"\t{negative_ex_quality_value}\t{negative_ex_suggestions}\t{negative_examples_appended}"

            instance_input = []
            instance_output = []
            instance_prediction = []
            for idx in range(0, 5):
                id = f'instance_{idx}_input'
                if id in json_line:
                    input = normalize(json_line[id])
                    output = normalize(json_line[f'instance_{idx}_output'])
                    human_output = normalize(json_line[f'annotated_instance_{idx}_output'])
                    instance_input.append(input)
                    instance_output.append(output)
                    instance_prediction.append(human_output)
                    print(f"{prefix}\t{input}\t{output}\t{human_output}")


    # print(f" * worker_stats: {worker_stats}")
    # print(plausiblity_labels_per_questions)
    # print(grammaticality_labels_per_questions)
    #
    #
    # for id, values in plausiblity_labels_per_questions.items():
    #     if len(values) == 0:
    #         continue
    #     values_gr = grammaticality_labels_per_questions[id]
    #
    #     maj_vote_value, avg_score, model_values_str = get_stats(values)
    #     maj_vote_value_gr, avg_score_gr, model_values_gr_str = get_stats(values_gr)
    #
    #     worker_ids = "_".join(workers_per_questions[id])
    #
    #
    #     if pairwise and id in s1_answers and id in s2_answers:
    #             print(f"{id} \t {s1_answers[id]} \t {s2_answers[id]} \t {worker_ids} \t {maj_vote_value} \t {avg_score} \t {maj_vote_value_gr} \t {avg_score_gr}")
    #     elif not pairwise and id in s1_answers:
    #             print(f"{id} \t {s1_answers[id]} \t {worker_ids} \t {maj_vote_value} \t {avg_score} \t {maj_vote_value_gr} \t {avg_score_gr}")

    from nltk import agreement
    # for type in num_invalid_questions_per_type.keys():
    #     my_agreement = {}
    #     taskdata = []
    #     print(f" ======= {type} ======== ")
    #     for id, values in labels_per_questions.items():
    #         if len(values) == 5 and type_merging[all_questions[id]['answer_type']] == type:
    #
    #             # l_model = len(set(values))
    #             l_model = max([values.count(x) for x in values])
    #             if l_model not in my_agreement:
    #                 my_agreement[l_model] = 0
    #             my_agreement[l_model] += 1
    #
    #             taskdata.append(['a1', id, str(discretize(values[0]))])
    #             taskdata.append(['a2', id, str(discretize(values[1]))])
    #             taskdata.append(['a3', id, str(discretize(values[2]))])
    #             taskdata.append(['a4', id, str(discretize(values[3]))])
    #             taskdata.append(['a5', id, str(discretize(values[4]))])
    #
    #     if len(taskdata) > 0:
    #         ratingtask = agreement.AnnotationTask(data=taskdata)
    #         print("fleiss " + str(ratingtask.multi_kappa()))
    #         print(my_agreement)
    #         total = sum(my_agreement.values())
    #         print({(k, 100.0 * v / total) for k, v in my_agreement.items()})

aggregate_v2("batch-43ecd7ef-0717-4b72-a39c-b6179f8b5f77_task156_pilot/batch-results.jsonl")
