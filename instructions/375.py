def classify_sentence(sentence: str, topic: str) -> str:
    """In this task, you will be given a debate topic, along with a sentence from the debate. You should classify the given sentence and choose the type of that sentence. Possible types are explained below.\nPolicy: This refers to a sentence proposing a specific course of action to be taken. It typically contains modal verbs like \"should\" and \"ought to\". It cannot be directly proved with objective evidence, and a proper type of support is a logical reason from which the proposition can be inferred.\nValue: This refers to a sentence containing value judgments without making specific claims about what should be done (If so, then it is a Policy sentence.). Because of the subjectivity of value judgments, it cannot be proved directly with objective evidence.\nFact: This refers to an objective proposition expressing or dealing with facts or conditions as perceived without distortion by personal feelings, prejudices, or interpretations. A Fact sentence has a truth value that can be verified with objective evidence that may be available at the time the claim is made; predictions about future are considered unverifiable.\nTestimony: This refers to an objective sentence about the author's personal state or experience. Evidence for Testimony is not publicly available in most cases."

    Parameters:
        text: text with marked element around a number

    Returns:
        str: label for marked element
    """

    class_labels = ["Policy", "Value", "Fact", "Testimony"]

    # Description of Policy label
    policy_description = 'This refers to a sentence proposing a specific course of action to be taken. It typically contains modal verbs like "should" and "ought to". It cannot be directly proved with objective evidence, and a proper type of support is a logical reason from which the proposition can be inferred'

    # Description of Value Label
    value_description = "This refers to a sentence containing value judgments without making specific claims about what should be done (If so, then it is a Policy sentence.). Because of the subjectivity of value judgments, it cannot be proved directly with objective evidence."

    # Description of Fact Label
    fact_description = "This refers to an objective proposition expressing or dealing with facts or conditions as perceived without distortion by personal feelings, prejudices, or interpretations. A Fact sentence has a truth value that can be verified with objective evidence that may be available at the time the claim is made; predictions about future are considered unverifiable."

    # Description of Testimony Label
    testimony_description = "This refers to an objective sentence about the author's personal state or experience. Evidence for Testimony is not publicly available in most cases."

    # Check if sentence is a policy
    if is_policy(sentence, policy_description):
        return class_labels[0]
    # Check if sentence is a Value judgement
    elif is_value(sentence, value_description):
        return class_labels[1]
    # Check if sentence is a Fact
    elif is_fact(sentence, fact_description):
        return class_labels[2]
    else:
        return class_labels[3]


# program
{
    "method": "classify_sentence",
    "arguments": {"sentence": "str", "topic": "str"},
    "return": "str",
    "execute": "classify_sentence(sentence,topic)",
}

# preprocessor
def preprocess(input: str):
    sentence = input.split("sentence:")[1].strip()
    topic = input.split("sentence:")[0].split("topic:")[1].strip()
    return sentence, topic
