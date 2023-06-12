def reverse_elements_in_list_in_range(begin_index: int, end_index: int, elements_list: list) -> list:
    """
    Given the begin index, end index, and, a list; print the elements of the list from begin index to end index in reverse order

    Parameters:
        begin_index (int): the starting index in the list
        end_index (int): the end index in the list
        elements_list (list): the list of elements

    Returns:
        list: The elements of the list from begin endex to end index in reverse order
    """

    # function which reverses the elements of the list
    return reverse_list_element(elements_list[begin_index : end_index + 1])


# program
{
    "method": "reverse_elements_in_list_in_range",
    "arguments": {
        "begin_index": "int",
        "end_index": "int",
        "elements_list": "list",
    },
    "return": "list",
    "execute": "reverse_elements_in_list_in_range(begin_index, end_index, elements_list)",
}


# preprocessor
def preprocess(input: str):
    import ast

    input = ast.literal_eval(input)
    begin_index = input[0]
    end_index = input[1]
    elements_list = input[2]
    return begin_index, end_index, elements_list
