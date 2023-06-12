def generate_question(context_word: str, question: str, answer: str) -> str:
    """
    Given a fill-in-the-blank question containing two objects. The answer which is one of the objects is also provided. Generate a question by minimallly changing the given question such that the answer flips to the second object in the question. The task typically involves replacing the trigger word with it's antonym. The content of the question should not be changed beyond a word or two. The xpected answer to the question should be the second object. The answer must not be associated with the trigger word but, instead depend on the context present in the sentence. Answers whould not be ambiguous. The questionshould not have potentially explicit, offensive, or adult content. The question should not use animals and proper nouns as objects. The question should contain at least 15 and at max 30 words. The question should have at least 70% overlapping words with the given question. There should only one blank in each of the question. The two objects must agree in number.

    Parameters:
        context_word (str): context_word
        question (str): question
        answer (str): answer

    Returns:
        str: question
    """

    # get the objects present in the question and are related to the context word
    object_1, object_2 = get_two_objects(context_word, question)

    sentence = question.replace("_", object_1)

    # get the trigger word for the given object and the context word in the sentence
    trigger_word = get_trigger_word(sentence, object_1)

    # Minimally modify the question such that object_2 becomes the answer. This can be accomplished by The task typically involves replacing the trigger word with it's antonym. The generated question should have at least 70% overlapping words with the input question. The sentence should not contain explicit, adult or offensive content
    question_2 = modify_question(
        question, object_2, trigger_word, min_sentence_length=15, max_sentence_length=30, has_explicit_content=False, has_adult_content=False, has_offensive_content=False, max_word_replace=2
    )

    return question_2


# program
{
    "method": "generate_question",
    "arguments": {
        "context_word": "str",
        "question": "str",
        "answer": "str",
    },
    "return": "str",
    "execute": "generate_question(context_word, question, answer)",
}


# preprocessor
def preprocess(input: str):
    context_word = input.split(" \n")[0].split("Context word: ")[-1][:-1]
    question = input.split("\nQuestion: ")[-1].split("\nAnswer: ")[0]
    answer = input.split("\nAnswer: ")[-1].split(".")[0]

    return context_word, question, answer
