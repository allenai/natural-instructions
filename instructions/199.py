def check_sentences_agreement(sentence1: str, sentence2: str) -> str:
    """Given two sentences return yes if they agree/disagree with each other, or no if this can't be determined.
    Parameters:
        sentence1: Description
        sentence2: Description
    Returns:
        str:yes or no based on determination of agreement/disagreement
    """

    # return True if the two sentences agree with each other
    if sentences_agree(sentence1, sentence2):
        return "yes"
    else:
        return "no"


# program
{"method": "check_sentences_agreement", "arguments": {"sentence1": "str", "sentence2": "str"}, "return": "str", "execute": "check_sentences_agreement(sentence1,sentence2)"}


# preprocessor
def preprocess(input: str):
    sentence1 = input.split("Sentence 2: ")[0].split("Sentence 1: ")[1].strip()
    sentence2 = input.split("Sentence 2: ")[1].strip()
    return sentence1, sentence2
