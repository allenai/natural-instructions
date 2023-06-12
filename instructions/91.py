def return_sublist(input_list: list[str], i: int, j: int) -> str:
    """
    Returns a string which is formed by joining the sublist input_list[i:j+1] using commas

    Parameters:
        input_list (list[str]): a list of elements
        i (int): starting index
        j (int): ending index

    Returns:
        str: string formed by joining the list
    """

    sublist = input_list[i : j + 1]
    return ", ".join(input_list[i : j + 1])


# program
{
    "method": "return_sublist",
    "arguments": {"input_list": "list[str]", "i": "int", "j": "int"},
    "return": "str",
    "execute": "return_sublist(input_list, i, j)",
}


# preprocessor
def preprocess(input: str):
    ij, input = input.split("[")
    input_list = "[" + input
    i, j, _ = ij.split(", ")
    i = int(i)
    j = int(j)
    i -= 1
    j -= 1
    return input_list, i, j
