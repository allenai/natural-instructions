def categorize_question_given_dialogue(dialogue: str, question: str, answers: str) -> str:
    """
    In this task, we are given a conversation and a question. The question should be categorized into matching, summary, logic, arithmetic and, commonsense groups.

    \"W\" and \"M\" in the conversations stand for \"woman\" and \"man\"

    Matching: question is entailed or paraphrased by exactly one sentence in a dialogue. the answer should be extracted from the same sentence.

    If the question cannot be answered by the surface meaning of a single sentence then it belongs to reasoning category.

    Summary: summary questions require the whole picture of dialogue like the topic and the relation between the speakers

    Logic: question which requires logical reasoning

    Arithmetic: question which requires arithmetic knowledge

    Commonsense: questions which in addition requires commonsense knowledge not present in the dialogue.


    Parameters:
        dialogue (str): dialogue
        question (str): question
        answers (str): answers

    Returns:
        str: question category
    """

    # this function checks if the answer to the given question can be answered given the dialogue. The answer should be extracted from one of the sentences in the dialogue as is.
    if answer_can_be_extracted_from_dialogue(dialogue, question):
        return "matching"
    # this function checks if the dialogue requires arithmetic reasoning to answer
    elif question_requires_arithmentic_reasoning(dialogue, question):
        return "arithmetic"
    # this function checks if the dialogue requires logical reasoning to answer
    elif question_requires_logical_reasoning(dialogue, question):
        return "logic"
    # this function checks if the dialogue requires commonsense reasoning to answer
    elif question_requires_commonsense_reasoning(dialogue, question):
        return "commonsense"
    else:
        return "summary"


# program
{
    "method": "categorize_question_given_dialogue",
    "arguments": {
        "dialogue": "str",
        "question": "str",
        "answers": "str",
    },
    "return": "str",
    "execute": "categorize_question_given_dialogue(dialogue, question, answers)",
}


# preprocessor
def preprocess(input: str):
    dialogue = input.split("Question: ")[0]
    question = input.split("Question: ")[-1].split("(A)")[0]
    answers = "(A): " + input.split("(A): ")[-1]

    return dialogue, question, answers
