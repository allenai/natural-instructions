def abuse_detection(text: str) -> str:
    """
    Given a text identify if the text contains abusive content or not. For abusive content return "yes" otherwise "no".

    A text is considered abusive if it contains any of the following:
    1) Content which contains a negative statement made against an identity. An identity is a social category that relates to a fundamental aspect of individuals community, socio-demographics, position or self-representation
    2) Content which express negativity against an affiliation. We define affiliation as a (more or less) voluntary association with a collective. Affiliations include but are not limited to: memberships (e.g. Trade unions), party memberships (e.g. Republicans), political affiliations (e.g. Right-wing people) and occupations (e.g. Doctors).)
    3) Content which directs negativity against an identifiable person, who is either part of the conversation thread or is named. Person-directed abuse includes serious character based attacks, such as accusing the person of lying, as well as aggression, insults and menacing language.)
    4) Content which challenges, condemns or calls out the abusive language of others.

    Parameters:
        text (str): text

    Returns:
        str: story
    """

    # this function checks if the text contains content which has a negative statement made against an identity. An identity is a social category that relates to a fundamental aspect of individuals community, socio-demographics, position or self-representation. If yes return True else return False
    if is_negative_statement_against_identity(text):
        return "yes"
    # this function checks if the text contains content which has a negative statement against an affiliation. We define affiliation as a (more or less) voluntary association with a collective. Affiliations include but are not limited to: memberships (e.g. Trade unions), party memberships (e.g. Republicans), political affiliations (e.g. Right-wing people) and occupations (e.g. Doctors).
    elif is_negative_statement_against_affilitaion(text):
        return "yes"
    # this function checks if the text contains content which directs negativity against an identifiable person, who is either part of the conversation thread or is named. Person-directed abuse includes serious character based attacks, such as accusing the person of lying, as well as aggression, insults and menacing language.
    elif is_negative_statement_against_person(text):
        return "yes"
    # this function checks if the text contains content which challenges, condemns or calls out the abusive language of others.
    elif is_counter_speech(text):
        return "yes"
    else:
        return "no"


# program
{
    "method": "abuse_detection",
    "arguments": {
        "text": "str",
    },
    "return": "str",
    "execute": "abuse_detection(text)",
}


# preprocessor
def preprocess(input: str):
    text = input

    return text
