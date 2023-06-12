def identify_agreement(sentence1: str, sentence2: str) -> str:
    """Given two senteces, return "yes" if both the sentences clearly agree with each other else return "no".
    Parameters:
        sentence1 : first sentence
        sentence2 : second sentence
        Returns:
                str: "yes" if two sentence clearly agree else "no"
    """

    # check if the two sentences agree
    if is_agreement(sentence1, sentence2):
        return "yes"
    else:
        # the two sentences disagree or cannot be determined therefore return no
        return "no"


# program
{
    "method": "identify_agreement",
    "arguments": {
        "sentence1": "str",
        "sentence2": "str",
    },
    "return": "str",
    "execute": "identify_agreement(sentence1, sentence2)",
}


# preprocessor
def preprocess(input: str):
    sentence1 = input.split("<sep>")[0].strip()
    sentence2 = input.split("<sep>")[1].strip()
    return sentence1, sentence2
