def hebrew_to_arabic(hebrew_sentence: str) -> str:
    """
    Given a sentence in the Hebrew language, translate it to Arabic language

    Parameters:
        hebrew_sentence (str): a hebrew sentence

    Returns:
        str: Arabic translation of the Hebrew sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(hebrew_sentence, source_language="Hebrew", target_language="Arabic")


# program
{
    "method": "hebrew_to_arabic",
    "arguments": {
        "hebrew_sentence": "str",
    },
    "return": "str",
    "execute": "hebrew_to_arabic(hebrew_sentence)",
}


# preprocessor
def preprocess(input: str):
    hebrew_sentence = input
    return hebrew_sentence
