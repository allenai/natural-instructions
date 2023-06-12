def identify_question_category(question: str) -> str:
    """
    Given a question, identify which category better describes the question. A question belongs to the description category if it asks about description and abstract concepts. Entity questions are about entities such as animals, colors, sports, etc. Abbreviation questions ask about abbreviations and expressions abbreviated. Questions regarding human beings, description of a person, and a group or organization of persons are categorized as Human. Quantity questions are asking about numeric values and Location questions ask about locations, cities, and countries.

    The categories are: \"Description\", \"Entity\", \"Abbreviation\", \"Person\", \"Quantity\", and \"Location\"

    Parameters:
        question (str): question

    Returns:
        str: category
    """

    # this function checks if the question asks about a description or an anstract concept
    if question_asks_about_description(question):
        return "Description"
    # this function checks if the question asks about entities such as animals, colors, sports, etc.
    elif question_asks_about_entity(question):
        return "Entity"
    # this function checks if the question asks about abbreviation
    elif question_asks_about_abbreviation(question):
        return "Abbreviation"
    # this function checks if the question asks regarding human beings, description of a person, and a group or organization of persons
    elif question_asks_about_person(question):
        return "Person"
    # this function checks if the question is asking about numeric values
    elif question_asks_about_quantity(question):
        return "Quantity"
    # this function checks if the question is asking about locations, cities, and countries
    elif question_asks_about_location(question):
        return "Location"


# program
{
    "method": "identify_question_category",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "identify_question_category(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
