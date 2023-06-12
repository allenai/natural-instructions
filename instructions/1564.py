def generate_answer_to_question(question: str) -> str:
    """Answer the question

    Parameters:
        question: question that needs to be answered

    Returns:
        str: answer to the question
    """
    # Generate a short answer to the question.
    answer = generate_answer(question)
    return answer


# program
{
    "method": "generate_answer_to_question",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "generate_answer_to_question(question)",
}


# preprocessor
def preprocess(input: str):
    question = input.split("Question:")[1].strip()
    return question
