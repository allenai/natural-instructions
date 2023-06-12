def cause_effect_classification(first_sentence: str, second_sentence: str) -> str:
    """
    Given two sentences in Indonesian language. classify if the second sentence is the "cause" or the "effect" of the first sentence.

    Parameters:
        first_sentence (str): first Indonesian sentence
        second_sentence (str): second Indonesian sentence

    Returns:
        str: \"cause\" or \"effect\"
    """

    # this function checks if the second sentence is the cause of the first one
    if is_cause(first_sentence, second_sentence):
        return "cause"
    else:
        return "effect"


# program
{
    "method": "cause_effect_classification",
    "arguments": {
        "first_sentence": "str",
        "second_sentence": "str",
    },
    "return": "str",
    "execute": "cause_effect_classification(first_sentence, second_sentence)",
}


# preprocessor
def preprocess(input: str):
    first_sentence = input.split("\n")
    second_sentence = input.split("\n")
    return first_sentence, second_sentence
