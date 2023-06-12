def identify_easier_text(text_1: str, text_2: str) -> str:
    """Given two text snippets text_1, text_2, identify simpler text

    Parameters:
        text_1: First input text
        text_2: Second input text
    Returns:
        str: Text One or Text Two
        'Text one' if text_1 is simpler than text_2; otherwise 'Text two'
    """

    if is_simpler(text_1, text_2) == "text_1":  # text_1 is simpler than text_2
        return "Text one"
    else:  # text_2 is simpler than text_1
        return "Text two"


# program
{
    "method": "identify_easier_text",
    "arguments": {
        "text_1": "str",
        "text_2": "str",
    },
    "return": "str",
    "execute": "identify_easier_text(text_1,text_2)",
}


# preprocessor
def preprocess(input: str):
    text_1 = input.split("Text two:")[0].split("Text one:")[1].strip()
    text_2 = input.split("Text two:")[1].strip()
    return text_1, text_2
