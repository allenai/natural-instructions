def translate_bengali_to_marathi(bengali_sentence: str) -> str:
    """
    Given a sentence in the Bengali language, translate it to Marathi language

    Parameters:
        bengali_sentence (str): a Bengali sentence

    Returns:
        str: Marathi translation of the Bengali sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(bengali_sentence, source_language="Bengali", target_language="Marathi")


# program
{
    "method": "translate_bengali_to_marathi",
    "arguments": {
        "bengali_sentence": "str",
    },
    "return": "str",
    "execute": "translate_bengali_to_marathi(bengali_sentence)",
}


# preprocessor
def preprocess(input: str):
    bengali_sentence = input
    return bengali_sentence
