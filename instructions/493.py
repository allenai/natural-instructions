def classify_review(review: str) -> str:
    """classify the input review into Negative or Positive."
    Parameters:
        review: passage expressing sentiment
    Returns:
        str: sentiment value
    """

    # this function returns the sentiment value of the given review. The function returns `Positive` if the review has positive sentiment. The function returns `Negative` if the review has negative sentiment.
    return get_sentiment_of_review(review)


# program
{"method": "classify_review", "arguments": {"review": "str"}, "return": "str", "execute": "classify_review(review)"}


# preprocessor
def preprocess(review: str):
    return review
