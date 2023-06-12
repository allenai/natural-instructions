def return_common_genre(sentence_1: str, sentence_2: str) -> str:
    """Given a pair of sentences, sentence 1 and sentence 2, write a single word that describes the genre that the two sentences belong to, such as face-to-face, government, letters, 9/11, slate, telephone, travel, verbatim, oup, fiction.

    Parameters:
        sentence_1: first sentence
        sentence_2: second sentence

    Returns:
        str: single word that describes the genre that the two sentences
    """
    # Generate span-extracted answer from story for the given question
    genre_set = {"face-to-face", "government", "letters", "9/11", "slate", "telephone", "travel", "verbatim", "oup", "fiction"}
    genre = get_common_genre(sentence_1, sentence_2, genre_set)
    return genre


# program
{
    "method": "return_common_genre",
    "arguments": {
        "sentence_1": "str",
        "sentence_2": "str",
    },
    "return": "str",
    "execute": "return_common_genre(sentence_1,sentence_2)",
}


# preprocessor
def preprocess(input: str):
    splits = input.split("Sentence 2:")
    sentence_1 = splits[0].split("Sentence 1:")[1].strip()
    sentence_2 = splits[1].strip()
    return sentence_1, sentence_2
