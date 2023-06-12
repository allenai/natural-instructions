def is_context_useful_answering_question(question: str, candidate_context: str, answer: str) -> str:
    """
    Given a question and three passages, 1, 2, and, 3. Find the passage which can ve used to answer the question.


    Parameters:
        question (str): a given question
        candidate_context (str): a candidate context tweet
        answer (str): the answer to the question

    Returns:
        bool: is the candidate context useful in answering the question
    """

    # this function takes in a question, an asnwer, and, a candidate context and returns yes if the context is useful in answering the question and a question as input and returns if the question can be answered by the passage
    if is_answerable(question, answer, candidate_context):
        return "yes"
    else:
        return "no"


# program
{
    "method": "is_context_useful_answering_question",
    "arguments": {
        "question": "str",
        "candidate_context": "str",
        "answer": "str",
    },
    "return": "str",
    "execute": "is_context_useful_answering_question(question, candidate_context, answer)",
}


# preprocessor
def preprocess(input: str):
    candidate_context = input.split("Question: ")[0].split("Context: ")[1]
    question = input.split("Answer: ")[0].split("Question: ")[-1]
    answer = input.split("Answer: ")[-1]
    return question, candidate_context, answer
