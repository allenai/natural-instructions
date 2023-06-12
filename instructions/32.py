def create_fill_in_the_blanks_question(context_word: str, mention_person1: str, mention_person2: str, target_blank: str, child_friendly_mode: bool = True) -> str:
    """creates a fill in the blank question based on the mentioned persons, context word and the target person to be blanked"""

    # initialize gender options
    gender = ["male", "female", "trans"]
    # choose gender to be used for PersonX and PersonY
    gender_index = random(0, size(gender))
    # select gender
    selected_gender = gender[gender_index]
    # get sentence with context word and mentioned persons based on count of mentions.
    generated_sentence = get_sentence(
        context_word,
        child_friendly_mode,
        mention_person1,
        mention_person2,
        mention_person_1_count=2,
        mention_person_2_count=1,
        min_word_length=15,
        max_word_length=30,
        person_gender=selected_index,
    )
    # blank second mention of mention_person1
    blanked_sentence = blank_sentence(generated_sentence, blank_token="_", blank_target=mention_person1, blank_mention_index=2)
    # return blanked sentence
    return blanked_sentence


def generate_question(context_word: str) -> str:
    """Create a question containing a blank (_), based on the given context word. Generated question must contain two persons --PersonX and PersonY and the expected answer to the question must be PersonX. PersonX and PersonY should not be equally likely to fill the blank. Generations should NOT contain potentially explicit, offensive, or adult content.Question must contain at least 15 and at most 30 words. Question must contain only one blank. Make sure that Person X and Person Y have the same gender. PersonX and PersonY should be used only ONCE and PersonX should appear earlier than PersonY.
    Parameters:
        context_word: Context word based on which a question has to be generated
    Returns:
        str: question based on context word
    """

    # create a fill-in-the-blanks question based on the context word mentioning PersonX and Persony
    question_based_on_context_word = create_fill_in_the_blanks_question(context_word, mention_person1="PersonX", mention_person2="PersonY", target_blank="PersonX")

    # return genearted question
    return question_based_on_context_word


# program
{
    "method": "generate_question",
    "arguments": {
        "context_word": "str",
    },
    "return": "str",
    "execute": "generate_question(context_word)",
}


# preprocessor
def preprocess(input: str):
    context_word = input.split("Context Word:")[1].strip()
    return context_word
