def generate_question_given_subject_relation(context: str, subject: str, relation: str) -> str:
    """
    Given a context, a subject and a relation. Generate a question involving the subject and the relation. The question should use words from given subject, relation, and, the context as much as possible

    Parameters:
        context (str): context
        subject (str): subject
        relation (str): relation

    Returns:
        str: a question involving the subject and the relation from the context
    """

    # this function generates a question involving the subject and the relation.
    return generate_question(context, subject, relation)


# program
{
    "method": "generate_question_given_subject_relation",
    "arguments": {
        "context": "str",
        "subject": "str",
        "relation": "str",
    },
    "return": "str",
    "execute": "generate_question_given_subject_relation(context, subject, relation)",
}


# preprocessor
def preprocess(input: str):
    context = input.split("Subject")[0].split("Context :")[-1].strip()
    subject = input.split("Relation")[0].split("Subject :")[-1].strip()
    relation = input.split("Relation :")[-1].strip()
    return context, subject, relation
