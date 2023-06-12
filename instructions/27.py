def classify_answer_type(passage: str, question: str) -> str:
    """
    Given a passage and a question surrouding the passage, check if the answer for the question is present in the passage. If yes, then the output will be \"span\". If the answer is a number, then the output will be \"number\". If the answer is a date, then the output will be \"date\".

    Parameters:
        passage (str): An English passage
        question (str): Question surrounding the passage

    Returns:
        str: Answer Type
    """

    # this function will answer the question taking cues from the passage
    answer = answer_given_passage(passage, question)

    if answer in passage:
        return "span"
    # this function checks if the given text is a date or not
    if is_date(answer):
        return "date"
    # this function checks if the given text is a number or not
    if is_number(answer):
        return "number"


# program
{
    "method": "classify_answer_type",
    "arguments": {
        "passage": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "classify_answer_type(passage, question)",
}


# preprocessor
def preprocess(input: str):
    passage = input.rpartition("Question: ")[0].partition("Passage: ")[-1]
    question = input.rpartition("Question: ")[2]
    return passage, question
