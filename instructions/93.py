def normalize_lists(number_list: list) -> list:
    """
    Normalize a given list of numbers such that the sum of all numbers in the list is 1
    The weights of the numbers should be maintained after normalization.
    Round-off the numbers to 3 decimal places.

    Parameters:
        number_list (list): list of numbers

    Returns:
        list: normalized list of numbers
    """

    # Function which normalizes a list such that the sum of all numbers in the list is 1
    normalized_number_list = normalize(number_list)
    # function which rounds off the floating point number to 3 decimal places
    return round_off_3_decimal(normalized_number_list)


# program
{
    "method": "normalize_lists",
    "arguments": {
        "number_list": "list",
    },
    "return": "list",
    "execute": "normalize_lists(number_list)",
}


# preprocessor
def preprocess(input: str):
    import json

    number_list = json.loads(input)
    return number_list
