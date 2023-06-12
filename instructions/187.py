def generate_contradiction(sentence1: str, sentence2: str) -> str:
    """Given two sentences, sentence1 and sentence2 where sentence2 agrees sentence1, modify sentence 2 such that it should contradicts sentence1. Pronouns should be avoided and new information can be added to generate the sentence. Make sure that new generated sentence is should not be more that 15 words.
    Parameters:
        sentence1: first sentence
        sentence2: second sentence
        Returns:
                str:answer to the question
    """

    # modify the second sentence
    new_sentence2 = get_contradictory_sentence(sentence1, sentence_to_modify=sentence2)

    # return the answer
    return new_sentence2


# program
{
    "method": "generate_contradiction",
    "arguments": {
        "sentence1": "str",
        "sentence2": "str",
    },
    "return": "str",
    "execute": "generate_contradiction(sentence1,sentence2)",
}


# preprocessor
def preprocess(input: str):
    sentence2 = input.split("Sentence 2:")[0].split("Sentence 1:")[1].strip()
    sentence1 = input.split("Sentence 2:")[1].strip()
    return sentence1, sentence2
