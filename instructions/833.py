def generate_sentiment(sentence: str) -> str:
    """For given sentence, the task in get the senitment about those sentence. For a positive sentiment return "postive" else return "negative".
    Parameters:
        setence: sentences
        Returns:
                str:answer to the question
    """

    # predict the sentiment
    if sentiment_is_positive(sentence):
        return "positive"
    else:
        return "negative"


# program
{
    "method": "generate_sentiment",
    "arguments": {"sentence": "str"},
    "return": "str",
    "execute": "generate_sentiment(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
