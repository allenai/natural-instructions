def generate_short_answer_to_question(question: str) -> str:
    """Given an open-domain question that can be answered based on factual information, generate a \\*short\\* answer (in a few words only) for the given question.
    Short answer can be one or more entities or it can also be boolean \\*yes\\* or \\*no\\*."

    Parameters:
        question: question that needs to be answered

    Returns:
        str: answer to the question
    """
    # Generate a short answer to the question. Can be a few words, names of one or more entities or a boolean answer (yes/no)
    answer = generate_answer(question, valid_answer_types=["few words", "entities", "yes/no"])
    return answer


# program
{
    "method": "generate_short_answer_to_question",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "generate_short_answer_to_question(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
