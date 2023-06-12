def generate_overlapping_word(sentence_1: str, sentence_2: str) -> str:
    """
    Given two sentences, sentence_1 and sentence_2, find the overlapping words. The overlapping words don't have to match exactly i.e. their surface forms need not be the same but the root word should be the same. Also, do not consider stop words for overlapping words. The overlapping words should be significant.

    Parameters:
        sentence_1 (str): An English sentence_1
        sentence_2 (str): An English sentence_2

    Returns:
        str: overlapping word
    """

    # this function returns the overlapping word between the two sentences
    return find_overlapping_words(sentence_1, sentence_2, ignore_stop_words=True, is_significant_word=True)


# program
{
    "method": "generate_overlapping_word",
    "arguments": {
        "sentence_1": "str",
        "sentence_2": "str",
    },
    "return": "str",
    "execute": "generate_overlapping_word(sentence_1, sentence_2)",
}


# preprocessor
def preprocess(input: str):
    sentence_1 = input.rpartition("Sentence2: ")[0].partition("Sentence1: ")[-1]
    sentence_2 = input.rpartition("Sentence2: ")[2]
    return sentence_1, sentence_2
