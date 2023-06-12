def generate_question(context_word: str, question: str, answer: str) -> str:
    """
    Given a fill-in-the-blank question where the answer is PersonX. Generate a question by minimallly changing the given question such that the answer flips to PersonY. The task typically involves replacing the trigger word with it's antonym. The content of the question should not be changed beyond a word or two. PersonX and PersonY should not be equally likely to fill the blank. For the generated question, PersonY should be a well-agreed answer to fill in the blank. The question should not have potentially explicit, offensive, or adult content. Do not use real people or generic names. The question should contain at least 15 and at max 30 words. The question should have at least 70% overlapping words with the given question. There should only one blank in each of the question. Both PersonX and PersonY must agree in gender. In the question, PersonX and PersonY should appear only once, and PersonX should appear before PersonY

    Parameters:
        context_word (str): context_word
        question (str): question
        answer (str): answer

    Returns:
        str: question
    """

    sentence = question.replace("_", answer)

    # get the trigger word for the given context word in the sentence
    trigger_word = get_trigger_word(sentence, context_word)

    # Minimally modify the question such that PersonY becomes the answer. This can be accomplished by replacing the trigger word with it's antonym. The generated question should have at least 70% overlapping words with the input question. The sentence should not contain explicit, adult or offensive content
    question_2 = modify_question(
        question, context_word, trigger_word, min_sentence_length=15, max_sentence_length=30, has_explicit_content=False, has_adult_content=False, has_offensive_content=False, max_word_replace=2
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
