def generate_unanswerable_question(passage: str) -> str:
    """Given a passage, construct a question that looks relevant to the given context but is unanswerable. Following are a few suggestions about how to create unanswerable questions:\n(i) create questions which require satisfying a constraint that is not mentioned in the passage\n(ii) create questions which require information beyond what is provided in the passage in order to answer\n(iii) replace an existing entity, number, date mentioned in the passage with other entity, number, date and use it in the question\n(iv) create a question which is answerable from the passage and then replace one or two words by their antonyms or insert/remove negation words to make it unanswerable.

    Parameters:
        passage: passage from which relevant but unanswerable question needs to be generated

    Returns:
        str: relevant but unanswerable question
    """
    # Possible strategies for creating unanswerable questions given a passage
    unanswerable_question_strategies = (
        "constraint not mentioned in passage",
        "require more information",
        "replace existing entity,number,date mentioned in passage",
        "modify answerable question by negation or replacement of words",
    )

    # Identify strategy best suited to generate unanswerable question given paragraph
    strategy = choose_best_strategy(passage, unanswerable_question_strategies)

    # generate question using chosen strategy
    question = generate_question(passage, unanswerable_question_strategy=strategy)

    return question


# program
{
    "method": "generate_unanswerable_question",
    "arguments": {
        "passage": "str",
    },
    "return": "str",
    "execute": "generate_unanswerable_question(passage)",
}


# preprocessor
def preprocess(input: str):
    splits = input.split("Passage:")
    passage = splits[1].strip()
    return passage
