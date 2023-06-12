def classify_agreement(sentence1: str, sentence2: str) -> str:
    """Given two senteces, check if both the sentences clearly agree, disagree or netural. If they agree return "E", if they disargee return "C" else return "N"
    Parameters:
        sentence1 : first sentence
        sentence2 : second sentence
        Returns:
                str: return 'E' if two sentences entail each other, 'C' if if two sentences contradiction and 'N' if it cannot be determined.
    """

    # return E if there are agreement among the sentences
    if is_sentences_in_agreement(sentence1, sentence2):
        return "E"
    # check for disagreement between the sentences and return C if true
    elif is_sentences_in_contradiction(sentence1, sentence2):
        return "C"
    else:
        # return N if it cannot be determined or neutral
        return "N"

    # return the answer
    return answer


# program
{
    "method": "classify_agreement",
    "arguments": {
        "sentence1": "str",
        "sentence2": "str",
    },
    "return": "str",
    "execute": "classify_agreement(sentence1, sentence2)",
}


# preprocessor
def preprocess(input: str):
    sentence1 = input.split("<sep>")[0].strip()
    sentence2 = input.split("<sep>")[1].strip()
    return sentence1, sentence2
