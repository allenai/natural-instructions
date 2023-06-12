def generate_example_for_same_sense(word: str, sentence: str) -> str:
    """
    Given a word and a sentence containing the word. Construct another sentences using the word and having the same sense as in the given sentence

    Parameters:
        word (str): a word
        sentence (str): sentence containing the word

    Returns:
        str: another sentence containing the given word in the same sense
    """

    # identify the sense of the word in the given sentence
    sense = identify_sense(word, sentence)

    # constructs a sentence using the word and the sense given. Avoids generating sentences given
    return construct_sentence_given_word(word, sense=sense, avoid_sentence=sentence)


# program
{
    "method": "generate_example_for_same_sense",
    "arguments": {
        "word": "str",
        "sentence": "str",
    },
    "return": "str",
    "execute": "generate_example_for_same_sense(word, sentence)",
}


# preprocessor
def preprocess(input: str):
    word = input.split("\n")[0].strip()
    sentence = input.split("\Sentence: ")[-1].strip()
    return word, sentence
