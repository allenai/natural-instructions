def order_sentences_given_story_title(sentences: list, title: str) -> int:
    """
    Given the title of a story and five sentences forming the story numbered from 1 through 5. Find two sentences which needs to swapped. On swapping the two sentences, the sequence of sentences should make sense and fit the story title.

    Parameters:
        sentences (list): List of five sentences forming a story
        title (str): the title of the story

    Returns:
        int: two sentences numbers which need to be swapped
    """

    # find two sentences which when swapped the story fits the title
    first_sentence, second_sentence = find_sentences_to_be_swapped(sentences, title=title, return_sentence_numbers=True)
    return str(first_sentence) + str(second_sentence)


# program
{
    "method": "order_sentences_given_story_title",
    "arguments": {
        "sentences": "list",
        "title": "str",
    },
    "return": "int",
    "execute": "order_sentences_given_story_title(sentences, title)",
}


# preprocessor
def preprocess(input: str):
    title = input.split("Sentence 1: '")[0].split("Title: ")[1]
    sentence_1 = input.split("Sentence 2: ")[0].split("Sentence 1: ")[-1]
    sentence_2 = input.split("Sentence 3: ")[0].split("Sentence 2: ")[-1]
    sentence_3 = input.split("Sentence 4: ")[0].split("Sentence 3: ")[-1]
    sentence_4 = input.split("Sentence 5: ")[0].split("Sentence 4: ")[-1]
    sentence_5 = input.split("Sentence 5: ")[-1]
    sentences = [sentence_1, sentence_2, sentence_3, sentence_4, sentence_5]
    return sentences, title
