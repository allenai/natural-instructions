def generate_question(background: str, story: str) -> str:
    """
    Given a background paragraph that describes one or more causal or qualitative relationships such as a relationship in economics or a scientific law and a story that makes use of the concepts or the relationship described in the provided paragraph. The task is to come up with a question about the story that requires an understanding of the relationship described in the background paragraph. The generated question should not be answerable without both the background and story. Write a question about the story that requires a relationship in the background paragraph to answer.

    Parameters:
        background (str): background
        story (str): story

    Returns:
        str: question
    """

    # this function extracts the causal or qualitative relationship in economics or a scientific law mentioned in the background.
    causal_or_qualitative_relationship = extract_causal_or_qualitative_relationship(background)

    # this function generates a question from the story. The answer should be present in the story. Answering the question requires understanding of the causal_or_qualitative_relationship
    question = generate_question_from_story(story, requires_understanding_of=causal_or_qualitative_relationship)

    return question


# program
{
    "method": "generate_question",
    "arguments": {
        "background": "str",
        "story": "str",
    },
    "return": "str",
    "execute": "generate_question(background, story)",
}


# preprocessor
def preprocess(input: str):
    background = input.split("\nStory: ")[0].split("Background Paragraph: ")[-1]
    story = input.split("\nStory: ")[-1]

    return background, story
