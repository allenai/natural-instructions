def find_primary_subject(sentence: str) -> str:
    """
    Given a sentence in the English language, find the primary subject in the sentence

    Parameters:
        sentence (str): an English sentence

    Returns:
        str: primary subject in the sentence
    """

    # this function extracts the primary subject in the given sentence
    return extract_primary_subject(sentence)


# program
{
    "method": "find_primary_subject",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "find_primary_subject(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
