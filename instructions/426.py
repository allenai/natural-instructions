def check_translation_match_hindi_english(hindi_text: str, english_text: str) -> str:
    """
    Checks if the translation of a Hindi sentence matches the given English translation.
    The translation preserves numbers and is sentence case (only beginning of sentence and
    nouns are capitalized).

    Parameters:
        hindi_text (str): hindi string
        english_text (str): english translation

    Returns:
        str: Yes/No
    """

    # do translation
    english_translation = translate_hindi_to_english(hindi_text)
    # check if translation matches the given english text
    return is_similar(english_translation, english_text)


# program
{
    "method": "check_translation_match_hindi_english",
    "arguments": {"hindi_text": "str", "english_text": "str"},
    "return": "str",
    "execute": "check_translation_match_hindi_english(hindi_text, english_text)",
}


# preprocessor
def preprocess(input: str):
    hindi_text, english_text = input.split(" \n ")
    hindi_text = hindi_text.split("Hindi: ")[1]
    english_text = english_text.split("English: ")[1]
    return hindi_text, english_text
