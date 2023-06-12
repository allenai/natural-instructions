def generate_answer_given_passage(passage: str, question: str) -> str:
    """
    Given a passage and an a question, the task is to generate the correct answer to the question

    Parameters:
        passage (str): An English passage
        question (str): Question from the passage

    Returns:
        str: the correct answer
    """

    # this function returns the answer for a question given the passage
    return get_answer_from_passage(passage, question)


# program
{
    "method": "generate_answer_given_passage",
    "arguments": {
        "passage": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "generate_answer_given_passage(passage, question)",
}


# preprocessor
def preprocess(input: str):
    passage = input.rpartition("Question: ")[0].partition("Passage: ")[-1]
    question = input.rpartition("Question: ")[2]
    return passage, question
