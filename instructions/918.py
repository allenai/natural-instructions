def generate_answer_from_story(story: str, question: str) -> str:
    """Based on the story provided and the given question, return the shortest continuous text span from the story that serves as an answer to the given question.
    Do not return answers that are incorrect or provide incomplete justification for the question.

    Parameters:
        story: story from which answers need to be generated
        question: question to be answered

    Returns:
        str: continuous text span from the story that serves as an answer
    """
    # Generate span-extracted answer from story for the given question
    answer = generate_answer(story, question=question, type="span", must_have_justification=True)

    return answer


# program
{
    "method": "generate_answer_from_story",
    "arguments": {"story": "str", "question": "str"},
    "return": "str",
    "execute": "generate_answer_from_story(story, question)",
}


# preprocessor
def preprocess(input: str):
    splits = input.split("question: ")
    try:
        splits[0] = splits[0].split("story: ")[1].strip()[:-3]
    except:
        try:
            splits[0] = splits[0].split('"story": "')[1].strip()[:-3]
        except:
            try:
                splits[0] = splits[0].split('"story" : "')[1].strip()[:-3]
            except:
                splits[0] = splits[0].split("story : ")[1].strip()[:-3]
    splits[1] = splits[1].strip()[1:]
    story, question = splits
    return story, question
