def generate_answer(question: str) -> str:
    """Given the provided goal task in the input, describe a process that would lead to the asked outcome. This process often involves physical motions with objects, such as moving them, arranging them in a certain way, mixing them, shaking them, etc.

    Parameters:
        question: question to be answered

    Returns:
        str:answer describing the process
    """

    # get answer by physical reasoning and common sense reasoning
    answer = get_process(physical_reasoning=True, common_sense_reasoning=True)
    return answer


# program
{
    "method": "generate_answer",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "generate_answer(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
