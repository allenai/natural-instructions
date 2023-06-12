def remove_non_primes_from_list(numbers_list: list[int]) -> list[int]:
    """
    Exclude non-primes from a list of numbers and retain only prime numbers.

    Parameters:
        numbers_list (str): list of numbers

    Returns:
        list[int]: list of only primes
    """

    prime_numbers = []
    for number in numbers_list:
        # check if the number is prime
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


# program
{
    "method": "remove_non_primes_from_list",
    "arguments": {"numbers_list": "list[int]"},
    "return": "list[int]",
    "execute": "remove_non_primes_from_list(numbers_list)",
}


# preprocessor
def preprocess(input: str):
    numbers_list = input
    return numbers_list
