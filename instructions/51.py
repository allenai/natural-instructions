def answer_the_question(sentence: str, question: str) -> str:
    """
    Given a sentence and a question surrounding the sentence, the task is to answer the question. Use only the information provided in the sentence to answer the question.

    Parameters:
        sentence (str): An English sentence
        question (str): Question surrounding the sentence

    Returns:
        str: Answer
    """

    # this function generates the answer given the question and a sentence
    return generate_answer(sentence, question)


# program
{
    "method": "answer_the_question",
    "arguments": {
        "sentence": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "answer_the_question(sentence, question)",
}


# preprocessor
def preprocess(input: str):
    sentence = input.rpartition("Question: ")[0].partition("Sentence: ")[-1]
    question = input.rpartition("Question: ")[2]
    return sentence, question
