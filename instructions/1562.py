def paraphrase_question(question: str) -> str:
    """
    Given a question, paraphrase it to have different wording. The paraphrased question should have the same answer as the given question. The question can be rephrased using synonyms and/or rearranging the structure of the sentence. The questions are in three domains: a) presidents, b) national parks, and c) dogs. Each question has a keyword indicating its domain. Keywords are \"this national park\", \"this dog breed\", and \"this president\", which will be replaced with the name of an actual president, a national park, or a breed of dog. During paraphrasing the keyword should also be used the same way. Do not write open-ended or subjective questions (e.g., questions that can be answered differently by different people.) The question should be specific and concrete. The question should have the same type of answer as the original question(e.g., if the question is extractive, the paraphrased question should be extractive as well.)

    Parameters:
        question (str): a given question

    Returns:
        str: paraphrased question
    """

    domains = ["presidents", "national parks", "dogs"]

    domain_keyword_mapping = {
        "presidents": "this president",
        "national parks": "this national park",
        "dogs": "this dog breed",
    }

    # this function identifies the domain of the question from a given list of domains.
    question_domain = get_domain(question, domains)

    question_keyword = domain_keyword_mapping[question_domain]

    # this function paraphrases the given question such that the domain is the same. The paraphrased question should have the same answer. It uses the keyword provided. The paraphrased question will have the same type of answer as the original question.
    paraphrased_question = get_paraphrase(question, domain=question_domain, use_keyword=question_keyword, open_ended_answer=False, subjective_answer=False, answer_type="same", answer="same")

    return paraphrased_question


# program
{
    "method": "paraphrase_question",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "paraphrase_question(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
