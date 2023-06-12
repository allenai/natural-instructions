def check_entity_sentiment(sentence: str) -> str:
    """Given a sentence, extract the entity, sentiment expected and document. If the sentiment towards the given entity then return "yes" or "no"
    Parameters:
        sentence: input sentences containg entity and the related document.
        Returns:
                str:answer to the question
    """

    # get the entity
    entity = extract_entity(sentence)

    # get the sentiment
    sentiment_to_verify = extract_sentiment_to_verify(sentence)

    # get the document describing the sentiment
    document = extract_document(sentence)

    # check the sentiment
    sentiment = get_sentiment(entity, document)

    # check if the sentiment towards the entity is expected,
    if sentiment_to_verify == sentiment:
        return "yes"
    else:
        return "no"


# program
{
    "method": "check_entity_sentiment",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "check_entity_sentiment(sentence)",
}


# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
