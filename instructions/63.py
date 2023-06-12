def output_first_i_elements_in_list(index: int, elements_list: list) -> list:
    """
    Given an index, and, a list; print the first `index` elements of the list

    Parameters:
        index (int): index value
        elements_list (list): the list of elements

    Returns:
        list: The first `index` elements of the list
    """

    return elements_list[:index]


# program
{
    "method": "output_first_i_elements_in_list",
    "arguments": {
        "index": "int",
        "elements_list": "list",
    },
    "return": "list",
    "execute": "output_first_i_elements_in_list(index, elements_list)",
}


# preprocessor
def preprocess(input: str):
    import ast

    input = ast.literal_eval(input)
    index = input[0]
    elements_list = input[1]
    return index, elements_list
