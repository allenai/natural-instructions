def arabic_to_japanese(arabic_sentence: str) -> str:
    """
    Given a sentence in the Arabic language, translate it to Japanese language

    Parameters:
        arabic_sentence (str): an Arabic sentence

    Returns:
        str: Japanese translation of the Arabic sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(arabic_sentence, source_language="Arabic", target_language="Japanese")


# program
{
    "method": "arabic_to_japanese",
    "arguments": {
        "arabic_sentence": "str",
    },
    "return": "str",
    "execute": "arabic_to_japanese(arabic_sentence)",
}


# preprocessor
def preprocess(input: str):
    arabic_sentence = input
    return arabic_sentence
