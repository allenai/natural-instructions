def is_words_flipped(sentence: str) -> str:
    """
    Given a sentence, check if the sentence contains two consecutive words which needs to be flipped to make the sentence grammatical and meaningful. If yes, then return 'Inversion'. If no changes are required return 'Original'

    Parameters:
        sentence (str): a given sentence

    Returns:
        str: \"Inversion"\ or \"Original\"
    """

    # the functions checks if the sentence contains two words which needs to be flipped to make the sentence grammatical and meaningful
    if words_need_to_be_flipped(sentence):
        return "Inversion"
    else:
        return "Original"


# program
{
    "method": "is_words_flipped",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "is_words_flipped(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
