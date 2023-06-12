def classify_response(prompt: str, response: str) -> str:
    """
    Given a prompt and a response, classify the response to `yes` if the response agrees with the prompt and then expand on that line of thought or context. The response is classified as `no` otherwise.

    Parameters:
        prompt (str): prompt
        response (str): response

    Returns:
        str: answer
    """

    # this function returns `yes` if the response follows the prompt and `no` if the response does not follow the prompt
    return does_response_follow_prompt(prompt, response)


# program
{
    "method": "classify_response",
    "arguments": {
        "prompt": "str",
        "response": "str",
    },
    "return": "str",
    "execute": "classify_response(prompt, response)",
}


# preprocessor
def preprocess(input: str):
    prompt = input.split("\n Response: ")[0].split("Prompt: ")[-1]
    response = input.split("Response: ")[-1]

    return prompt, response
