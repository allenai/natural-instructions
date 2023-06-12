def translate_thai_to_english(thai_sentence: str) -> str:
    """
    Given a sentence in the Thai language, translate it to English language

    Parameters:
        thai_sentence (str): a Thai sentence

    Returns:
        str: English translation of the Thai sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(thai_sentence, source_language="Thai", target_language="English")


# program
{
    "method": "translate_thai_to_english",
    "arguments": {
        "thai_sentence": "str",
    },
    "return": "str",
    "execute": "translate_thai_to_english(thai_sentence)",
}


# preprocessor
def preprocess(input: str):
    thai_sentence = input
    return thai_sentence
