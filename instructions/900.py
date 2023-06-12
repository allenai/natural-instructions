def question_category_classification(background: str, story: str) -> str:
    """
    Given a trivia question, classify the quetsion into one of the topical categories from the list: 'theater', 'geology', 'book', 'tv', 'astronomy', 'aviation', 'military', 'government', 'boxing', 'projects', 'metropolitan_transit', 'law', 'venture_capital', 'broadcast', 'biology', 'people', 'influence', 'baseball', 'spaceflight', 'media_common', 'cvg', 'opera', 'olympics', 'chemistry', 'visual_art', 'conferences', 'sports', 'language', 'travel', 'location', 'award', 'dining', 'martial_arts', 'comic_strips', 'computer', 'user', 'tennis', 'music', 'organization', 'food', 'event', 'transportation', 'fictional_universe', 'measurement_unit', 'meteorology', 'distilled_spirits', 'symbols', 'architecture', 'freebase', 'internet', 'fashion', 'boats', 'cricket', 'film', 'medicine', 'finance', 'comic_books', 'celebrities', 'soccer', 'games', 'time', 'geography', 'interests', 'common', 'base', 'business', 'periodicals', 'royalty', 'education', 'type', 'religion', 'automotive', 'exhibitions'.

    Parameters:
        question (str): question

    Returns:
        str: category
    """

    category_list = [
        "theater",
        "geology",
        "book",
        "tv",
        "astronomy",
        "aviation",
        "military",
        "government",
        "boxing",
        "projects",
        "metropolitan_transit",
        "law",
        "venture_capital",
        "broadcast",
        "biology",
        "people",
        "influence",
        "baseball",
        "spaceflight",
        "media_common",
        "cvg",
        "opera",
        "olympics",
        "chemistry",
        "visual_art",
        "conferences",
        "sports",
        "language",
        "travel",
        "location",
        "award",
        "dining",
        "martial_arts",
        "comic_strips",
        "computer",
        "user",
        "tennis",
        "music",
        "organization",
        "food",
        "event",
        "transportation",
        "fictional_universe",
        "measurement_unit",
        "meteorology",
        "distilled_spirits",
        "symbols",
        "architecture",
        "freebase",
        "internet",
        "fashion",
        "boats",
        "cricket",
        "film",
        "medicine",
        "finance",
        "comic_books",
        "celebrities",
        "soccer",
        "games",
        "time",
        "geography",
        "interests",
        "common",
        "base",
        "business",
        "periodicals",
        "royalty",
        "education",
        "type",
        "religion",
        "automotive",
        "exhibitions",
    ]

    for category in category_list:
        # this function cheks if the question falls into the specified category. If the question falls into the specified category, the function returns True else False
        if question_category_classification(question, category):
            return category


# program
{
    "method": "question_category_classification",
    "arguments": {
        "question": "str",
    },
    "return": "str",
    "execute": "question_category_classification(question)",
}


# preprocessor
def preprocess(input: str):
    question = input
    return question
