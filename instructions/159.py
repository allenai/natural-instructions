def is_frequency_word_same(sentence_1: str, sentence_2: str, word: str) -> str:
    """
    Given two sentences and a word. If the frequency of occurence of the word in the two sentences is same then return 'Yes' else 'No'

    Parameters:
        sentence_1 (str): Sentence 1
        sentence_1 (str): Sentence 2
        word (str): word of interest that should be compared for similar frequency counts in the two sentences

    Returns:
        str: \"Yes\" if the frequencey of a word is same in the two sentences or \"No\"
    """

    # this function return the frequency of the word in a given sentence
    frequency_1 = get_frequency(sentence_1, word)
    frequency_2 = get_frequency(sentence_2, word)

    if frequency_1 == frequency_2:
        return "Yes"
    else:
        return "No"


# program
{
    "method": "is_frequency_word_same",
    "arguments": {
        "sentence_1": "str",
        "sentence_2": "str",
        "word": "str",
    },
    "return": "str",
    "execute": "is_frequency_word_same(sentence_1, sentence_2, word)",
}


# preprocessor
def preprocess(input: str):
    sentence_1 = input.split("Sentence2: ")[0].split("Sentence1: ")[-1].strip()
    sentence_2 = input.split("Sentence2: ")[-1].split(". ")[0]

    word = input.split("Sentence2: ")[-1].split(". ")[-1].split("'")[1]
    return sentence_1, sentence_2, word
