def is_edited_news_headline_funny(headline: str, original_word: str, edited_word: str) -> str:
    """
    Given news headlines and an edited word. The original sentence has word within given format {word}. Create new headlines by replacing {word} in the original sentence with edit word. Classify news headlines into \"Funny\" and \"Not Funny\" that have been modified by humans using an edit word to make them funny.

    Parameters:
        headline (str): a news headline
        edited_word (str): word to be replaced in the headline

    Returns:
        str: \"Funny"\ or \"Not Funny\"
    """

    # this function takes in a text, the word to be replaced and the word replacing. Replaces the word to be replaced with the word replacing
    replaced_headline = replace(text=headline, word_to_be_replaced=original_word, replacement_word=edited_word)

    # this function checks if the given text is funny or not
    if is_funny(text=replaced_headline):
        return "Funny"
    else:
        return "Not Funny"


# program
{
    "method": "is_edited_news_headline_funny",
    "arguments": {
        "headline": "str",
        "original_word": "str",
        "edited_word": "str",
    },
    "return": "str",
    "execute": "is_edited_news_headline_funny(headline, original_word, edited_word)",
}


# preprocessor
def preprocess(input: str):
    headline = input.split("Edit:")[0].strip()
    original_word = headline.split("}")[0].split("{")[-1]
    edited_word = input.split("Edit:")[-1].strip()
    return headline, original_word, edited_word
