def identify_essential_words(question: str) -> str:
    """Given an elementary science question along with a few answer options. List all the words from the question that are essential and sufficient for choosing the correct answer option.

    Parameters:
        question: input question along with four answer options

    Returns:
        str:words from the question that are essential and sufficient for choosing the correct answer option."""

    # list of answer options mentioned in question
    answer_options = extract_answer_options_from_question(question)

    # Get essential and sufficient words from question for choosing the correct answer option.
    salient_words_list = extract_salient_words(question, answer_options)

    # return essential and sufficient words
    return salient_words_list


# program
{
    "method": "identify_essential_words",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "identify_essential_words(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
