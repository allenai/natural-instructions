def summarize_news(news_articles: list) -> str:
    """
    Given a several news articles in English language, summarize them

    Parameters:
        news_articles (list): several news articles

    Returns:
        str: summary
    """

    # This functions takes as input several news articles and summarizes them
    return summarize(news_articles)


# program
{
    "method": "summarize_news",
    "arguments": {
        "news_articles": "list",
    },
    "return": "str",
    "execute": "summarize_news(news_articles)",
}


# preprocessor
def preprocess(input: str):
    news_articles = input.split("|||||")
    return news_articles
