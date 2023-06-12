def reverse_array(list_of_numbers: list) -> list:
    """
    Given a list of integers, return the list in the reverse order

    Parameters:
        list_of_numbers (list): list of numbers

    Returns:
        list: given list in reverse order
    """

    # this function reverse the elements of the given list
    return reverse_list(list_of_numbers)


# program
{
    "method": "reverse_array",
    "arguments": {
        "list_of_numbers": "list",
    },
    "return": "list",
    "execute": "reverse_array(list_of_numbers)",
}


# preprocessor
def preprocess(input: str):
    import json

    list_of_numbers = json.loads(input)
    return list_of_numbers
