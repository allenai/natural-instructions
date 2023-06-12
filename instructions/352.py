def classify_sentences_in_paragraph(paragraph: str) -> str:
    """Given a paragraph (from a research paper), classify each sentence of the paragraph (assume n sentence) into the following categories: Background, Purpose, Method, Finding/Contribution, or Other. Return the output in this format: 1 - category of sentence 1, 2 - category of sentence 2, ..., n - category of sentence n; where each number indicates the order of the sentence. The categories can be identified using the following questions: \n Background: - Why is this problem important? - What relevant works have been done before? - What did the previous works miss? - What are the high-level research questions? - How might this help other researchers?\n Purpose: - What specific things do the researchers want to do? - What specific knowledge do the researchers want to know? - What specific hypothesis do the researchers want to test?\n Method: - How did the researchers do it or find it out? - What are the procedures and steps of this research?\n Finding/Contribution: - What did the researchers find out? Did the proposed methods work? - Did things behave as the researchers expected?\nOther: put every text fragment that does not fit into any of the categories above here. Put a sentence here if its not in English, is not part of the article, contains numbers and dates, is a caption of a figure or a table, is a formatting error, or you are not sure about it..

    Parameters:
        paragraph: paragraph whose sentences need to be labeled

    Returns:
        str: containing the index of each sentence along with its label
    """

    # list of classes
    class_labels = ["background", "purpose", "method", "finding", "other"]

    # get list of sentences from paragraph
    sentences = get_sentences(paragraph)

    # prepare string to return class labels
    return_string = ""

    for index, sentence in enumerate(sentences):
        # classifiy each sentence in paragraph
        class_label = classify_sentence(sentence, class_labels)
        # get sentence number
        sentence_number = index + 1
        # update return string with class label of current sentence
        return_string = return_string + sentence_number + " - ", class_label + " ,"

    # Return string with class label for each sentence
    return return_string


def classify_sentence(sentence: str, class_labels: list) -> str:
    """\n Background: - Why is this problem important? - What relevant works have been done before? - What did the previous works miss? - What are the high-level research questions? - How might this help other researchers?\n Purpose: - What specific things do the researchers want to do? - What specific knowledge do the researchers want to know? - What specific hypothesis do the researchers want to test?\n Method: - How did the researchers do it or find it out? - What are the procedures and steps of this research?\n Finding/Contribution: - What did the researchers find out? Did the proposed methods work? - Did things behave as the researchers expected?\nOther: put every text fragment that does not fit into any of the categories above here. Put a sentence here if its not in English, is not part of the article, contains numbers and dates, is a caption of a figure or a table, is a formatting error, or you are not sure about it..

    Parameters:
        sentence: sentence to be classified

    Returns:
        str: class label
    """

    # class description for background
    background_description = " Why is this problem important? - What relevant works have been done before? - What did the previous works miss? - What are the high-level research questions? - How might this help other researchers?\n"

    # class description for purpose
    purpose_description = "What specific things do the researchers want to do? - What specific knowledge do the researchers want to know? - What specific hypothesis do the researchers want to test?"

    # class description for method
    method_description = "How did the researchers do it or find it out? - What are the procedures and steps of this research?"

    # class description for finding
    finding_description = "What did the researchers find out? Did the proposed methods work? - Did things behave as the researchers expected?"

    # sentence is labeled as "other" if its not in English, is not part of the article, contains numbers and dates, is a caption of a figure or a table, is a formatting error, or you are not sure about it
    if is_english(sentence) or contains_date(sentence) or is_caption(sentence) or contains_formatting_error(sentence):
        return class_labels[4]
    else:
        # check if sentence is a background sentence
        if is_background(sentence, background_description):
            return class_labels[0]
        # check if sentence is a purpose sentence
        elif is_purpose(sentence, purpose_description):
            return class_labels[1]
        # check if sentence is a method sentence
        elif is_method(sentence, method_description):
            return class_labels[2]
        # check if sentence is a finding sentence
        elif is_finding(sentence, finding_description):
            return class_labels[3]
        else:
            # return other
            return class_labels[4]


# program
{
    "method": "classify_sentences_in_paragraph",
    "arguments": {"paragraph": "str"},
    "return": "str",
    "execute": "classify_sentences_in_paragraph(paragraph)",
}

# preprocessor
def preprocess(input: str):
    paragraph = input
    return paragraph
