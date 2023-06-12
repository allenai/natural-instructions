def check_if_answerable(sentence: str, question: str) -> str:
    """Check if question is answerable based on the given sentence
    Parameters:
        sentence: sentence that could contain the answer
        question: question to be answered
    Returns:
        str:'Yes.' if answerable else 'No.'
    """

    # if the question is answerable based on the sentence
    if is_answerable(sentence, question):
        return "Yes."
    else:
        return "No."


# program
{
    "method": "check_if_answerable",
    "arguments": {
        "sentence": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "check_if_answerable(sentence,question)",
}


# preprocessor
def preprocess(input: str):
    sentence = input.split("Question:")[0].split("Sentence:")[1].strip()
    question = input.split("Question:")[1].strip()
    return sentence, question
