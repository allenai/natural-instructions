def generate_question(passage: str) -> str:
    """Generates questions given the passage. Generated questions involve some kind of complex reasoning (including numerical reasoning). Generated questions must require looking at more than one part of the passage to answer. Generated Questions require a variety of reasoning types and also have a variety of answer types (spans, numbers, dates). Questions should require AT LEAST 2 arithmetic operations
    Parameters:
        passage: Passaged based on which a question has to be generated
    Returns:
        str:question that requires complex reasoning
    """

    question_types = ["span", "number", "date"]

    # given the passage, identify the 'type' of the question to be asked.
    question_type = identify_apporiate_question_type(passage, question_types)

    # create question that requires AT LEAST 2 arithmetic operations based on the passage and identified question_type
    question = create_complex_question(passage, question_type)

    # return the generated question
    return question


# program
{
    "method": "generate_question",
    "arguments": {
        "passage": "str",
    },
    "return": "str",
    "execute": "generate_question(passage)",
}


# preprocessor
def preprocess(input: str):
    passage = input
    return passage
