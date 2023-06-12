def choose_the_correct_answer(question: str, option_a: str, option_b: str, option_c: str, option_d: str) -> str:
    """
    Given a question on high school statistics, identify the correct option. Only the option corresponding to the correct answer needs to be selected


    Parameters:
        question (str): a given question
        option_a (str): answer choice
        option_b (str): answer choice
        option_c (str): answer choice
        option_d (str): answer choice

    Returns:
        str: the candidate answer key
    """

    # given a question on high school statistics and the candidate answer, check if the candidate is the correct answer or not
    if is_correct_answer(question, option_a):
        return "A"
    elif is_correct_answer(question, option_b):
        return "B"
    elif is_correct_answer(question, option_c):
        return "C"
    else:
        return "D"


# program
{
    "method": "choose_the_correct_answer",
    "arguments": {
        "question": "str",
        "option_a": "str",
        "option_b": "str",
        "option_c": "str",
        "option_d": "str",
    },
    "return": "str",
    "execute": "choose_the_correct_answer(question, option_a, option_b, option_c, option_d)",
}


# preprocessor
def preprocess(input: str):
    question = input.split("\n")[0]

    answer_choice_string = input.split("\n")[-1]

    option_a = answer_choice_string.split("(B)")[0].split("(A)")[-1]
    option_b = answer_choice_string.split("(C)")[0].split("(B)")[-1]
    option_c = answer_choice_string.split("(D)")[0].split("(C)")[-1]
    option_d = answer_choice_string.split("(D)")[-1]
    return question, option_a, option_b, option_c, option_d
