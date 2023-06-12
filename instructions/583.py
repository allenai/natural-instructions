def get_POS_for_word_in_sentence(sentence: str, word: str) -> str:
    """provide the parts-of-speech tag of a word present in a sentence specified within curly braces  ( '{{ ... }}' ). The parts-of-speech tags are coarse labels that represent a category of words with similar grammatical properties. The list of part-of-speech tags i.e. tagset of this corpus is 'ADJ': Adjectives are words that typically modify nouns and specify their properties or attributes, 'ADP': Adposition is a cover term for prepositions and postpositions, 'ADV': Adverbs are words that typically modify verbs for such categories as time, place, direction or manner, 'AUX': An auxiliary is a function word that accompanies the lexical verb of a verb phrase and expresses grammatical distinctions not carried by the lexical verb, such as person, number, tense, mood, aspect, voice or evidentiality, 'CCONJ': A coordinating conjunction is a word that links words or larger constituents without syntactically subordinating one to the other and expresses a semantic relationship between them, 'DET': Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context, 'INTJ': An interjection is a word that is used most often as an exclamation or part of an exclamation, 'NOUN': Nouns are a part of speech typically denoting a person, place, thing, animal or idea, 'NUM': A numeral is a word, functioning most typically as a determiner, adjective or pronoun, that expresses a number and a relation to the number, such as quantity, sequence, frequency or fraction, 'PART': Particles are function words that must be associated with another word or phrase to impart meaning and that do not satisfy definitions of other universal parts of speech, 'PRON': Pronouns are words that substitute for nouns or noun phrases, whose meaning is recoverable from the linguistic or extralinguistic context, 'PROPN': A proper noun is a noun (or nominal content word) that is the name (or part of the name) of a specific individual, place, or object, 'PUNCT': Punctuation marks are non-alphabetical characters and character groups used in many languages to delimit linguistic units in printed text, 'SCONJ': A subordinating conjunction is a conjunction that links constructions by making one of them a constituent of the other. The subordinating conjunction typically marks the incorporated constituent which has the status of a (subordinate) clause, 'SYM': A symbol is a word-like entity that differs from ordinary words by form, function or both, 'VERB': A verb is a member of the syntactic class of words that typically signal events and actions, can constitute a minimal predicate in a clause, and govern the number and types of other constituents which may occur in the clause, 'X': The tag X is used for words that for some reason cannot be assigned a real part-of-speech category.

    Parameters:
        sentence: sentence containing the word to be labeled
        word: word whose parts-of-speech tag needs to be identified

    Returns:
        str: containing the index of each sentence along with its label
    """
    # Description of ADJ POS Tag
    adj_description = "Adjectives are words that typically modify nouns and specify their properties or attributes"

    # Description of ADV POS Tag
    adv_description = "Adverbs are words that typically modify verbs for such categories as time, place, direction or manner"

    # Description of AUX POS Tag
    aux_description = "An auxiliary is a function word that accompanies the lexical verb of a verb phrase and expresses grammatical distinctions not carried by the lexical verb, such as person, number, tense, mood, aspect, voice or evidentiality"

    # Description of CCONJ POS Tag
    cconj_description = (
        "A coordinating conjunction is a word that links words or larger constituents without syntactically subordinating one to the other and expresses a semantic relationship between them"
    )

    # Description of DET POS Tag
    det_description = "Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context"

    # Description of INTJ POS Tag
    intj_description = "An interjection is a word that is used most often as an exclamation or part of an exclamation"

    # Description of NOUN POS Tag
    noun_description = "Nouns are a part of speech typically denoting a person, place, thing, animal or idea"

    # Description of NUM POS Tag
    num_description = (
        "A numeral is a word, functioning most typically as a determiner, adjective or pronoun, that expresses a number and a relation to the number, such as quantity, sequence, frequency or fraction"
    )

    # Description of PART POS Tag
    part_description = "Particles are function words that must be associated with another word or phrase to impart meaning and that do not satisfy definitions of other universal parts of speech"

    # Description of PRON POS Tag
    pron_description = "Pronouns are words that substitute for nouns or noun phrases, whose meaning is recoverable from the linguistic or extralinguistic context"

    # Description of PROPN POS Tag
    propn_description = "A proper noun is a noun (or nominal content word) that is the name (or part of the name) of a specific individual, place, or object"

    # Description of PUNCT POS Tag
    punct_description = "Punctuation marks are non-alphabetical characters and character groups used in many languages to delimit linguistic units in printed text"

    # Description of SCONJ POS Tag
    sconj_description = "A subordinating conjunction is a conjunction that links constructions by making one of them a constituent of the other. The subordinating conjunction typically marks the incorporated constituent which has the status of a (subordinate) clause"

    # Description of SYM POS Tag
    sym_description = "A symbol is a word-like entity that differs from ordinary words by form, function or both, 'VERB': A verb is a member of the syntactic class of words that typically signal events and actions, can constitute a minimal predicate in a clause, and govern the number and types of other constituents which may occur in the clause"

    # Description of X POS Tag
    x_description = "The tag X is used for words that for some reason cannot be assigned a real part-of-speech category"

    if is_adj(sentence, word, adj_description):
        return "ADJ"
    elif is_adv(sentence, word, adv_description):
        return "ADV"
    elif is_aux(sentence, word, aux_description):
        return "AUX"
    elif is_cconj(sentence, word, cconj_description):
        return "CCONJ"
    elif is_det(sentence, word, det_description):
        return "DET"
    elif is_intj(sentence, word, intj_description):
        return "INTJ"
    elif is_noun(sentence, word, noun_description):
        return "NOUN"
    elif is_num(sentence, word, num_description):
        return "NUM"
    elif is_part(sentence, word, part_description):
        return "PART"
    elif is_prop(sentence, word, prop_description):
        return "PROP"
    elif is_propn(sentence, word, propn_description):
        return "PROPN"
    elif is_punct(sentence, word, punct_description):
        return "PUNCT"
    elif is_sconj(sentence, word, sconj_description):
        return "SCONJ"
    elif is_sym(sentence, word, sym_description):
        return "SYM"
    else:
        return "X"


# program
{
    "method": "get_POS_for_word_in_sentence",
    "arguments": {"sentence": "str", "word": "str"},
    "return": "str",
    "execute": "get_POS_for_word_in_sentence(sentence,word)",
}

# preprocessor
def preprocess(input: str):
    word = input.split("Word:")[1].strip()
    sentence = input.split("Word:")[0].strip().split("Sentence:")[1].strip()
    return sentence, word
