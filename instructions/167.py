def generate_question(term: str, description: str, answer: str) -> str:
    """Given a term, a description of the term, and an expected answer ('yes' or 'no') this method creates a yes-no question about the given term such that the answer is the one provided. (i.e., If the answer is "No", the generated question should have its answer as "No", and if the answer is \"Yes\", the generated question should have its answer is \"Yes\". ). The generated question is one that has a definitive answer (as opposed to ambiguous or subjective questions, e.g., Is Batman a good movie?). The question is one such that its answer can not be found easily on a single web page (e.g., mentioned in a Wikipedia page). This can be accomplished if answering the question requires more than one fact (facts = statements that can be found on a Wikipedia page or Google).  For example, answering the question 'did Aristotle use a laptop?', one needs the know about the invention of the laptop and the death of Aristotle. Questions are not those that just compare the properties of objects (e.g., Is a door bigger than an elephant?) or those that refer to details in the given description."

    Parameters:
        term: term for which question needs to be created
        description: description of the term
        answer: yes or no
    Returns:
        str: generated_question
    """

    # create a question that has a yes/no answer and needs a definitive answer and does not rely on comparisons of properties for answering.
    question = create_question(term=term, term_description=description, answer_type=answer, question_needs_definitive_answer=True, property_comparisons_in_question=False)

    return question


# program
{
    "method": "generate_question",
    "arguments": {"term": "str", "description": "str", "answer": "str"},
    "return": "str",
    "execute": "generate_question(term,description,answer)",
}

# preprocessor
def preprocess(input: str):
    description = input.split("Description: ")[1].split(", Answer:")[0].strip()
    answer = input.split("Answer:")[1].strip()
    term = input.split("Description: ")[0].split("Term:")[1].strip()
    return term, description, answer
