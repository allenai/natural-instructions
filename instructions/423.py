def verify_doc_sentiment(sentences: str) -> str:
    """Check the sentiment towards the given entity. The answer text should be "yes" or "no"
    Parameters:
        sentences: input sentences containg entity and the related document.
        Returns:
                str:answer to the question
    """

    # get the entity
    entity = extract_target_entity(sentences)

    # get the document describing the sentiment
    document = extract_document(sentences)

    # get the sentiment stated about the entity
    sentiment = extract_stated_sentiment(sentences)

    # check the sentiment
    sentiment_answer = get_sentiment(entity, document)

    # if the extracted sentiment agrees with the actual sentiment return yes
    if sentiment == sentiment_answer:
        return "yes"
    else:
        return "no"


# program
{
    "method": "verify_doc_sentiment",
    "arguments": {
        "sentences": "str",
    },
    "return": "str",
    "execute": "verify_doc_sentiment(sentences)",
}


# preprocessor
def preprocess(input: str):
    sentences = input
    return sentences
