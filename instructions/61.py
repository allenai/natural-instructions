def generate_answer(background: str, story: str, question: str) -> str:
    """
    Given a background paragraph that describes one or more causal or qualitative relationships and a story that makes use of the concepts or the relationship described in the provided paragraph. Given a question about the story that requires an understanding of the relationship described in the background paragraph and the story, generate an answer to the given question.
    The answer will be a span from either the question or the story. In order to correctly answer the given question, the understanding of the relationship mentioned in the background paragraph and using it to understand that in the story is required.
    The answer should not consist of any word that is not mentioned in any of these: the background paragraph, the story, or the question.


    Parameters:
        background (str): paragraph that describes one or more causal or qualitative relationships
        story (str): passage that conatins concepts or the relationship from the background paragarph
        question (str): question related to story which requires understanding of the paragaraph

    Returns:
        str: answer spanning from the story or the question
    """

    # this function extracts the causal or qualitative relationship metioned in the background.
    causal_or_qualitative_relationship = extract_causal_or_qualitative_relationship(background)

    # this function generates an answer which can be a span from either the question or the story. Answering the question requires understanding of the causal_or_qualitative_relationship
    answer = generate_answer_given_question(question, story, requires_understanding_of=causal_or_qualitative_relationship)

    return answer


# program
{
    "method": "generate_answer",
    "arguments": {
        "background": "str",
        "story": "str",
        "question": "str",
    },
    "return": "str",
    "execute": "generate_answer(background, story, question)",
}


# preprocessor
def preprocess(input: str):
    background = input.split("\nStory: ")[0].split("Background Paragraph: ")[-1]
    story = input.split("\nStory: ")[-1].split(" \nQuestion:")[0]
    question = input.split(" \nQuestion:")[-1]

    return background, story, question
