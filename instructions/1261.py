def polish_to_galician(polish_sentence: str) -> str:
    """
    Given a sentence in the Polish language, translate it to Galician language

    Parameters:
        polish_sentence (str): a Polish sentence

    Returns:
        str: Galician translation of the Polish sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(polish_sentence, source_language="Polish", target_language="Galician")


# program
{
    "method": "polish_to_galician",
    "arguments": {
        "polish_sentence": "str",
    },
    "return": "str",
    "execute": "polish_to_galician(polish_sentence)",
}


# preprocessor
def preprocess(input: str):
    polish_sentence = input
    return polish_sentence
