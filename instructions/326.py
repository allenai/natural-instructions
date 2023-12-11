def is_the_comment_obscene(comment: str) -> str:
    """
    Given a comment, identify if the comment is obscene or non-obscene. The comment is considered obscene if it is offensive to the public sense of decency.

    Parameters:
        comment (str): a given comment

    Returns:
        str: whether the comment is obscene or non-obscene
    """

    # this function chekcs if the comment is offensive to the public decency or not. the comment is offensive to public sense of decency if the comment relates to sex or any other topic considered taboo
    if is_offensive_to_public_decency(comment):
        return "obscene"
    else:
        return "non-obscene"


# program
{
    "method": "is_the_comment_obscene",
    "arguments": {
        "comment": "str",
    },
    "return": "str",
    "execute": "is_the_comment_obscene(comment)",
}


# preprocessor
def preprocess(input: str):
    comment = input.split("Comment: ")[1]
    return comment
