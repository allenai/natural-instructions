def answer_question(question: str) -> str:
    """
    Answer an open-domain question. The answer should be short and refer to entities. Do not answer in the form of a sentence

    Parameters:
        question (str): a question

    Returns:
        str: answer to the question
    """

    # this function answers the given question
    return answer_given_question(
        question,
        is_answer_short=True,
        answer_as_a_sentence=False,
    )


# program
{
    "method": "answer_question",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "answer_question(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
