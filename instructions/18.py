def question_temporal_reasoning(sentence: str, question: str) -> str:
    """
    Given a sentence and a question around the sentence. The goal is to identify the presence of temporal reasoning in the provided question. Questions that involve temporal reasoning/understanding contain one of the following five temporal phenomena:

    a) Event Duration: understanding of how events last
    b) transient v. stationary: understanding of whether an event will change over time or not
    c) event ordering: understanding of how events are usually ordered in nature
    d) absolute timepoint: understanding of when events usually happen
    e) frequency: how often an event is likely to be repeated

    Indicate with `Yes` if the question involves temporal reasoning. Indicate with `No`, otherwise.

    Parameters:
        sentence (str): sentence
        question (str): question
    Returns:
        str: `Yes` or `No`
    """

    # this function checks if the question has an understanding of how long the events last
    if does_question_require_event_duration_reasoning(question, sentence):
        return "Yes"
    # this function checks if the question has an understanding of whether an event will change over time or not
    elif does_question_require_event_temporal_reasoning(question, sentence):
        return "Yes"
    # this function checks if the question has an understanding of how events are ordered in nature
    elif does_question_require_event_ordering_reasoning(question, sentence):
        return "Yes"
    # this function checks if the question has an understanding of when events usually happen
    elif does_question_require_event_happen_reasoning(question, sentence):
        return "Yes"
    # this function checks if the question has an understanding of how often an event is likely to be repeated
    elif does_question_require_event_frequency_reasoning(question, sentence):
        return "Yes"
    else:
        return "No"


# program
{
    "method": "question_temporal_reasoning",
    "arguments": {
        "sentence": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "question_temporal_reasoning(sentence, question)",
}


# preprocessor
def preprocess(input: str):
    question = input.split("\nQuestion: ")[-1]
    sentence = input.split("\nQuestion: ")[0].split("Sentence: ")[-1]
    return sentence, question
