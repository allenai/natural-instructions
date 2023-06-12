def generate_sentiment(tweet: str) -> str:
    """Given a text from tweet, the task in get the senitment about the tweet. For a positive sentiment tweet return "postive" else return "negative".
    Parameters:
        tweet: text from tweet
        Returns:
                str:answer to the question
    """

    # predict the sentiment (postive or ne
    if get_sentiment(tweet) == "positive":
        return "positive"
    else:
        return "negative"


# program
{
    "method": "generate_sentiment",
    "arguments": {"tweet": "str"},
    "return": "str",
    "execute": "generate_sentiment(tweet)",
}


# preprocessor
def preprocess(input: str):
    tweet = input
    return tweet
