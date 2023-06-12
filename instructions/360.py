def generate_response(prompt: str) -> str:
    """
    Given a prompt, generate a `yes and` repsonse. `Yes, and` is a rule-of-thumb in improvisational comedy that suggests that a participant in a dialogue should accept what another participant has stated (`Yes`) and then expand on that line of thought or context (`and...`). The generation should should add new information on top of the information/setting that was constructed by another speaker.

    Parameters:
        prompt (str): prompt

    Returns:
        str: response
    """

    # this function generates a `yes and` response to the given prompt. The response should agree with the line of thought or context in the prompt and expand on that line of thought or context. The generation should should add new information on top of the information/setting that was constructed by another speaker
    return generate_response(prompt, follows_prompt=True)


# program
{
    "method": "generate_response",
    "arguments": {
        "prompt": "str",
    },
    "return": "str",
    "execute": "generate_response(prompt)",
}


# preprocessor
def preprocess(input: str):
    prompt = input
    return prompt
