def classify_genre_sentiment(article: str, genre: str) -> str:
    """For given news article and a genre, get the sentiment about the given genre. If the sentiment is positive return "positive" else return "negative"
    Parameters:
        article: news article in thai language
        genre: genre
        Returns:
                str: If the sentiment for the genre is positive return "positive" else return "negative"
    """

    # predict the sentiment about the genre
    answer = get_sentiment(article, genre)

    # return the answer
    return answer


# program
{
    "method": "classify_genre_sentiment",
    "arguments": {"article": "str", "genre": "str"},
    "return": "str",
    "execute": "classify_genre_sentiment(article, genre)",
}


# preprocessor
def preprocess(input: str):
    sentences = input.split("\n")
    article = "\n".join(sentences[:-2])
    genre = sentences[-1].split("genre:")[1].strip()
    return article, genre
