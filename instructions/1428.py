def get_country_surface_area(country: str) -> str:
    """
    Given a country, return the surface area of the country in terms of square kilometers. The area should be up to two deimal places

    Parameters:
        country (str): country name

    Returns:
        float: surface area truncated to two decimal places
    """

    # This functions takes in a country name and return the surface area in floating number
    surface_area = get_surface_area(country)

    # this function takes in a floating number and truncates to two decimal places
    surface_area = round(surface_area, 2)

    return surface_area


# program
{
    "method": "get_country_surface_area",
    "arguments": {
        "country": "str",
    },
    "return": "float",
    "execute": "get_country_surface_area(country)",
}


# preprocessor
def preprocess(input: str):
    country = input
    return country
