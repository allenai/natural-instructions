def create_sentence_pair_answer(context_word: str) -> str:
    """
    Given a context word, the task is to create pair of sentences. The sentence pair should contain blank and the answer for that blank should be generated. The sentence pair should a) look similar b) be about two related but different objects. The sentence pairs should have different trigger words i.e, words which express contrasting features of the objects. The answer must not be associated with the trigger word but, instead depend on the context present in the sentence. Answers whould not be ambiguous. The sentence pairs should not have potentially explicit, offensive, or adult content. The sentence pairs should not use animals and proper nouns as objects. There should be diversity in the sentence pair. The sentence pair should contain at least 15 and at max 30 words. The sentence pairs should have at least 70% overlapping words. There should only one blank in each of the sentence. The two objects must agree in number.

    Parameters:
        context_word (str): context_word

    Returns:
        str: two sentences and answer for them
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

    # generate blanked sentence and return the blanked word. The blanked word should not be ambiguous
    blank_word_1, blanked_sentence_1 = get_blanked_sentence(sentence_1, is_blank_word_ambiguous=False)

    # generate another sentence containing the context_word, the attribute, object_1, object_2, and, the trigger_word but different from sentence_1. The generated sentence has at least 70% overlapping words with the sentence_1.  The sentence should not contain explicit, adult or offensive content
    sentence_2 = generate_different_full_sentence_using_words(
        sentence_1,
        context_word,
        attribute,
        object_1,
        object_2,
        contrastive_trigger_word,
        min_sentence_length=15,
        max_sentence_length=30,
        has_overlap_percentage=0.7,
        has_explicit_content=False,
        has_adult_content=False,
        has_offensive_content=False,
    )

    # generate blanked sentence and return the blanked word. The blanked word should not be ambiguous
    blank_word_2, blanked_sentence_2 = get_blanked_sentence(sentence_2, is_blank_word_ambiguous=False)

    return "Sentence 1: " + blanked_sentence_1 + " \nAnswer1: " + blank_word_1 + ". \nSentence 2: " + blanked_sentence_2 + " \nAnswer2: " + blank_word_2 + "."


# program
{
    "method": "create_sentence_pair_answer",
    "arguments": {
        "context_word": "str",
    },
    "return": "str",
    "execute": "create_sentence_pair_answer(context_word)",
}


# preprocessor
def preprocess(input: str):
    context_word = input.split("Context word: ")[-1][:-1]

    return context_word
