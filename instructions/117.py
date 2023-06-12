def translate_english_to_german(sentence: str) -> str:
    """
    Given an inquiry about the restaurants in English, translate it to German language. The translation should be formal and should not contain any colloquial forms of the sentence. Words between quotation marks are named entities and should not be translated. The named entities in the translation should include quotation marks. Fully capitalized words should not be translated and retained in the translation as is. The measurement units should not be localized and kept as is. The translation should be in lowercase except for the above special token mentioned

    Parameters:
        sentence (str): An English query about a restaurant

    Returns:
        str: The corresponding translation in German
    """

    # function which translates a given English sentence to german
    translated_sentence = translate_from_english_to_german(sentence)

    # this function takes in a German sentence as input formalizes the sentence if it contains any colloquial form
    formalize_sentence = formalize_german_sentence(translated_sentence)

    # this function first identifies the named entities in the source sentence, checks if the named entities are translated or not. If the named entities are translated converts the translated form to the original form from the source sentence
    formalize_sentence_with_named_entities = retain_named_entities(formalize_sentence, sentence)

    # this function adds quotes around named entities if not present
    formalize_sentence_with_named_entities_quotes = add_quotes_named_entities(formalize_sentence_with_named_entities)

    # this function looks at capitalized words in the source sentence, if they are translated then they would be converted to the original form from the source sentence
    formalize_sentence_with_capital_entity_quotes = retain_captalized_words(formalize_sentence_with_named_entities_quotes, sentence)

    # this function looks for measurements in the source sentence, if they are localized in the translation, they would be converted to the original form from the source sentence
    formalize_sentence_with_capital_entity_quotes_measurements = retain_measurements(formalize_sentence_with_capital_entity_quotes, sentence)

    # this function lowercased all words except for special tokens in the translation
    final_translation = lowercase_non_special_tokens(formalize_sentence_with_capital_entity_quotes_measurements)

    return final_translation


# program
{
    "method": "translate_english_to_german",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "translate_english_to_german(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
