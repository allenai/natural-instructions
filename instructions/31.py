def create_question_with_single_blank_given_context(context_word: str) -> str:
    """
    Return a question that is 15-30 words long, created using the given context word, and have only one blank. The question should not have potentially explicit, offensive, or adult content and not use animals and proper nouns as objects.
    The generated question should have two related but different objects. The two objects must agree in number and should be used only once in the question.
    The expected answer should be one of the objects in the sentence, based on the context in the question. The answer should not be associated with a specific word in the question and should not be ambiguous.

    Parameters:
        context_word: word that should be used as the context for the question to be generated

    Returns:
        str: question at least 15 and at most 30 words created based on the context that contains a blank with two related but different objects and one of which can fill the blank.
    """

    attribute_trigger_words_tuple = [
        {"age", "old", "new"},
        {"altitude", "low", "high"},
        {"area", "small", "vast"},
        {"brightness", "dark", "light"},
        {"clarity", "obscure", "clear"},
        {"cleanness", "dirty", "clean"},
        {"complexity", "simple", "complex"},
        {"cost", "cheap", "expensive"},
        {"density", "sparse", "dense"},
        {"depth", "shallow", "deep"},
        {"distance", "near", "far", ""},
        {"electric conductivity", "low", "high"},
        {"flexibility", "rigid", "flexible"},
        {"granularity", "fine", "coarse"},
        {"hardness", "soft", "hard"},
        {"length", "short", "long"},
        {"magnitude", "small", "large"},
        {"mass", "small", "large"},
        {"odor", "weak", "strong"},
        {"pressure", "low", "high"},
        {"resistance", "low", "high"},
        {"shape", "round", "sharp"},
        {"shape", "flat", "spiky"},
        {"size", "small", "large"},
        {"sound", "quiet", "loud"},
        {"sound pitch", "low", "high"},
        {"speed", "slow", "fast"},
        {"stability", "unstable", "stable"},
        {"strength", "weak", "strong"},
        {"temperature", "low", "high"},
        {"texture", "smooth", "rough"},
        {"thermal conductivity", "low", "high"},
        {"thickness", "thin", "thick"},
        {"volume", "small", "large"},
        {"weight", "light", "heavy"},
        {"width", "narrow", "wide"},
        {"location", "in", "out"},
        {"location", "up", "down"},
        {"location", "above", "below"},
        {"location", "on", "off"},
        {"location", "to", "from"},
    ]

    # select random attribute and trigger word pair
    select_trigger = random.int(len(attribute_trigger_words_tuple) - 1)

    # get an attribute
    attribute = attribute_trigger_words_tuple[select_trigger][0]

    # get trigger word
    trigger_word = attribute_trigger_words_tuple[select_trigger][1]

    # get constrastive trigger word
    constrastive_trigger_word = attribute_trigger_words_tuple[select_trigger][2]

    # this function returns two objects which exhibits the attribute specified. The objects should not be animals or proper names
    object_1, object_2 = get_two_objects(attribute=attribute, is_related=True, same_object=False, is_proper_noun=False, is_animal=False)

    # generate a sentence containing the context_word, the attribute, object_1, object_2, and, the trigger_word. The sentence should not contain explicit, adult or offensive content
    sentence_1 = generate_full_sentence_using_words(
        context_word,
        attribute,
        object_1,
        object_2,
        trigger_word,
        min_sentence_length=15,
        max_sentence_length=30,
        has_explicit_content=False,
        has_adult_content=False,
        has_offensive_content=False,
    )

    # generate question i.e, sentence with one word blanked, and return the blanked word along with the question. The blanked word should be one of the two objects. The blanked word should not be ambiguous and must be between 15 to 30 words.
    return get_blanked_question(sentence_1, object_1, object_2, is_blank_word_ambiguous=False)


# program
{
    "method": "create_question_with_single_blank_given_context",
    "arguments": {
        "context_word": "str",
    },
    "return": "str",
    "execute": "create_question_with_single_blank_given_context(context_word)",
}


# preprocessor
def preprocess(input: str):
    context_word = input.split("Context word: ")[-1][:-1]

    return context_word
