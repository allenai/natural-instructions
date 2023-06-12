def story_sentence_generation(sentences: list) -> str:
    """
    Given four sentences of a story the task is to generate the appropriate last sentence. The generated sentence should be coherent with the given sentence

    Parameters:
        sentences (list): four sentences forming the story

    Returns:
        str: A sentence which completes the story
    """

    # function which completes a story by generating a single sentence given the list of sentences forming the bulk of the story
    last_sentence = complete_story(sentences)

    return last_sentence


# program
{
    "method": "story_sentence_generation",
    "arguments": {
        "sentences": "list",
    },
    "return": "str",
    "execute": "story_sentence_generation(sentences)",
}


# preprocessor
def preprocess(input: str):
    sentence_1 = input.split("Sentence2")[0].split("Sentence1: ")[-1]
    sentence_2 = input.split("Sentence3")[0].split("Sentence2: ")[-1]
    sentence_3 = input.split("Sentence4")[0].split("Sentence3: ")[-1]
    sentence_4 = input.split("Sentence4: ")[-1]
    sentences = [sentence_1, sentence_2, sentence_3, sentence_4]
    return sentences
