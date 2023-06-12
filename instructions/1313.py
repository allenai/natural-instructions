def validate_polarity_classifier(review: str, polarity: str) -> bool:
    """Given a review and its polarity (positive or negative). Validate if the polarity matches with the review.
    Parameters:
        review: passage describing the product
    Returns:
        bool:true if polarity matches with the review sentiment else false
    """
    if get_polarity(review) == polarity:
        return True
    else:
        return False


# program
{"method": "validate_polarity_classifier", "arguments": {"review": "str", "polarity": "str"}, "return": "bool", "execute": "validate_polarity_classifier(review, polarity)"}


# preprocessor
def preprocess(input: str):
    review = input.split("Polarity:")[0].split("Review:")[1].strip()
    polarity = input.split("Polarity:")[1].strip()
    return review, polarity
