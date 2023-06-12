def question_category_classification(sentence: str, question: str, category: str) -> str:
    """
    Given a sentence and a question around the sentence. A reasoning category is also provided. The task is to indicate if the question belongs to the provided reasoning vategory or not.

    a) Event Duration: understanding of how events last
    b) transient v. stationary: understanding of whether an event will change over time or not
    c) event ordering: understanding of how events are usually ordered in nature
    d) absolute timepoint: understanding of when events usually happen
    e) frequency: how often an event is likely to be repeated

    Parameters:
        sentence (str): sentence
        question (str): question
        category (str): category
    Returns:
        str: `Yes.` or `No.`
    """

    if "Event Duration" in category:
        # this function checks if the question has an understanding of how long the events last
        if does_question_require_event_duration_reasoning(question, category, sentence):
            return "Yes."
        else:
            return "No."
    elif "transient v. stationary" in category:
        # this function checks if the question has an understanding of whether an event will change over time or not
        if does_question_require_event_temporal_reasoning(question, category, sentence):
            return "Yes."
        else:
            return "No."
    elif "event ordering" in category:
        # this function checks if the question has an understanding of how events are ordered in nature
        if does_question_require_event_ordering_reasoning(question, category, sentence):
            return "Yes."
        else:
            return "No."
    elif "absolute timepoint" in category:
        # this function checks if the question has an understanding of when events usually happen
        if does_question_require_event_happen_reasoning(question, category, sentence):
            return "Yes."
        else:
            return "No."
    elif "frequency" in category:
        # this function checks if the question has an understanding of how often an event is likely to be repeated
        if does_question_require_event_frequency_reasoning(question, category, sentence):
            return "Yes."
        else:
            return "No."


# program
{
    "method": "question_category_classification",
    "arguments": {
        "sentence": "str",
        "question": "str",
        "category": "str",
    },
    "return": "str",
    "execute": "question_category_classification(sentence, question, category)",
}


# preprocessor
def preprocess(input: str):
    question = input.split("\nQuestion: ")[-1].split(" \nCategory")[0]
    category = input.split(" \nCategory")[-1]
    sentence = input.split("\nQuestion: ")[0].split("Sentence: ")[-1]
    return sentence, question, category
