def verify_the_claim(post: str, claim: str) -> str:
    """
    Given a post and a claim surrounding the post, the task is to validate if the claim is true or not. A post is HYPOTHETICAL if the author is considering doing something in the future. A post is HISTORICAL if the author has already done something.

    Parameters:
        post (str): a post
        claim (str): Either HYPOTHETICAL or HISTORICAL

    Returns:
        str: \"Yes"\ or \"No\"
    """

    if claim == "HYPOTHETICAL":
        # the function takes in an post and checks if the post talks about something that the author will be doing in the future
        if is_post_hypothetical(post):
            return "yes"
        else:
            return "no"

    if claim == "HISTORICAL":
        # the function takes in an post and checks if the post talks about something that the author has already done
        if is_post_historical(post):
            return "yes"
        else:
            return "no"


# program
{
    "method": "verify_the_claim",
    "arguments": {
        "post": "str",
        "claim": "str",
    },
    "return": "str",
    "execute": "verify_the_claim(post, claim)",
}


# preprocessor
def preprocess(input: str):
    claim = input.split(" POST :")[0].strip()
    if "HISTORICAL" in claim:
        claim = "HISTORICAL"
    else:
        claim = "HYPOTHETICAL"
    post = input.split("POST : ")[-1].strip()
    return post, claim
