def generate_span_answerable_question(passage: str) -> str:
    """Generates a question in such a way that (i) it is unambiguous, (ii) it is answerable from the passage, (iii) its answer is unique (iv) its answer is a continuous text span from the paragraph. Does not create questions that (i) can be answered correctly without actually understanding the paragraph and (ii) uses same words or phrases given in the passage.

    Parameters:
        passage: passage from which questions need to be generated

    Returns:
        str: question based on the passage
    """
    # Create question that is unanswerable from a span in passage but requires a deeper understanding of the passage.
    generated_question = generate_question_from_passage(passage, type="answerable_from_span", requires_passage_understanding=True)

    return generated_question


# program
{
    "method": "generate_span_answerable_question",
    "arguments": {
        "passage": "str",
    },
    "return": "str",
    "execute": "generate_span_answerable_question(passage)",
}


# preprocessor
def preprocess(input: str):
    passage = input
    return passage
