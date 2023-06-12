def find_sentiment_polarity_of_french_review(sentence: str) -> str:
    """
    Given a French sentence containing dvd product reviews, classify the review as positive polarity if the overall sentiment of the review is positive else negative

    Parameters:
        sentence (str): a French sentence containing dvd product reviews

    Returns:
        str: \"POS"\ or \"NEG\"
    """

    # this function checks if the overall sentiment of the French sentence is positive or not
    if overall_sentiment_positive(sentence):
        return "POS"
    else:
        return "NEG"


# program
{
    "method": "find_sentiment_polarity_of_french_review",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "find_sentiment_polarity_of_french_review(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
