def generate_hypothesis_status(premise: str, hypothesis: str, update: str) -> str:
    """Given three sentences: premise, hypothesis and update where premise represents a real-world scenario and is always true, hypothesis represents an assumption and update gives additional information about the premise that might weaken or strengthen the hypothesis. Return with 'strengthener' if the update strengthens the hypothesis else return 'weakener'.
    Parameters:
        premise: sentence representing real-world scenario
        hypothesis: sentence representing an assumption
        update: sentence gives additional information about the prmise
        Returns:
                str: answer to the question
    """

    # get the strength about the hypothesis
    answer = get_hypothesis_status(premise, hypothesis, update)

    # return the answer
    return answer


# program
{
    "method": "generate_hypothesis_status",
    "arguments": {"premise": "str", "hypothesis": "str", "update": "str"},
    "return": "str",
    "execute": "generate_hypothesis_status(premise, hypothesis, update)",
}


# preprocessor
def preprocess(input: str):
    premise = input.split("Update:")[0].split("Hypothesis:")[0].split("Premise:")[1].strip()
    hypothesis = input.split("Update:")[0].split("Hypothesis:")[1].strip()
    update = input.split("Update:")[1].strip()
    return premise, hypothesis, update
