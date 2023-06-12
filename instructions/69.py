def pick_plausible_story_coherent(beginning: str, middle_1: str, middle_2: str, ending: str) -> str:
    """
    Given the beginning and ending of a story along with two candidates for the middle of the story. Return the best candidate which makes the story more coherent or plausible as either 1 or 2

    Parameters:
        beginning (str): The beginning of the story
        middle_1 (str): Plausible candidate for the middle of the story
        middle_2 (str): Plausible candidate for the middle of the story
        ending (str): Ending of the story

    Returns:
        str: 1 if middle_1 is more coherent or 2 if middle_2 is more coherent
    """

    # function which takes in a beginning, middle, and, end of the story and returns a coherency score. If candidate1 coherency score is greater than candidate2 return 1
    if get_coherent_score(beginning, middle_1, ending) > get_coherent_score(beginning, middle_2, ending):
        return "1"
    else:
        # if candidate2 coherency score is greater than candidate1 return 2
        return "2"


# program
{
    "method": "pick_plausible_story_coherent",
    "arguments": {
        "beginning": "str",
        "middle_1": "str",
        "middle_2": "str",
        "ending": "str",
    },
    "return": "str",
    "execute": "pick_plausible_story_coherent(beginning, middle_1, middle_2, ending)",
}


# preprocessor
def preprocess(input: str):
    beginning = input.split("Middle 1")[0].split("Beginning: ")[-1]
    middle_1 = input.split("Middle 2")[0].split("Middle 1: ")[-1]
    middle_2 = input.split("Ending")[0].split("Middle 2: ")[-1]
    ending = input.split("Ending: ")[-1]
    return beginning, middle_1, middle_2, ending
