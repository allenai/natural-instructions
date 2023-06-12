def is_comment_hope_speech(comment: str) -> str:
    """
    Given a comment, identify if the comment is in Tamil Language. If the comment is in Tamil language identify if it's an hope speech i.e. it contains encouraging, positive or supportive contents about equality, diversity or inclusion or not.

    Parameters:
        comment (str): a comment

    Returns:
        str: answer to the question
    """

    # this function checks if the comment is in tamil language
    if comment_in_tamil(comment):
        # this function checks if the comment is an hope speech
        if comments_is_hope_speech(comment):
            return "Hope Speech"
        else:
            return "Not Hope Speech"
    else:
        "Not in Expected Language"


# program
{
    "method": "is_comment_hope_speech",
    "arguments": {
        "comment": "str",
    },
    "return": "str",
    "execute": "is_comment_hope_speech(comment)",
}


# preprocessor
def preprocess(input: str):
    comment = input
    return comment
