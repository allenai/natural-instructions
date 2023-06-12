def answer_question_given_passage(passage: str, question: str, option_1: str, option_2: str) -> str:
    """
    Given a passage and a question centered around the passage. Additionally, two options are also provided. Select the option which correctly answers the question.

    Parameters:
        passage (str): Passage
        question (str): Question
        option_1 (str): First option for answer
        option_2 (str): Second option for answer

    Returns:
        str: returns the correct option text
    """

    # this function return True if the option correctly answer the question from the passage
    if answers_given_question_passage(passage, question, option_1):
        return option_1
    else:
        return option_2


# program
{
    "method": "answer_question_given_passage",
    "arguments": {
        "passage": "str",
        "question": "str",
        "option_1": "str",
        "option_2": "str",
    },
    "return": "str",
    "execute": "answer_question_given_passage(passage, question, option_1, option_2)",
}


# preprocessor
def preprocess(input: str):
    passage = input.split("Question: ")[0].split("Passage: ")[-1].strip()
    question = input.split("Option1: ")[0].split("Question: ")[-1].strip()

    option_1 = input.split("Option2: ")[0].split("Option1: ")
    option_2 = input.split("Option2: ")[-1]

    return passage, question, option_1, option_2
