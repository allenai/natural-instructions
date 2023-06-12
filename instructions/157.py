def count_vowels_or_consonants(text: str, pattern: str) -> int:
    """
    Counts vovels or consonants based on the value of pattern

    Parameters:
        text (str): input text
        pattern (str): vowels/consonants

    Returns:
        int: count of the pattern
    """

    vowels = ["a", "e", "i", "o", "u"]

    count = 0
    for char in text:
        if char in vowels and pattern == "vowels":
            count += 1
        elif char not in vowels and pattern == "consonants":
            count += 1

    return count


# program
{
    "method": "count_vowels_or_consonants",
    "arguments": {"text": "str", "pattern": "str"},
    "return": "int",
    "execute": "count_vowels_or_consonants(text, pattern)",
}


# preprocessor
def preprocess(input: str):
    text, pattern = input.split(" Count the number of ")
    pattern = pattern.split()[0]
    text = text.split("Sentence: ")[1]
    return text, pattern
