def generate_concluding_fact(fact: str, topic: str) -> str:
    """
    Given two facts, write a concluding fact. There should be some parts of the first and second facts that are not mentioned in this conclusion fact. The combined fact should be the result of a chain between the two facts. Parts of the conluding fact should overlap with the first and second fact.

    Parameters:
        first_fact (str): first fact
        second_fact (str): second fact

    Returns:
        str: concluding fact
    """

    # this function extracts the subject from the first fact
    subject = extract_subject(first_fact)

    # this function extracts the conclusion from the second fact
    conclusion = extract_conclusion(second_fact)

    # this function generates a fact having the specified subject and the conclusion
    return generate_fact(subject, conclusion)


# program
{
    "method": "generate_concluding_fact",
    "arguments": {
        "first_fact": "str",
        "second_fact": "str",
    },
    "return": "str",
    "execute": "generate_concluding_fact(first_fact, second_fact)",
}


# preprocessor
def preprocess(input: str):
    first_fact = input.split("\nFact 2: ")[0].split("Fact 1: ")[-1]
    second_fact = input.split("\nFact 2: ")[-1]

    return first_fact, second_fact
