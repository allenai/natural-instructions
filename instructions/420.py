def detect_entity_sentitment(document: str) -> str:
    """Identify the entity discssused in the document and classify the sentiment expressed as Positive, Neutral or Negative.
    Parameters:
        document: passage expressing sentiment about an entity of target
    Returns:
        str: entity sentiment
    """
    entity = detect_discussed_entity_from_document(document)
    sentiment = detect_entity_sentiment(document, entity)
    if sentiment == "positive":
        if is_positivequotes_from_others(document, entity) or has_equal_positive_negative_sentiment(document, entity):
            return "Neutral"
        else:
            return "Positive"
    elif sentiment == "Negative":
        if is_negativequotes_from_others(document, entity) or has_equal_positive_negative_sentiment(document, entity):
            return "Neutral"
        else:
            return "Negative"
    return sentiment


# program
{"method": "detect_entity_sentitment", "arguments": {"document": "str"}, "return": "str", "execute": "detect_entity_sentitment(document)"}


# preprocessor
def preprocess(document: str):
    return document
