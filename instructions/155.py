def count_noun_verbs(sentence: str, pos_tag: str) -> int:
    """
    Count the number of nouns/verbs in the given sentence
    If the instruction is to count the number of nouns then return the number of nouns in the sentence
    If the instruction is to count the number of verbs then return the number of verbs in the sentence
    Ignore the instruction part while counting for frequency

    Parameters:
        sentence (str): An English Sentence
        pos_tag (str): the target POS category, either nouns or verbs

    Returns:
        int: Count of nouns or verbs
    """

    # this function returns the count of tokens belonging to a given POS tag
    return count_of_pos_tags(sentence, pos_tag)


# program
{
    "method": "count_noun_verbs",
    "arguments": {
        "sentence": "str",
        "pos_tag": "str",
    },
    "return": "int",
    "execute": "count_noun_verbs(sentence, pos_tag)",
}


# preprocessor
def preprocess(input: str):
    sentence = input.split("Sentence: '")[1].split("'. Count")[0]
    pos_tag = input.split("Count the number of ")[1].split(" in this sentence.")[0]
    return sentence, pos_tag
