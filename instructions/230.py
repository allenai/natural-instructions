def find_passage_containing_answer_given_question(question: str, passage_1: str, passage_2: str, passage_3: str) -> int:
    """
    Given a question and three passages, 1, 2, and, 3. Find the passage which can  e used to answer the question.


    Parameters:
        question (str): a given question
        passage_1 (str): the first passage
        passage_2 (str): the second passage
        passage_3 (str): the third passage

    Returns:
        int: which passage likely helps in answering the given question
    """

    # this function takes in a passage and a question as input and returns if the question can be answered by the passage
    if is_answerable(question, passage_1):
        return 1
    elif is_answerable(question, passage_2):
        return 2
    elif is_answerable(question, passage_3):
        return 3


# program
{
    "method": "find_passage_containing_answer_given_question",
    "arguments": {
        "question": "str",
        "passage_1": "str",
        "passage_2": "str",
        "passage_3": "str",
    },
    "return": "int",
    "execute": "find_passage_containing_answer_given_question(question, passage_1, passage_2, passage_3)",
}


# preprocessor
def preprocess(input: str):
    question = input.split("Passage 1:")[0].split("Question: ")[1]
    passage_1 = input.split("Passage 2:")[0].split("Passage 1:")[-1]
    passage_2 = input.split("Passage 3:")[0].split("Passage 2:")[-1]
    passage_3 = input.split("Passage 3:")[-1]
    return question, passage_1, passage_2, passage_3
