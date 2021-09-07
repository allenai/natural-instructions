## Tasks List 

This directory contains the tasks that are part of this benchmark. 


Name | Summary | Category
---- | ----------- | --------
`task001_quoref_question_generation`	| Writing questions that require tracking entity references.	| Question Generation
`task002_quoref_answer_generation`	| Answering questions that require tracking entity references.	| Answer Generation
`task003_mctaco_question_generation_event_duration`	| Writing questions that involve commonsense understanding of "event duration". | Question Generation
`task004_mctaco_answer_generation_event_duration`	| Answering questions that involve commonsense understanding of "event duration". | Answer Generation
`task005_mctaco_wrong_answer_generation_event_duration`	| Writing an implausible answer to the given "event duration" question. | Incorrect Answer Generation
`task006_mctaco_question_generation_transient_stationary`	| Writing questions that involve commonsense understanding of "transient vs. stationary" events. | Question Generation
`task007_mctaco_answer_generation_transient_stationary`	| Answering questions that involve commonsense understanding of "transient vs. stationary" events. | Answer Generation
`task008_mctaco_wrong_answer_generation_transient_stationary`	| Writing an implausible answer to a "transient v. stationary" question. | Incorrect Answer Generation
`task009_mctaco_question_generation_event_ordering`	| Writing questions that involve commonsense understanding of "event ordering" of events. | Question Generation
`task010_mctaco_answer_generation_event_ordering`	| Answering questions that involve commonsense understanding of "event ordering". | Answer Generation
`task011_mctaco_wrong_answer_generation_event_ordering`	| Writing an implausible answers to the given "event ordering" question. | Incorrect Answer Generation
`task012_mctaco_question_generation_absolute_timepoint`	| Writing questions that involve commonsense understanding of when events typically happen. | Question Generation
`task013_mctaco_answer_generation_absolute_timepoint`	| Answering questions that involve commonsense understanding of "absolute timepoint" of events. | Answer Generation
`task014_mctaco_wrong_answer_generation_absolute_timepoint`	| Writing an implausible answer to the provided "absolute timepoint" question. | Incorrect Answer Generation
`task015_mctaco_question_generation_frequency`	| Writing questions that involve commonsense understanding of events' "frequencies". | Question Generation
`task016_mctaco_answer_generation_frequency`	| Answering questions that involve commonsense understanding of event "frequency". | Answer Generation
`task017_mctaco_wrong_answer_generation_frequency`	| Writing an implausible answer to the given event "frequency" question. | Incorrect Answer Generation
`task018_mctaco_temporal_reasoning_presence`	| Checking the presence of temporal reasoning in a question.	| Classification
`task019_mctaco_temporal_reasoning_category`	| Verifying the temporal reasoning category of a given question.	| Classification
`task020_mctaco_span_based_question`	| Checking whether the given sentence contains answer to the given question.	| Classification
`task021_mctaco_grammatical_logical`	| Checking grammatical and logical correctness of a question.	| Classification
`task022_cosmosqa_passage_inappropriate_binary`	| Identifying inappropriate content in context sentences. |  Classification
`task023_cosmosqa_question_generation`	| Craft one question such that it requires commonsense to be answered. | Question Generation 
`task024_cosmosqa_answer_generation`	| Answering commonsense questions.	| Answer Generation
`task025_cosmosqa_incorrect_answer_generation`	| Writing incorrect answers options for a commonsense question. | Incorrect Answer Generation
`task026_drop_question_generation`	| Creating complex reasoning questions based on a passage.	| Question Generation
`task027_drop_answer_type_generation`	| Finding the answer type of a reasoning question.	| Classification
`task028_drop_answer_generation`	| Answering a complex reasoning question based on a passage.	| Answer Generation
`task029_winogrande_full_object`	| Creating a pair of fill in the blank question-answer pairs on objects. | Long Text Generation
`task030_winogrande_full_person`	| Creating a pair of fill in the blank questions on persons. | Long Text Generation
`task031_winogrande_question_generation_object`	| Writing a fill in the blank question on objects.	| Question Generation
`task032_winogrande_question_generation_person`	| Writing a fill in the blank question on persons.	| Question Generation
`task033_winogrande_answer_generation`	| Answering a fill in the blank question on objects.	| Answer Generation
`task034_winogrande_question_modification_object`	| Modifying a fill in the blank question on objects. | Text Modification
`task035_winogrande_question_modification_person`	| Modifying a fill in the blank question on persons. | Text Modification
`task036_qasc_topic_word_to_generate_related_fact`	| Writing a topic word related to a given fact. | Text Modification
`task037_qasc_generate_related_fact`	| Constructing a related fact based on a given topic word.	 | Text Modification
`task038_qasc_combined_fact`	| Combining two facts.	 | Text Modification
`task039_qasc_find_overlapping_words`	| Finding overlapping words between two sentences.	| Verification
`task040_qasc_question_generation`	| Creating a question based on a given sentence.	| Question Generation
`task041_qasc_answer_generation`	| Writing correct answer to a given question based on a given sentence.	| Answer Generation
`task042_qasc_incorrect_option_generation`	| Writing incorrect answers to a given question based on a given sentence.	| Incorrect Answer Generation
`task043_essential_terms_answering_incomplete_questions`	| Answering incomplete questions. | Answer Generation
`task044_essential_terms_identifying_essential_words`	| Identifying words or phrases of the question essential for choosing the correct answer.	| Verification
`task045_miscellaneous_sentence_paraphrasing`	| Generating sentence paraphrases. | Text Modification
`task046_miscellaenous_question_typing`	| Annotating question-answer pairs with their corresponding type(s).	| Classification
`task047_miscellaenous_answering_science_questions`	| Answering simple science questions.	| Answer Generation
`task048_multirc_question_generation`	| Constructing questions based on the information present in the passage.	| Question Generation
`task049_multirc_questions_needed_to_answer`	| Identifying sentences needed to answer a given question.	| Classification
`task050_multirc_answerability`	| Finding answerability of questions based on a given sentence.	| Classification
`task051_multirc_correct_answer_single_sentence`	| Generating correct answer to single-sentence questions.	| Answer Generation
`task052_multirc_identify_bad_question`	| Identifying bad questions.	| Classification
`task053_multirc_correct_bad_question`	| Correcting bad questions. | Text Modification
`task054_multirc_write_correct_answer`	| Writing A Correct Answer for a Reading Comprehension Task.	| Answer Generation
`task055_multirc_write_incorrect_answer`	| Writing Incorrect Answers for a Reading Comprehension Task. | Incorrect AnswerGeneration
`task056_multirc_classify_correct_answer`	| Classifying Good Correct Answers.	| Classification
`task057_multirc_classify_incorrect_answer`	| Classifying Good Incorrect Answers.	| Classification
`task058_multirc_question_answering`	| Reading Comprehension Over Multiple Sentences.	| Classification
`task059_ropes_story_generation`	| Generating a story about relations in the given paragraph.	| Long Text Generation
`task060_ropes_question_generation`	| Constructing questions regarding relations in the given paragraph.	| Question Generation
`task061_ropes_answer_generation`	| Answering questions regarding relations in the given paragraph.	| Answer Generation
`task062_bigbench_repeat_copy_logic`	|  Generating text that follows simple logical operations such as "repeat", "before", "after" etc.	| Logic
`task065_timetravel_consistent_sentence_classification`	| Choosing the option that makes a given short story consistent. | Classification
`task066_timetravel_binary_consistency_classification`	| Identifying if the given sentence is consistent with the given story. | Classification
`task067_abductivenli_answer_generation`	|  Generating text that completes a story based on given beginning and ending.	| Answer Generation
`task068_abductivenli_incorrect_answer_generation.json`	|  Generating text that modifies a story to be incorrect based on given beginning, middle, and ending.	| Answer Generation
`task069_abductivenli_classification.json`	|  Choosing text that completes a story based on given beginning and ending.	| Classification
`task070_abductivenli_incorrect_classification.json`	|  Choosing text that incorrectly completes a story based on given beginning and ending.	| Classification
`task071_abductivenli_answer_generation`	|  Generating text that completes a story based on given beginning and middle.	| Answer Generation
`task072_abductivenli_answer_generation`	|  Generating text that completes a story based on given middle and ending.	| Answer Generation
`task073_CommonsenseQA_answer_generation` | Answering questions based on commonsense knowledge | Answer Generation
`task074_squad1.1_question_generation` | Generating guestions (based on SQuAD 1.1) | Question Generation  
`task075_squad1.1_answer_generation` | Generating answers to SQuAD 1.1 questions | Answer Generation  
`task076_splash_correcting_sql_mistakes` | Based on feedback correct the mistake in a given SQL statement. | Structured Query Generation, Text Modification
`task077_splash_explanation_to_sql` | Generate an SQL statement based on a description of what the SQL statement does. | Structured Query Generation
`task078_splash_sql_to_explanation` | Give a natural language description of what a given SQL statement is doing. | Structured Query Classification
`task079_conala_concat_strings` | Given a list of strings concatenate them to form one string | Answer Generation.
`task085_unnatural_addsub_arithmetic`	|  Performing Arithmetic with swapped operator symbols.	| Arithmetic
`task086_translated_symbol_arithmetic`	|  Performing Arithmetic with translated operator symbols.	| Arithmetic
`task087_new_operator_addsub_arithmetic`	|  Performing Arithmetic with newly defined operator symbols.	| Arithmetic
`task088_identify_typo_verification`	|  Identifying typo in a sentence.	| Verification
`task089_swap_words_verification`	|  Identifying swapped words in a sentence.	| Verification
`task090_equation_learner_algebra`	|  Answering based on the given equation.	| Algebra
`task092_check_prime_classification`	|  Finding whether the number is prime or not.	| Mathematics
`task079_conala_concat_strings` | Given a list of strings concatenate them to form one string | Answer Generation
`task080_piqa_answer_generation`	|  Generating solution to a goal regarding physical knowledge about the world	| Answer Generation
`task081_piqa_wrong_answer_generation`	|  Generating incorrect solution to a goal regarding physical knowledge about the world	| Incorrect Answer Generation
`task082_babi_t1_single_supporting_fact_question_generation` | Generating a question, given a collection of facts | Question Generation  
`task083_babi_t1_single_supporting_fact_answer_generation` | Generating an answer, given a collection of evidence sentences | Answer Generatiomn 
`task084_babi_t1_single_supporting_fact_identify_relevant_fact` | Given a question and answer, identifying the relevant piece of evidence | Supporting Fact Identification  
`task093_conala_normalize_lists` | Given a list of numbers normalize the list such that the result adds to 1 | Answer Generation, Arithmetic
`task094_conala_calculate_mean` | Given a list of numbers calculate the mean of the list | Answer Generation, Arithmetic
`task095_conala_max_absolute_value` | Given a list of numbers calculate the element with the largest absolute value | Answer Generation, Arithmetic
`task096_conala_list_index_subtraction` | Given a list of numbers subtract each element by its index in the list | Answer Generation, Arithmetic
`task097_conala_remove_duplicates` | Given a list of numbers remove all of the duplicates in the list | Text Modification, Arithmetic
`task098_conala_list_intersection` | Given a two lists of numbers find the intersection of the two lists | Answer Generation, Arithmetic
`task111_asset_sentence_simplification` | Given a sentence, simplify it so it can be understood by non-native English speakers | Generation, Paraphrasing
`task112_asset_simple_sentence_identification` | Given two text pieces, choose the one that is simpler and easier to understand by non-native speakers | Answer Generation, Sentence Comparison
`task102_commongen_sentence_generation` | Given a collection of concepts, use them in a coherent sentence. | Sentence Generation
`task103_facts2story_long_text_generation` | Given 5 facts, write a story that incorporates them. | Long Text Generation
`task104_semeval_2019_task10_closed_vocabulary_mathematical_answer_generation`	|  Answering multiple choices mathematical problem described with a closed-vocabulary.	| Answer Generation, Arithmetic
`task105_Story_Cloze-ROCStories_sentence_generation` | Given a four sentences, predict the next (fifth) coherent sentence. | Sentence Generation
`task106_scruples_ethical_judgment`	|  Given two actions choose the one that is considered less ethical.	| Ethical Judgment
`task107_splash_question_to_sql` | Generate an SQL statement from a question asking for certain data. | Structured Query Generation
`task108_ContextualAbuseDetection_classification` | Given a text detect whether it's abusive or not. | Classification
`task109_SMSspamcollection_SpamSMSdetection` | Classify SMS into spam or ham | Classification
`task110_logic2text_sentence_generation.json` | Generate a natural language interpretation of the given logical operators | Sentence Generation
`task113_count_frequency_of_letter.json` | Count Frequency of a letter in the given string | Answer Generation
`task114_is_the_given_word_longest.json` | Is the given word longest in the sentence | Classification
`task115_Help_advice_classification` | Given a text detect whether it's an advise or not. | Classification
`task116_com2sense_commonsense_reasoning` | Decide whether a sentence is plausible and matches commonsense. | Commonsense Reasoning
`task117_spl_translation_en_de.json` | Translate English questions to German while preserving named entities in the original language | Translation
`task118_semeval_2019_task10_open_vocabulary_mathematical_answer_generation`	|  Answering multiple choices mathematical problem described with an open-vocabulary.	| Answer Generation, Arithmetic
`task119_semeval_2019_task10_geometric_mathematical_answer_generation`	|  Answering multiple choices geometric problems.	| Answer Generation, Geometry
`task119_zest_text_modification.json` | Paraphrasing given question | Text Modification
`task120_zest_text_modification.json` | Given a question, Change the answer with minimum changes | Text Modification
`task121_zest_text_modification.json` | Given some questions, combine them to have one new question | Text Modification
`task122_conala_list_index_addition.json` | Add lists together based on their index | Answer Generation, Arithmetic
`task123_conala_sort_dictionary.json` | Sort a list of dictionaries based on a given key | Answer Generation, Arithmetic
`task124_conala_pair_averages.json` | Calculate the averages for each two consecutive elements | Answer Generation, Arithmetic
`task125_conala_pair_differences.json` | Calculate the absolute difference for each two consecutive elements | Answer Generation, Arithmetic
`task126_scan_structured_text_generation_command_action_all.json` | Given a natural language command, provide its sequence of actions. | Structured Text Generation
`task127_scan_long_text_generation_action_command_all.json` | Given a sequence of actions, provide its natural language command. | Long Text Generation
`task128_scan_structured_text_generation_command_action_short.json` | Given a short natural language command, provide its sequence of actions. | Structured Text Generation
`task129_scan_long_text_generation_action_command_short.json` | Given a short sequence of actions, provide its natural language command. | Long Text Generation
`task130_scan_structured_text_generation_command_action_long.json` | Given a long natural language command, provide its sequence of actions. | Structured Text Generation
`task131_scan_long_text_generation_action_command_long.json` | Given a long sequence of actions, provide its natural language command. | Long Text Generation
`task133_winowhy_reason_plausibility_detection.json` | Detect if a reason explaining an answer to a pronoun coreference resolution question is correct or not | Classification
`task134_winowhy_reason_generation.json` | Giva a reason that explains the answer to a pronoun coreference resolution question | Answer Generation
`task135_winowhy_wrong_reason_generation.json` | Giva an reason that can not explain the answer to a pronoun coreference resolution question | Wrong Answer Generation
`task136_winowhy_knowledge_categorization.json` | Categorize the knowledge required to answer a pronoun coreference resolution question  | Classification
`task137_detoxifying-lms_classification_toxicity.json` | Given a prompt and two completions, determine which completion is less toxic. | Classification
`task138_detoxifying-lms_classification_fluency.json` | Given a prompt and two completions, determine which completion is more fluent. | Classification
`task139_detoxifying-lms_classification_topicality.json` | Given a prompt and two completions, determine which completion is more topical. | Classification
`task140_detoxifying-lms_classification_style.json` | Given a prompt and two completions, determine which completion is stylistically more similar. | Classification
`task145_afs_argument_similarity_death_penalty.json` | Given two arguments, determine if they are similar or not. | Binary Classification
`task146_afs_argument_similarity_gun_control.json` | Given two arguments, determine if they are similar or not. | Binary Classification
`task147_afs_argument_similarity_gay_marriage.json` | Given two arguments, determine if they are similar or not. | Binary Classification
`task148_afs_argument_quality_gay_marriage.json` | Given an argument, determine if it's valid. | Binary Classification
`task149_afs_argument_quality_death_penalty.json` | Given an argument, determine if it's valid. | Binary Classification
`task150_afs_argument_quality_gun_control.json.json` | Given an argument, determine if it's valid. | Binary Classification
`task141_odd-man-out_classification_category.json` | Given a category and set of words, select the word that least belongs. | Classification
`task142_odd-man-out_classification_no_category.json` | Given a set of words, select the word that least belongs. | Classification
`task143_odd-man-out_classification_generate_category.json` | Given a set of words, select the category that represents the words. | Classification
`task144_subjqa_question_answering.json` | Given a review and a question, give a span of the review that answers the question. | Answer Generation
`task151_tomqa_find_location_easy_clean.json` | Given an easy story, answer the question regarding the location of an object. | Answer Generation
`task152_tomqa_find_location_easy_noise.json` | Given an easy story with distractor sentences, answer the question regarding the location of an object. | Answer Generation
`task153_tomqa_find_location_hard_clean.json` | Given a hard story, answer the question regarding the location of an object. | Answer Generation
`task154_tomqa_find_location_hard_noise.json` | Given a hard story with distractor sentences, answer the question regarding the location of an object. | Answer Generation
`task155_count_nouns_verbs.json` | Count number of nouns/verbs in the given sentence | Answer Generation
`task110_logic2text_sentence_generation.json` | Generate a natural language interpretation of the given logical operators | Sentence Generation
`task161_count_words_containing_letter.json` | Count number of words in the sentence that contain the given letter | Counting
`task162_count_words_starting_with_letter.json` | Count number of words in the sentence that start with the given letter | Counting
`task163_count_words_ending_with_letter.json` | Count number of words in the sentence that end with the given letter | Counting
`task158_count_frequency_of_words.json` | Count number of occurrences of a word in the given sentence | Counting
`task159_check_frequency_of_words_in_sentence_pair.json` | Check the frequency of a word in the two sentences | Counting, Classification
`task156_codah_classification_adversarial.json` | Given a prompt, select the completion that is the most plausible. | Classification
`task183_rhyme_generation.json` | Given an input word, generate a list of words that rhyme exactly with the input | Answer Generation
`task178_QuaRTz_question_answering` | Given a question, select correct answer from the given options using an Explanation. | Answer Generation
`task223_QuaRTz_explanation_generation` | Given a question and its answer, generate an explanation statement. | Sentence Generation
`task171_spl_translation_en_es.json` | Translate English questions to Spanish while preserving named entities in the original language | Translation
`task172_spl_translation_en_fa.json` | Translate English questions to Farsi while preserving named entities in the original language | Translation
`task173_spl_translation_en_it.json` | Translate English questions to Italian while preserving named entities in the original language | Translation
`task174_spl_translation_en_ja.json` | Translate English questions to Japanese while preserving named entities in the original language | Translation
`task175_spl_translation_en_pl.json` | Translate English questions to Polish while preserving named entities in the original language | Translation
`task179_participant_extraction` | Given a sentence from a medical study paper, select the tokens representing information about participants | Entity Detection
`task180_intervention_extraction` | Given a sentence from a medical study paper, select the tokens representing information about intervention in the study | Entity Detection
`task181_outcome_extraction` | Given a sentence from a medical study paper, select the tokens representing information about outcome of the study | Entity Detection
`task157_count_vowels_and_consonants.json` | Count number of vowels/consonants in the given sentence | Counting
`task160_replace_letter_in_a_sentence.json` | Replace a letter in the sentence with another given letter | Text Modification
`task132_DAIS_text_modification.json` | Given a sentence, generate a sentence with same meaning and different grammatical structure | Text Modification
`task164_MCScript_question_answering_text.json` | Reading Comprehension Task (Multiple Choice Question Answering). | Answer Generation
`task165_MCScript_question_answering_commonsense.json` | Reading Comprehension Task using Commonsense (Multiple Choice Question Answering). | Answer Generation
`task166_ClariQ_sentence_generation` | Provide clarification on the given query which is written in natural language | Sentence Generation
`task167_strategyqa_question_generation` | Given a term, write questions based on two or more facts | Question Generation
`task168_strategyqa_question_decomposition` | Given a yes/no question, its answer, and additional information, decompose the question | Question Decomposition
`task169_strategyqa_sentence_generation` | Given a question, write the facts one needs to know in order to answer the question| Sentence Generation
`task176_break_decompose_questions` | Break a question into the steps needed to answer the question. | Question Decomposition
`task177_para-nmt_paraphrasing` | Given a sentence, rephrase it using another words while retaining meaning same as input. | Text Modification
`task178_QuaRTz_question_answering` | Given a question, select correct answer from the given options using an Explanation. | Answer Generation
`task182_duorc_question_generation` | Writing a question based on a given plot | Question Generation
`task170_hotpotqa_answer_generation.json` | Given a set of context and supporting facts, answer the question asked based on them. | Answer Generation
`task184_snli_entailment_to_neutral_text_modification.json` | Given two sentences that agree with each other, modify the second sentence so that they do not clearly agree or disagree | Answer Generation
`task185_snli_contradiction_to_neutral_text_modification.json` | Given two sentences that don't agree with each other, modify the second sentence so that they do not clearly agree or disagree | Answer Generation
`task186_snli_contradiction_to_entailment_text_modification.json` | Given two sentences that don't agree with each other, modify the second sentence so that they clearly agree with each other | Answer Generation
`task187_snli_entailment_to_contradiction_text_modifcation.json` | Given two sentences that agree with each other, modify the second sentence so that they clearly do not agree | Answer Generation
`task188_snli_neutral_to_entailment_text_modification.json` | Given two sentences that do not clearly agree or disagree with each other, modify the second sentence so that they clearly agree | Answer Generation
`task189_snli_neutral_to_contradiction_text_modification.json` | Given two sentences that do not clearly agree or disagree with each other, modify the second sentence so that they clearly do not agree | Answer Generation
`task190_snli_classification.json` | Given two sentences choose whether they agree/disagree/neither with each other | Classification
`task191_hotpotqa_question_generation.json` | Given a set of context, supporting facts and an answer, generate the question asked based on them. | Question Generation
`task192_hotpotqa_sentence_generation.json` | Given a context paragraph, question and corresponding answer, generate the supporting facts that helps in answering question. | Sentence Generation
`task184_break_generate_question` | Generate a question based on the given steps used to answer it. | Question Generation
`task170_hotpotqa_answer_generation.json` | Given a set of context and supporting facts, answer the question asked based on them. | Answer Generation
`task191_hotpotqa_question_generation.json` | Given a set of context, supporting facts and an answer, generate the question asked based on them. | Question Generation
`task192_hotpotqa_sentence_generation.json` | Given a context paragraph, question and corresponding answer, generate the supporting facts that helps in answering question. | Sentence Generation
`task197_mnli_domain_answer_generation.json` | Given two sentences, write a single word describing the common genre to which they belong | Answer Generation
`task198_mnli_domain_classification.json` | Given two sentences and 10 genre choices, determine the genre to which the sentences belong. | Classification
`task199_mnli_classification.json` | Given 2 sentences, determine if they clearly agree or disagree with each other, or if this cannot be answered at all. | Classification
`task200_mnli_entailment_classification.json` | Given a context statement and 3 sentences as choices, choose the sentence that clearly agrees with the context statement. | Classification
`task201_mnli_neutral_classification.json` | Given a context statement and 3 sentences as choices, choose the sentence that neither clearly agrees nor disagrees with the context statement. | Classification
`task202_mnli_contradiction_classification.json` | Given a context statement and 3 sentences as choices, choose the sentence that clearly disagrees with the context statement. | Classification
`task203_mnli_sentence_generation.json` | Given a context statement, genre, and label indicating agree/disagree/neither with respect to the context statement, generate a sentence that follows the genre and label specifications. | Answer Generation
`task204_mnli_same_genre_classification.json` | Given two sentences and the genre they should belong to, determine if they belong to the same genre or not. | Classification
`task225_English_language_Answer_Generation.json` | Given a basic english language related question generate the answer with proper context, definitions, and examples. | Answer Generation
`task226_English_language_Answer_Relevance_Classification.json` | Given a question and answer pair, detect whether the answer is acceptable or not. | Classification
`task193_duorc_question_generation` | Writing a question based on a given plot | Question Generation
`task194_duorc_answer_generation` | Given a plot and a question, answer the question based on the plot | Answer Generation
`task195_sentiment140_classification.json` | Given a tweet text, classify it into positive or negative | Classification
`task196_sentiment140_answer_generation.json` | Given a tweet text and boolean question, generate answer yes or no | Answer Generation
`task205_remove_even_elements.json` | Given a list of integers remove all elements that are even | Answer Generation, Arithmetic
`task206_collatz_conjecture.json` | Given a list of integers compute the next number in the *3n+1* problem | Answer Generation, Arithmetic
`task207_max_element_lists.json` | Given a list of lists of integers compute the max value for each list | Answer Generation, Arithmetic
`task208_combinations_of_list.json` | Given a list of integers of length *n* find all possible combinations,without replacement, of length *n-1* | Answer Generation, Combinatorics
`task209_StanceDetection_classification.json` | Given a topic and an argument detect whether topic is in favor or against in the argument. | Classification
`task210_logic2text_structured_text_generation.json` | Given a natural language interpretation, generate a command using logical operations | Structured Text Generation
`task211_logic2text_classification.json` | Given a command and corresponding interpretation, classify whether it's right interpretation or not | Classification
`task212_logic2text_classification.json` | Given a command (in the form of logical operators), classify command in one of seven logic types | Classification
`task224_scruples_anecdotes_ethical_judgment` | Given an anecdotes, judge whether the author is ethically correct or not. | Ethical Judgment
`task223_QuaRTz_explanation_generation` | Given a question and its answer, generate an explanation statement. | Sentence Generation
`task224_scruples_anecdotes_ethical_judgment` | Given an anecdotes, judge whether the author is ethically correct or not. | Ethical Judgment
`task227_ClariQ_classification`	| Given a query and its clarification, classify whether clarification is proper or not by providing 'Yes' or 'No' | Classification
`task228_ARC_answer_generation_easy.json` | Given a science question (easy-level), provide answer based on scientific facts and reasoning. (Multiple Choice Question Answering) | Answer Generation
`task229_ARC_answer_generation_hard.json` | Given a science question (hard-level), provide answer based on scientific facts and reasoning. (Multiple Choice Question Answering) | Answer Generation
`task239_TweetQA_answer_generation.json` | Given a context paragraph of the tweet and question, generate a right answer | Answer Generation
`task240_TweetQA_question_generation.json` | Given a context paragraph of the tweet and answer, generate a right question | Question Generation
`task241_TweetQA_classification.json` | Given a context paragraph of the tweet, question and corresponding answer, generate a label whether the answer is right or wrong | Classification
`task242_TweetQA_classification.json` | Given a context paragraph of the tweet, question and corresponding answer, generate a label whether the context is helpful in answering question or not | Classification
`task243_count_elements_in_set_intersection.json` | Count number of elements in the intersection of two given sets | Counting
`task244_count_elements_in_set_union.json` |  Count number of elements in the union of two given sets | Counting
`task245_check_presence_in_set_intersection.json` | Check presence of an element in the intersection of two given sets | Answer Generation
`task281_points_of_correspondence` | Find the entity or event that is in common between the given three sentences | Entity Detection
`task246_dream_question_generation` | Given a conversation, generate a multiple-choice question based on it | Question Generation
`task247_dream_answer_generation` | Given a conversation and a question, answer the question based on the conversation | Answer Generation
`task248_dream_classification` | Given a conversation and a question, classify the question | Classification
`task283_dream_incorrect_answer_generation`	| Given a conversation and a question, write an incorrect answer to the question | Incorrect Answer Generation
`task249_enhanced_wsc_pronoun_disambiguation` | Given a sentence and a pronoun, decide which one of the choices is the pronoun referring to | Answer Generation, Pronoun Disambiguation
`task250_spl_translation_en_ar.json` | Translate English questions to Arabic while preserving named entities in the original language | Translation
`task251_spl_translation_en_fi.json` | Translate English questions to Finnish while preserving named entities in the original language | Translation
`task252_spl_translation_en_tr.json` | Translate English questions to Turkish while preserving named entities in the original language | Translation
`task253_spl_translation_en_zh.json` | Translate English questions to Chinese while preserving named entities in the original language | Translation
`task254_spl_translation_fi_en.json` | Translate Finnish questions to English while preserving named entities in the original language | Translation
`task255_spl_translation_it_en.json` | Translate Italian questions to English while preserving named entities in the original language | Translation
`task256_spl_translation_de_en.json` | Translate German questions to English while preserving named entities in the original language | Translation
`task257_spl_translation_ar_en.json` | Translate Arabic questions to English while preserving named entities in the original language | Translation
`task258_spl_translation_fa_en.json` | Translate Farsi questions to English while preserving named entities in the original language | Translation
`task259_spl_translation_tr_en.json` | Translate Turkish questions to English while preserving named entities in the original language | Translation
`task260_spl_translation_zh_en.json` | Translate Chinese questions to English while preserving named entities in the original language | Translation
`task261_spl_translation_es_en.json` | Translate Spanish questions to English while preserving named entities in the original language | Translation
`task262_spl_translation_ja_en.json` | Translate Japanese questions to English while preserving named entities in the original language | Translation
`task263_spl_translation_pl_en.json` | Translate Polish questions to English while preserving named entities in the original language | Translation
`task268_casehold_legal_answer_generation` | Given a prompt from a judicial decision and multiple potential holdings, choose the correct option | Legal , Answer Generation
`task271_europarl_translation.json`| Translate bulgarian sentence into english language | Translation
`task272_europarl_translation.json`| Translate english sentence into bulgarian language | Translation
`task273_europarl_classification.json`| Given bulgarian sentence and corresponding english translation, verify that the translation is right or wrong | Classification
`task274_overruling_legal_classification`	| Given a sentence, classify it into overruling or non-overruling| Legal , Classification
`task275_enhanced_wsc_paraphrase_generation` | Given a sentence and an aspect, paraphrase the sentence changing that aspect | Text Modification
`task276_enhanced_wsc_classification` | Given a sentence and its paraphrase, decide what is the difference between them. | Classification
`task277_StereoSet_sentence_generation_stereotype.json` | Generate sentences with stereotype given context | Sentence Generation
`task278_StereoSet_sentence_generation_antistereotype.json` | Generate sentences with anti-stereotype given context | Sentence Generation
`task279_StereoSet_classification_stereotype.json` | Classify sentences into stereotype, anti-stereotype, and unrelated | Classification
`task280_StereoSet_classification_stereotype_type.json` | Classify sentences into four kinds of stereotype, including gender, profession, race, and religion | Classification
`task282_scruples_event_time` | Given an anecdotes, find whether it has already happened or it may happen in the future  | Answer Generation
`task286_olid_offense_judgment.json` | Given a tweet judge whether its offensive or not | Classification
`task287_casehold_legal_incorrect_answer_generation` | Given a prompt from a judicial decision and multiple potential holdings, choose one of the incorrect options | Legal , Incorrect Answer Generation
`task290_TELLMYWHY_question_answerability` | Given a story and a question, decide whether or not the question is answerable | Classification
`task301_record_question_generation` | Given a passage, generate a fill-in-the-gap question based on it | Question Generation
`task302_record_classification` | Given a passage and a question, classify the answer to the question based on the options | Classification
`task303_record_incorrect_answer_generation` | Given a passage and a question, write an incorrect answer for the question | Incorrect Answer Generation
`task339_record_answer_generation` | Given a passage and a question, answer the question based on the passage | Answer Generation
