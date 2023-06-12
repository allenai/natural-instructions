def get_outcomes(sentence: str) -> str:
    """In medical studies, treatments are tested within a group of study participants. To determine if a new treatment works, various outcomes are measured in the people who take part in the study. Given a sentence of a study report, list the phrases that give information about the outcomes of the study. You should list the phrases in the same order that they appear in the text, separated by commas. If no information about the outcome is mentioned, just answer with: \"not found\".\n Outcomes contain: outcomes measured in patients: like blood sugar,\n outcomes regarding the intervention: like effectiveness, costs\n the score on a medical test or questionnaire,\n positive or negative events in the patient groups: like quitting smoking, or adverse reactions.\n Do not mention numbers or results, interpretations of outcomes, outcome mentions without relevant information.

    Parameters:
        sentence: dialog between user and agent

    Returns:
        str: outcome phrases
    """

    # description of an outcome
    outcome_description = "outcomes measured in patients: like blood sugar,\n outcomes regarding the intervention: like effectiveness, costs\n the score on a medical test or questionnaire,\n positive or negative events in the patient groups: like quitting smoking, or adverse reactions."

    # list the phrases in the same order that they appear in the text, separated by commas. If no information about the outcome is mentioned, just answer with: "not found".Do not mention numbers or results, interpretations of outcomes, outcome mentions without relevant information.
    outcome_phrases = extract_outcome_phrases(outcome_descroption, sentence, delimiter=",", retain_mention_sequence=True, not_found_string="not found", include_numbers=False, include_results=False)

    # return extracted outcome phrases
    return outcome_phrases


# program
{
    "method": "get_outcomes",
    "arguments": {
        "sentence": "str",
    },
    "return": "str",
    "execute": "get_outcomes(sentence)",
}

# preprocessor
def preprocess(input: str):
    sentence = input
    return sentence
