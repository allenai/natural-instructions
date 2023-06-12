def update_middle_sentence_of_story_to_make_implausible(beginning: str, middle: str, ending: str) -> str:
    """Given a three-part story, with a beginning, middle, and ending, modify the middle part, so that the whole story becomes unlikely, improbable, or inconsistent. Generated sentences must minimally alter the given middle, with at most 4 new words added/existing words removed. Modified entence should be grammatically and syntactically correct and needs to stick to the context of the given story. Modified sentence should not just be a negation of the original sentence.

    Parameters:
        beginning: opening sentence of the story
        middle: middle sentence of the story
        ending: end sentence of the story

    Returns:
        str:updated story after modifying the middle
    """

    # initialize variable for context consistency checking
    is_topic_context_retained = False
    while not is_topic_context_retained:
        # Create implausible story by modifying to a create a grammatically and syntactically valid sentence with upto a maximum of 4 new words. Negation of original sentence is not allowed.
        updated_middle = modify_sentence_to_make_implausible(sentence=middle, max_new_words=4, do_not_negate=True, retain_topic_context=True, grammatical=True)
        # check if context consistency is retained
        is_topic_context_retained = check_topic_context_alignment_across_sentences(beginning + updated_middle + ending)
        # if updated_middle is valid, return updated middle sentence
        if is_topic_context_retained:
            return updated_middle

    return updated_middle


# program
{
    "method": "update_middle_sentence_of_story_to_make_implausible",
    "arguments": {
        "beginning": "str",
        "middle": "str",
        "ending": "str",
    },
    "return": "str",
    "execute": "update_middle_sentence_of_story_to_make_implausible(beginning,middle,ending)",
}


# preprocessor
def preprocess(input: str):
    beginning = input.split("Middle:")[0].strip().split("Beginning:")[1].strip()
    middle = input.split("Middle:")[1].strip().split("Ending:")[0].strip()
    ending = input.split("Ending:")[1].strip()
    return beginning, middle, ending
