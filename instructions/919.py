def generate_incorrect_answer_from_story(story: str, question: str) -> str:
    """Based on the story provided and the given question, return an incorrect answer

    Parameters:
        story: story from which incorrect answers need to be generated
        question: question to be answered incorrectly

    Returns:
        str: continuous text span from the story that is not the correct answer
    """
    # Generate span-extracted incorrect answer from story for the given question
    answer = generate_incorrect_answer(story, question=question, type="span")

    return answer


# program
{
    "method": "generate_incorrect_answer_from_story",
    "arguments": {"story": "str", "question": "str"},
    "return": "str",
    "execute": "generate_incorrect_answer_from_story(story,question)",
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
