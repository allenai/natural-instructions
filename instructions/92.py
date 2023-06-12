def check_if_prime(number: int) -> str:
    """Output 'Yes' if the given number is a prime number otherwise output 'No'. A 'prime number' is a a whole number above 1 that can not be made by multiplying other whole numbers."
    Parameters:
        number: number to be checked

    Returns:
        str:'yes' if number is a prime number, else no.
    """
    # check if number is a prime number
    if is_prime(number):
        return "yes"
    else:
        return "no"


# program
{
    "method": "check_if_prime",
    "arguments": {
        "number": "int",
    },
    "return": "str",
    "execute": "check_if_prime(number)",
}


# preprocessor
def preprocess(input: str):
    number = input
    return number
