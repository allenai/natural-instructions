def generate_question_from_story(story: str) -> str:
    """Generate a question about the information present in the passage in such a way (i) it is unambiguous, (ii) it is answerable from the passage, (iii) the answer is unique, (iv) its answer is a continous text span from the paragraph. Avoid creating questions that (i) can be answered correctly without actually understanding the paragraph and (ii) uses same words or phrases given in the passage "

    Parameters:
        story: passage from which questions need to be generated


    Returns:
        str: question that is answerable from story
    """
    # Generate question answerable from story
    question = generate_question(
        story,
        is_unambiguous=True,
        is_answerable_from_passage=True,
        is_unique_answer=True,
        type="span",
        requires_passage_understanding=True,
    )

    return question


# program
{
    "method": "generate_question_from_story",
    "arguments": {
        "story": "str",
    },
    "return": "str",
    "execute": "generate_question_from_story(story)",
}


# preprocessor
def preprocess(input: str):
    story = input.strip()
    return story
