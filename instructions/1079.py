def english_to_gujarati(english_sentence: str) -> str:
    """
    Given a sentence in the English language, translate it to Gujarati language

    Parameters:
        english_sentence (str): an English sentence

    Returns:
        str: Gujarati translation of the English sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(english_sentence, source_language="English", target_language="Gujarati")


# program
{
    "method": "english_to_gujarati",
    "arguments": {
        "english_sentence": "str",
    },
    "return": "str",
    "execute": "english_to_gujarati(english_sentence)",
}


# preprocessor
def preprocess(input: str):
    english_sentence = input
    return english_sentence
