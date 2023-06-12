def generate_yes_no_question(passage: str) -> str:
    """Generate a yes/no question given a passage that is answerable based on the given passage

    Parameters:
        passage: passage from which yes/no question needs to be generated

    Returns:
        str: yes/no question
    """

    # generate yes/no question
    question = generate_question(passage, type="yes/no", answerable_from_passage=True)

    return question


# program
{
    "method": "generate_yes_no_question",
    "arguments": {
        "passage": "str",
    },
    "return": "str",
    "execute": "generate_yes_no_question(passage)",
}


# preprocessor
def preprocess(input: str):
    passage = input
    return passage
