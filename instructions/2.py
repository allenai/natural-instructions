def extract_answer(passage: str, question: str) -> str:
    """Write answers to questions involving multiple references to the same entity in the given passage. The answer to the question is unambiguous and a phrase in the passage.
    Parameters:
        passage: passage involving multiple references to the same entity
        question: question to be answered
    Returns:
        str:answer to the question
    """

    # get answer which is the entity referenced multiple times based on the question
    entity_answer = extract_entity_answer_to_question(passage, question)

    # return the answer
    return entity_answer


# program
{
    "method": "extract_answer",
    "arguments": {
        "passage": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "extract_answer(passage,question)",
}


# preprocessor
def preprocess(input: str):
    passage = input.split("Question:")[0].split("Passage:")[1].strip()
    question = input.split("Question:")[1].strip()
    return passage, question
