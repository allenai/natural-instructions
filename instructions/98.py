def get_intersection(list_1: list, list_2: list) -> list:
    """Given two lists of numbers return the intersection between these two lists. The intersection between two lists is another list where every element is common between the two original lists. If there are no elements in the intersection, answer with an empty list. List of numbers must be inside brackets. Sort the numbers in an ascending order, that is, no matter what the order of the numbers in the lists is
    Parameters:
        list_1: first list of numbers
        list_2: second list of numbers

    Returns:
        list: interesection of list_1 and list_2 in sorted order
    """

    # get intersection between two lists
    list_intersection = intersection(list_1, list_2)

    # sort list
    sorted_list = list_intersection.sort(ascending=True)

    # convert sorted_list to string and including it within brackets and return it
    return str(sorted_list)


# program
{
    "method": "get_intersection",
    "arguments": {
        "list_1": "list",
        "list_2": "list",
    },
    "return": "str",
    "execute": "get_intersection(list_1,list_2)",
}


# preprocessor
def preprocess(input: str):
    input = input.replace(" ", "")
    list_1 = input.split("],[")[0] + "]"
    list_2 = "[" + input.split("],[")[1]
    return list_1, list_2
