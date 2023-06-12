def is_the_label_correct(tweet: str, label: str) -> str:
    """
    Given a tweet and a corresponding label whether this tweet is 'Offensive', 'Hate Speech' or 'Neither', the task is to predict whether the label si correct or not

    Parameters:
        tweet (str): a tweet
        label (str): the corresponding label

    Returns:
        str: "true" if the label is correct else "false"
    """

    if label == "Hate Speech":
        # this function checks if the tweet is an hate speech or not
        if is_tweet_hate_speech(tweet):
            return "true"
        else:
            return "false"
    elif label == "Offensive":
        # this function checks if the tweet is offensive or not
        if is_tweet_offensive(tweet):
            return "true"
        else:
            return "false"
    elif label == "Neither":
        # this function checks if the tweet is offensive or not
        # this function checks if the tweet is an hate speech or not
        if is_tweet_offensive(tweet) or is_tweet_hate_speech(tweet):
            return "false"
        else:
            return "true"


# program
{
    "method": "is_the_label_correct",
    "arguments": {
        "tweet": "str",
        "label": "str",
    },
    "return": "str",
    "execute": "is_the_label_correct(tweet, label)",
}


# preprocessor
def preprocess(input: str):
    tweet = input.split("\n")[0].split("Tweet")[1].strip()
    label = input.split("Label: ")[-1].strip()
    return tweet, label
