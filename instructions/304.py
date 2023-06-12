def label_marked_element(text: str) -> str:
    """In this task, you will use your knowledge about language (and common sense) to determine what element the marked number refers to. The numbers are marked with two underlines around them, like: _ number _. There are several possible answers, you'll need to choose the proper one. Carefully read the given text, pay special attention to the marked number, think about what (unwritten) information the marked number holds inside, choose the most adequate word(s) from the optional answers. If none of them seems right to you, there's also an option for other. If your answer is \"REFERENCE\", also write the reference entity, otherwise write the implicit option name. Options to choose from are:\nREFERENCE: Some object which is being mentioned in the text before or after the target number. The reference answer has a higher priority than any other. If both Reference and another answer are possible, prioritize the Reference.\nYEAR: Describing a calendric year\nAGE: Describing someone's age\nCURRENCY: Reference to some monetary value e.g dollar, euro etc.\nPEOPLE: Describing a single/plural persons\nTIME: Describing a time of the day. Usually you can add the word o'clock after those numbers.\nOTHER: Some other option, which isn't listed here.

    Parameters:
        text: text with marked element around a number

    Returns:
        str: label for marked element
    """

    # get marked element(s)
    element = get_marked_element(text, marker_token="_")

    # Description of REFERENCE
    reference_description = "Some object which is being mentioned in the text before or after the target number."

    # Description of AGE
    age_description = "Describing someone's age"

    # Descriotion of CURRENCY
    currency_description = "Reference to some monetary value e.g dollar, euro etc."

    # Description of PEOPLE
    people_description = "Describing a single/plural persons"

    # Description of TIME
    time_description = "Describing a time of the day. Usually you can add the word o'clock after those numbers."

    # If both Reference and another answer are possible, prioritize the Reference
    if is_reference(element, reference_description):
        # If answer is \"REFERENCE\", also write the reference entity, otherwise write the implicit option name.
        entity = get_reference_entity(element)
        return "REFERENCE" + " " + entity
    elif is_age(element, age_description):
        return "AGE"
    elif is_currency(element, currency_description):
        return "CURRENCY"
    elif is_people(element, people_description):
        return "PEOPLE"
    elif is_time(element, time_description):
        return "TIME"
    else:
        return "OTHER"


# program
{
    "method": "label_marked_element",
    "arguments": {
        "text": "str",
    },
    "return": "str",
    "execute": "label_marked_element(text)",
}

# preprocessor
def preprocess(input: str):
    text = input
    return text
