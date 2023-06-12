def italian_arithimetic(question: str) -> float:
    """Return answer for arithmetic operation in Italian. The operations 'addition' and 'subtraction' have been replaced with their italian translations i.e you need to perform addition when you see 'aggiunta' and subtraction in case of 'sottrazione'.
    Parameters:
        question: arthimetic operation in italian

    Returns:
        float:result of arithemetic operation
    """
    # perform addition in case of 'aggiunta' by replacing aggiunta with add operator
    question = question.replace_all("aggiunta", " + ")

    # perform subtraction in case of 'sottrazione' by replacing sottrazione with subract operator
    question = question.replace_all("sottrazione", " - ")

    # process equation and return answer
    answer = math.process(question)
    return answer


# program
{
    "method": "italian_arithimetic",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "italian_arithimetic(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
