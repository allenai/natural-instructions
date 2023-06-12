def translate_oriya_to_tamil(oriya_sentence: str) -> str:
    """
    Given a sentence in the Oriya language, translate it to Tamil language

    Parameters:
        oriya_sentence (str): an Oriya sentence

    Returns:
        str: Tamil translation of the Oriya sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(oriya_sentence, source_language="Oriya", target_language="Tamil")


# program
{
    "method": "translate_oriya_to_tamil",
    "arguments": {
        "oriya_sentence": "str",
    },
    "return": "str",
    "execute": "translate_oriya_to_tamil(oriya_sentence)",
}


# preprocessor
def preprocess(input: str):
    oriya_sentence = input
    return oriya_sentence
