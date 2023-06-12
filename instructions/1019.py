def translate_oriya_to_telugu(oriya_sentence: str) -> str:
    """
    Given a sentence in the Oriya language, translate it to Telugu language

    Parameters:
        oriya_sentence (str): an Oriya sentence

    Returns:
        str: Telugu translation of the Oriya sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(oriya_sentence, source_language="Oriya", target_language="Telugu")


# program
{
    "method": "translate_oriya_to_telugu",
    "arguments": {
        "oriya_sentence": "str",
    },
    "return": "str",
    "execute": "translate_oriya_to_telugu(oriya_sentence)",
}


# preprocessor
def preprocess(input: str):
    oriya_sentence = input
    return oriya_sentence
