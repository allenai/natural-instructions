def get_sentiment(sentence: str) -> str:
    """Given a sentence identify the sentiment based on its empathetic direction. If sentiment is happy return "positive" and if its offmychest return "negative"
    Parameters:
        sentence : engilsh sentence
        Returns:
                str: "positive" for happy setiment expressed else "negative"
    """

    # check if the sentence expresses happy sentiment
    if is_happy_sentiment(sentence):
        return "positive"
    else:
        return "negative"


# program
{
    "method": "get_sentiment",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "get_sentiment(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
