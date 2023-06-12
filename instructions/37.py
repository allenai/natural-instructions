def generate_fact(fact: str, topic: str) -> str:
    """
    Given a fact and a topic, write a fact related to the given topic and based on the topic. The generated fact should have at least one word in common with the given fact. The genrated fact should form a chain with the given fact i.e, they connect together to produce a third fact. The generated fact should describe slightly different scientific phenomena.


    Parameters:
        passage (str): passage
        question (str): question
        answer_type (str): answer_type

    Returns:
        str: answer
    """

    # this function generates a related fact given the fact and grounded on the topic. The generated fact will have at least one overlapping word. The generated fact forms a chain with the given fact to produce a third fact.
    return generate_related_fact(fact, grounded_on=topic, min_overlapping_words=1, forms_chain=True)


# program
{
    "method": "generate_fact",
    "arguments": {
        "fact": "str",
        "topic": "str",
    },
    "return": "str",
    "execute": "generate_fact(fact, topic)",
}


# preprocessor
def preprocess(input: str):
    fact = input.split("\nTopic: ")[0].split("Fact: ")[-1]
    topic = input.split("\nTopic: ")[-1]

    return fact, topic
