def generate_inference(statement: str, choice1: str, choice2: str, choice3: str) -> str:
    """Given a statement and three choices, the task is to get the choice that can be inferred from the statement. The answer should be '1', '2' or '3'.
    Parameters:
        statement: sentence representing a statment
        choice1: first choice
        choice2: second choice
        choice3: third choice
        Returns:
                str: answer to the question
    """

    # get one choice out the three choices
    answer = get_inference(statement, choice1, choice2, choice3)

    # return the answer
    return answer


# program
{
    "method": "generate_inference",
    "arguments": {"statement": "str", "choice1": "str", "choice2": "str", "choice3": "str"},
    "return": "str",
    "execute": "generate_inference(statement, choice1, choice2, choice3)",
}


# preprocessor
def preprocess(input: str):
    choices = input.split("Choices:")
    statement = choices[0].split("Statement:")[-1].strip()
    choice1 = choices[1].split(" 3.")[0].split(" 2.")[0].split(" 1.")[1].strip()
    choice2 = choices[1].split(" 3.")[0].split(" 2.")[1].strip()
    choice3 = choices[1].split(" 3.")[1].strip()
    return statement, choice1, choice2, choice3
