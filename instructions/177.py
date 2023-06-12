def paraphrase_sentence(sentence: str) -> str:
    """
    Given a sentence, generate a paraphrase. The paraphrse should express the same meaning using different words

    Parameters:
        sentence (str): Sentence

    Returns:
        str: paraphrase
    """

    # this function generates the paraphrase of the given sentence
    return generate_paraphrase(sentence, use_different_words=True)


# program
{
    "method": "paraphrase_sentence",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "paraphrase_sentence(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
