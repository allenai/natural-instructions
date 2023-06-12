def generate_headline_for_article(article: str) -> str:
    """
    Generates a headline for an article.

    Parameters:
        article (str): a piece of text for which to generate a headline

    Returns:
        str: headline for the article
    """

    # returns a headline for the article which can be obtained from the summary
    return headline(article)


# program
{
    "method": "generate_headline_for_article",
    "arguments": {"article": "str"},
    "return": "str",
    "execute": "generate_headline_for_article(article)",
}


# preprocessor
def preprocess(input: str):
    article = input
    return article
