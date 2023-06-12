def japanese_to_hebrew(japanese_sentence: str) -> str:
    """
    Given a sentence in the Japanese language, translate it to Hebrew language

    Parameters:
        japanese_sentence (str): a Japanese sentence

    Returns:
        str: Hebrew translation of the Japanese sentence
    """

    # Translate the given input sentence in source language to Target language
    return generate_translation(japanese_sentence, source_language="Japanese", target_language="Hebrew")


# program
{
    "method": "japanese_to_hebrew",
    "arguments": {
        "japanese_sentence": "str",
    },
    "return": "str",
    "execute": "japanese_to_hebrew(japanese_sentence)",
}


# preprocessor
def preprocess(input: str):
    japanese_sentence = input
    return japanese_sentence
