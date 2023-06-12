def sentence_simplifications(complex_sentence: str) -> list:
    """
    Simplify a sentence so that it's easily understandable by non non-native English speakers. This is achieved by replacing complex words with synonyms, deleting unimportant information. Split long complex sentence into multiple simpler sentences. The meaning of the original sentence should be retained in the simpler sentence/s

    Parameters:
        complex_sentence (str): a complex English sentence

    Returns:
        list: Simple sentence or sentences
    """

    return simplify_sentence(complex_sentence, replace_complex_word=True, delete_unimportant_information=True, split_long_sentences=True)


# program
{
    "method": "sentence_simplifications",
    "arguments": {
        "complex_sentence": "str",
    },
    "return": "list",
    "execute": "sentence_simplifications(complex_sentence)",
}


# preprocessor
def preprocess(input: str):
    complex_sentence = input
    return complex_sentence
