def translate_english_to_punjabi(english_sentence: str) -> str:
    """
    Given a sentence in the English language, translate it to Punjabi language without omitting or adding information

    Parameters:
        english_sentence (str): an English sentence

    Returns:
        str: Punjabi translation of the English sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(english_sentence, source_language="English", target_language="Punjabi")


# program
{
    "method": "translate_english_to_punjabi",
    "arguments": {
        "english_sentence": "str",
    },
    "return": "str",
    "execute": "translate_english_to_punjabi(english_sentence)",
}


# preprocessor
def preprocess(input: str):
    english_sentence = input
    return english_sentence
