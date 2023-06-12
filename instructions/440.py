def is_english_translation_of_gujarati(gujarati_sentence: str, english_sentence: str) -> str:
    """
    Given a Gujarati sentence, check if the correspnding English sentence is the translation of the Gujarati sentence

    Parameters:
        gujarati_sentence (str): a Gujarati sentence
        english_sentence (str): an English sentence

    Returns:
        str: \"Yes"\ or \"No\"
    """

    # this function checks if the english sentence is the translations of the Gujarati sentence or not
    if is_translation(gujarati_sentence, english_sentence):
        return "Yes"
    else:
        return "No"


# program
{
    "method": "is_english_translation_of_gujarati",
    "arguments": {
        "gujarati_sentence": "str",
        "english_sentence": "str",
    },
    "return": "str",
    "execute": "is_english_translation_of_gujarati(gujarati_sentence, english_sentence)",
}


# preprocessor
def preprocess(input: str):
    gujarati_sentence = input.split("English: ")[0].split("Gujarati: ")[1].strip()
    english_sentence = input.split("English: ")[-1].strip()
    return gujarati_sentence, english_sentence
