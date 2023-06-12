def get_name_referred_by_pronoun(text: str) -> str:
    """
    Returns the name referred to by the pronoun marked with 2 _'s

    Parameters:
        text (str): input text

    Returns:
        str: the name referred by the pronoun
    """

    # get the position of pronoun marked with underscore
    position = get_pronoun_position_marked_with_underscore(text)
    # get referring name
    name = get_name_for_pronoun_position(text, position)

    return name


# program
{
    "method": "get_name_referred_by_pronoun",
    "arguments": {"text": "str"},
    "return": "str",
    "execute": "get_name_referred_by_pronoun(text)",
}


# preprocessor
def preprocess(input: str):
    text = input
    return text
