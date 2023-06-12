def get_price_range(dialog_context: str) -> str:
    """The input is a conversation between an automated system and a user looking for suggestions for pubs, restaurants and coffee shops in Cambridge. In the dialogue, the user may provide some criteria for the type of place they want such as price range, cuisine, etc. Given such a dialogue, output the price range the user if looking for which can take one of four values: Cheap, Moderate, Expensive and Don't Care. Output cannot be any other value than the four values. Note that if the user asks for the prices of items provided at a pub, restaurant or coffee shop but doesn't mention the price range they are looking for then the correct classification will be Don't Care. If the user does not mention a particular price, the correct classification will be Don't Care.

    Parameters:
        dialog_context: dialog between user and agent

    Returns:
        str: price range that can be one of the following: "Cheap", "Moderate", "Expensive", "Dont' Care"
    """

    # the price range the user if looking for which can take one of four values: Cheap, Moderate, Expensive and Don't Care
    price_range_labels = ["Cheap", "Moderate", "Expensive", "Dont' Care"]

    # get price range. if the user asks for the prices of items provided at a pub, restaurant or coffee shop but doesn't mention the price range they are looking for then the correct classification will be Don't Care. If the user does not mention a particular price, the correct classification will be Don't Care.
    price_range = get_price_range(dialog_context, price_range_labels)

    return price_range


# program
{
    "method": "get_price_range",
    "arguments": {
        "dialog_context": "str",
    },
    "return": "str",
    "execute": "get_price_range(dialog_context)",
}

# preprocessor
def preprocess(input: str):
    dialog_context = input
    return dialog_context
