def check_semantic_similarity(sentence1: str, sentence2: str) -> str:
    """Given two sentences check if they are parapharses of each other and mean the same, if the do return "Paraphrase" else "Not paraphrase"
    Parameters:
        sentence1: Description
        sentence2: Description
    Returns:
        str: Paraphrase or Not paraphrase based on semantic similarity
    """
    return is_paraphase(sentence1, sentence2)


# program
{"method": "check_semantic_similarity", "arguments": {"sentence1": "str", "sentence2": "str"}, "return": "str", "execute": "check_semantic_similarity(sentence1,sentence2)"}


# preprocessor
def preprocess(input: str):
    sentence1 = input.split("\n")[0].strip()
    sentence2 = input.split("\n")[1].strip()
    return sentence1, sentence2
