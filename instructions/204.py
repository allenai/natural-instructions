def check_genre_similarity(sentence1: str, sentence2: str, genre: str) -> str:
    """Given two sentences and a genere determine if the two sentences belong to the same genre or not. If same return 'Y' else 'N'
    Parameters:
        sentence1: Description
        sentence2: Description
        genre : Genre
    Returns:
        str:Y if both the sentences belong to same genre else N
    """
    genres = ["face-to-face", "government", "letters", "9/11", "slate", "telephone", "travel", "verbatim", "oup", "fiction"]
    # identify the genre for the sentence1 with the given genre list
    sentence1_genre = get_genre(sentence1, genres)
    # identify the genre for the sentence1 with the given genre list
    sentence2_genre = get_genre(sentence2, genres)
    # check if both the sentences genre match with the given genre, if true return Y
    if genre == sentence1_genre and genre == sentence2_genre:
        return "Y"
    else:
        # even if any one of the sentence genre doesn't match the target genre return N
        return "N"


# program
{"method": "check_genre_similarity", "arguments": {"sentence1": "str", "sentence2": "str", "genre": "str"}, "return": "str", "execute": "check_genre_similarity(sentence1,sentence2, genre)"}


# preprocessor
def preprocess(input: str):
    sentence1 = input.split("Sentence 2: ")[0].split("Sentence 1: ")[1].strip()
    sentence2 = input.split("Sentence 2: ")[1].strip()
    genre = input.split("Genre: ")[1].strip()[0:-1]
    return sentence1, sentence2, genre
