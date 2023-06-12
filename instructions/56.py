def is_correct_complete_answer(passage: str, question: str, answer: str) -> str:
    """Checks if the question is correctly and completely answered based on the passage and if true return yes else returns No.

    Parameters:
        passage: description
        question: question to be answered from the passage
        answer: answer identified

    Returns:
        str:'Yes' if correctly and completely answered else 'No'
    """

    # check if the question is correctly and completely answered based on the passage
    if check_for_correct_and_complete_answer(passage, question, answer) == "True":
        return "Yes"
    # if question is partially or incorrectly answered return No
    else:
        return "No"


# program
{
    "method": "is_correct_complete_answer",
    "arguments": {
        "passage": "str",
        "question": "str",
        "answer": "str",
    },
    "return": "str",
    "execute": "is_correct_complete_answer(passage,question,answer)",
}


# preprocessor
def preprocess(input: str):
    passage = input.split("Question:")[0].strip()
    question = input.split("Question:")[1].strip().split("Correct Answer:")[0].strip()
    answer = input.split("Question:")[1].strip().split("Correct Answer:")[1].strip()
    return passage, question, answer
