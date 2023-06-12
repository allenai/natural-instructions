def find_best_matching_entity(question: str, passage: str, answer_choices: dict) -> str:
    """
    Given a passage, a question, and possible answer choices, select the correct option or entity for the question with the information from the passage. The question contains \"_\" which is the missing entity and need to select the best option from the choices


    Parameters:
        question (str): a given question related to understanding of the events from the passage
        passage (str): a passage
        answer_choices (dict): possible answer

    Returns:
        str: the best candidate answer key that can fill the blank
    """

    answer_options = list(answer_choices.keys())

    # given a question, a reference passage and list of possible options, find the best answer candidate
    answer = find_missing_entity_infer_from_passage(question, passage, answer_options)

    # return the best candidate option
    return answer_choices[answer]


# program
{
    "method": "find_best_matching_entity",
    "arguments": {
        "question": "str",
        "passage": "str",
        "answer_choices": "dict",
    },
    "return": "str",
    "execute": "find_best_matching_entity(question, passage, answer_choices)",
}


# preprocessor
def preprocess(input: str):
    passage = input.split("Questions:")[0]
    question = input.split("Questions:")[-1].split(" (A) ")[0]
    answer_choice_string = "(A) " + input.split(" (A) ")[-1]

    answer_choices = {}
    options = answer_choice_string.split("(")

    for option in options:
        if len(option) > 0:
            answer_key = "(" + option.split(")")[0] + ")"
            answer = option.split(")")[-1].strip()
            answer_choices[answer] = answer_key
    return question, passage, answer_choices
