def are_arguments_similar(argument_1: str, argument_2: str) -> str:
    """
    Given two arguments cetered around Gay marriage, the task is to classify whether the two arguments are similar or not. The arguments are similar if they are about the same FACET (making the same argument). A FACET is a low level issue that often reoccurs in many arguments in support of the author's stance or in attacking the other author's position.

    Parameters:
        argument_1 (str): Argument 1
        argument_2 (str): Argument 2

    Returns:
        str: \"Similar\" or \"Not Similar\"
    """

    # this function takes in two arguments and checks if they are making the same argument or not
    if make_same_argument(argument_1, argument_2):
        return "Similar"
    else:
        return "Not Similar"


# program
{
    "method": "are_arguments_similar",
    "arguments": {
        "argument_1": "str",
        "argument_2": "str",
    },
    "return": "str",
    "execute": "are_arguments_similar(argument_1, argument_2)",
}


# preprocessor
def preprocess(input: str):
    argument_1 = input.split("Sent2: ")[0].split("Sent1: ")[-1].strip()
    argument_2 = input.split("Sent2: ")[-1].strip()
    return argument_1, argument_2
