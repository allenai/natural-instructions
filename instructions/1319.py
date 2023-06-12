def get_country_bar_code(country: str) -> str:
    """
    Given a country, return the three digit bar code prefix. If a country has multiple bar codes, return any one of them

    Parameters:
        country (str): country name

    Returns:
        str: 3 digit bar code prefix
    """

    # This functions takes in a country name and return the bar code
    bar_code = get_bar_code(country)

    # thsi function takes in a bar code and return the first three digits
    bar_code_prefix = get_first_three_digits(bar_code)

    return bar_code_prefix


# program
{
    "method": "get_country_bar_code",
    "arguments": {
        "country": "str",
    },
    "return": "str",
    "execute": "get_country_bar_code(country)",
}


# preprocessor
def preprocess(input: str):
    country = input
    return country
