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
`task067_abductivenli_answer_generation`	|  Generating text that completes a story based on the beginning and ending.	| Answer Generation
`task068_abductivenli_incorrect_answer_generation`	|  Generating text that modifies a story to be incorrect based on the beginning, middle, and ending.	| Answer Generation
`task069_abductivenli_classification`	|  Choosing text that completes a story based on given beginning and ending.	| Classification
`task070_abductivenli_incorrect_classification`	|  Choosing text that incorrectly completes a story based on given beginning and ending.	| Classification
`task071_abductivenli_answer_generation`	|  Generating text that completes a story based on given beginning and middle.	| Answer Generation
`task072_abductivenli_answer_generation`	|  Generating text that completes a story based on given middle and ending.	| Answer Generation
`task073_commonsenseqa_answer_generation` | Answer questions based on commonsense knowledge. | Answer Generation
`task074_squad1.1_question_generation` | Generate guestions based on SQuAD 1.1. | Question Generation
`task075_squad1.1_answer_generation` | Generate answers to SQuAD 1.1 questions. | Answer Generation
`task076_splash_correcting_sql_mistakes` | Correct the mistake in a given SQL statement based on feedback. | Structured Query Generation, Text Modification
`task077_splash_explanation_to_sql` | Generate a SQL statement based on a description of what the SQL statement does. | Structured Query Generation
`task078_splash_sql_to_explanation` | Give a natural language description of what a given SQL statement does. | Structured Query Classification
`task079_conala_concat_strings` | Given a list of strings, concatenate them to form one string. | Answer Generation
`task080_piqa_answer_generation`	|  Generate a solution to a goal regarding physical knowledge about the world.	| Answer Generation
`task081_piqa_wrong_answer_generation`	|  Generate an incorrect solution to a goal regarding physical knowledge about the world.	| Incorrect Answer Generation
`task082_babi_t1_single_supporting_fact_question_generation` | Generate a question, given a collection of facts. | Question Generation
`task083_babi_t1_single_supporting_fact_answer_generation` | Generate an answer, given a collection of evidence sentences. | Answer Generation
`task084_babi_t1_single_supporting_fact_identify_relevant_fact` | Given a question and an answer, identify the relevant piece of evidence. | Supporting Fact Identification
`task085_unnatural_addsub_arithmetic`	|  Performing arithmetic with swapped operator symbols.	| Arithmetic
`task086_translated_symbol_arithmetic`	|  Performing arithmetic with translated operator symbols.	| Arithmetic
`task087_new_operator_addsub_arithmetic`	|  Performing arithmetic with newly defined operator symbols.	| Arithmetic
`task088_identify_typo_verification`	|  Identify the typo in a sentence.	| Verification
`task089_swap_words_verification`	|  Identify the swapped words in a sentence.	| Verification
`task090_equation_learner_algebra`	|  Answer the given equation.	| Algebra
`task092_check_prime_classification`	|  Identify whether the number is prime or not.	| Mathematics
`task093_conala_normalize_lists` | Given a list of numbers, normalize the list such that the result adds to 1. | Answer Generation, Arithmetic
`task094_conala_calculate_mean` | Given a list of numbers, calculate the mean of the list. | Answer Generation, Arithmetic
`task095_conala_max_absolute_value` | Given a list of numbers, calculate the element with the largest absolute value. | Answer Generation, Arithmetic
`task096_conala_list_index_subtraction` | Given a list of numbers, subtract each element by its index in the list. | Answer Generation, Arithmetic
`task097_conala_remove_duplicates` | Given a list of numbers, remove all of the duplicates in the list. | Text Modification, Arithmetic
`task098_conala_list_intersection` | Given a two lists of numbers, find the intersection of the two lists. | Answer Generation, Arithmetic
`task102_commongen_sentence_generation` | Given a collection of concepts, use them in a coherent sentence. | Sentence Generation
`task103_facts2story_long_text_generation` | Given 5 facts, write a story that incorporates them. | Long Text Generation
`task104_semeval_2019_task10_closed_vocabulary_mathematical_answer_generation`	|  Answering multiple choices mathematical problem described with a closed-vocabulary.	| Answer Generation, Arithmetic
`task105_story_cloze-rocstories_sentence_generation` | Given four sentences, predict the next coherent sentence. | Sentence Generation
`task106_scruples_ethical_judgment`	|  Given two actions choose the one that is considered less ethical.	| Ethical Judgment
`task107_splash_question_to_sql` | Generate an SQL statement from a question asking for certain data. | Structured Query Generation
`task108_contextualabusedetection_classification` | Given a text detect whether it's abusive or not. | Classification
`task109_smsspamcollection_spamsmsdetection` | Classify SMS into spam or ham. | Classification
`task110_logic2text_sentence_generation` | Generate a natural language interpretation of the given logical operators. | Sentence Generation
`task111_asset_sentence_simplification` | Given a sentence, simplify it so it can be understood by non-native English speakers. | Generation, Paraphrasing
`task112_asset_simple_sentence_identification` | Given two excerpts of text, choose the one that is simpler and easier to understand by non-native speakers. | Answer Generation, Sentence Comparison
`task113_count_frequency_of_letter` | Count the frequency of a letter in the given string. | Answer Generation
`task114_is_the_given_word_longest` | Identify whether the word is the longest in the sentence. | Classification
`task115_help_advice_classification` | Given a text, detect whether it's an advise or not. | Classification
`task116_com2sense_commonsense_reasoning` | Decide whether a sentence is plausible and matches commonsense. | Commonsense Reasoning
`task117_spl_translation_en_de` | Translate English questions to German while preserving named entities in the original language. | Translation
`task118_semeval_2019_task10_open_vocabulary_mathematical_answer_generation`	|  Answering multiple choices mathematical problem described with an open vocabulary.	| Answer Generation, Arithmetic
`task119_semeval_2019_task10_geometric_mathematical_answer_generation`	|  Answering multiple choices geometric problems.	| Answer Generation, Geometry
`task119_zest_text_modification` | Paraphrase the given question. | Text Modification
`task120_zest_text_modification` | Given a question, change the answer with minimum changes. | Text Modification
`task121_zest_text_modification` | Given some questions, combine them to have one new question. | Text Modification
`task122_conala_list_index_addition` | Add lists together based on their index. | Answer Generation, Arithmetic
`task123_conala_sort_dictionary` | Sort a list of dictionaries based on a given key. | Answer Generation, Arithmetic
`task124_conala_pair_averages` | Calculate the averages for each two consecutive elements. | Answer Generation, Arithmetic
`task125_conala_pair_differences` | Calculate the absolute difference for each two consecutive elements. | Answer Generation, Arithmetic
`task126_scan_structured_text_generation_command_action_all` | Given a natural language command, provide its sequence of actions. | Structured Text Generation
`task127_scan_long_text_generation_action_command_all` | Given a sequence of actions, provide its natural language command. | Long Text Generation
`task128_scan_structured_text_generation_command_action_short` | Given a short natural language command, provide its sequence of actions. | Structured Text Generation
`task129_scan_long_text_generation_action_command_short` | Given a short sequence of actions, provide its natural language command. | Long Text Generation
`task130_scan_structured_text_generation_command_action_long` | Given a long natural language command, provide its sequence of actions. | Structured Text Generation
`task131_scan_long_text_generation_action_command_long` | Given a long sequence of actions, provide its natural language command. | Long Text Generation
`task132_dais_text_modification` | Given a sentence, generate a sentence with same meaning and different grammatical structure. | Text Modification
`task133_winowhy_reason_plausibility_detection` | Detect if a reason that explains an answer to a pronoun coreference resolution question is correct or not. | Classification
`task134_winowhy_reason_generation` | Give a reason that explains the answer to a pronoun coreference resolution question. | Answer Generation
`task135_winowhy_wrong_reason_generation` | Give a reason that can not explain the answer to a pronoun coreference resolution question. | Wrong Answer Generation
`task136_winowhy_knowledge_categorization` | Categorize the knowledge required to answer a pronoun coreference resolution question.  | Classification
`task137_detoxifying-lms_classification_toxicity` | Given a prompt and two completions, determine which completion is less toxic. | Classification
`task138_detoxifying-lms_classification_fluency` | Given a prompt and two completions, determine which completion is more fluent. | Classification
`task139_detoxifying-lms_classification_topicality` | Given a prompt and two completions, determine which completion is more topical. | Classification
`task140_detoxifying-lms_classification_style` | Given a prompt and two completions, determine which completion is stylistically more similar. | Classification
`task141_odd-man-out_classification_category` | Given a category and set of words, select the word that least belongs. | Classification
`task142_odd-man-out_classification_no_category` | Given a set of words, select the word that least belongs. | Classification
`task143_odd-man-out_classification_generate_category` | Given a set of words, select the category that represents the words. | Classification
`task144_subjqa_question_answering` | Given a review and a question, answer the question with the span of the review. | Answer Generation
`task145_afs_argument_similarity_death_penalty` | Given two arguments, determine if they are similar or not. | Binary Classification
`task146_afs_argument_similarity_gun_control` | Given two arguments, determine if they are similar or not. | Binary Classification
`task147_afs_argument_similarity_gay_marriage` | Given two arguments, determine if they are similar or not. | Binary Classification
`task148_afs_argument_quality_gay_marriage` | Given an argument, determine if it's valid. | Binary Classification
`task149_afs_argument_quality_death_penalty` | Given an argument, determine if it's valid. | Binary Classification
`task150_afs_argument_quality_gun_control` | Given an argument, determine if it's valid. | Binary Classification
`task151_tomqa_find_location_easy_clean` | Given an easy story, answer the question regarding the location of an object. | Answer Generation
`task152_tomqa_find_location_easy_noise` | Given an easy story with distractor sentences, answer the question regarding the location of an object. | Answer Generation
`task153_tomqa_find_location_hard_clean` | Given a hard story, answer the question regarding the location of an object. | Answer Generation
`task154_tomqa_find_location_hard_noise` | Given a hard story with distractor sentences, answer the question regarding the location of an object. | Answer Generation
`task155_count_nouns_verbs` | Count the number of nouns/verbs in the given sentence. | Answer Generation
`task156_codah_classification_adversarial` | Given a prompt, select the completion that is the most plausible. | Classification
`task157_count_vowels_and_consonants` | Count the number of vowels/consonants in the given sentence. | Counting
`task158_count_frequency_of_words` | Count the number of occurrences of a word in the given sentence. | Counting
`task159_check_frequency_of_words_in_sentence_pair` | Check the frequency of a word in the two sentences. | Counting, Classification
`task160_replace_letter_in_a_sentence` | Replace a letter in the sentence with another given letter. | Text Modification
`task161_count_words_containing_letter` | Count the number of words in the sentence that contain the given letter. | Counting
`task162_count_words_starting_with_letter` | Count the number of words in the sentence that start with the given letter. | Counting
`task163_count_words_ending_with_letter` | Count the number of words in the sentence that end with the given letter. | Counting
`task164_mcscript_question_answering_text` | Given a passage and question, select the best answer from the given choices. | Answer Generation
`task165_mcscript_question_answering_commonsense` | Given a passage and question, generate the best answer. | Answer Generation
`task166_clariq_sentence_generation` | Provide clarification on the given query which is written in natural language. | Sentence Generation
`task167_strategyqa_question_generation` | Given a term, write questions based on two or more facts. | Question Generation
`task168_strategyqa_question_decomposition` | Given a yes/no question, its answer, and additional information, decompose the question. | Question Decomposition
`task169_strategyqa_sentence_generation` | Given a question, write the facts one needs to know in order to answer the question. | Sentence Generation
`task170_hotpotqa_answer_generation` | Given a set of context and supporting facts, answer the question asked. | Answer Generation
`task171_spl_translation_en_es` | Translate English questions to Spanish while preserving named entities in the original language. | Translation
`task172_spl_translation_en_fa` | Translate English questions to Farsi while preserving named entities in the original language. | Translation
`task173_spl_translation_en_it` | Translate English questions to Italian while preserving named entities in the original language. | Translation
`task174_spl_translation_en_ja` | Translate English questions to Japanese while preserving named entities in the original language. | Translation
`task175_spl_translation_en_pl` | Translate English questions to Polish while preserving named entities in the original language. | Translation
`task176_break_decompose_questions` | Break a question into the steps needed to answer the question. | Question Decomposition
`task177_para-nmt_paraphrasing` | Given a sentence, rephrase it using another words while retaining meaning same as input. | Text Modification
`task178_quartz_question_answering` | Given a question, select the correct answer from the given options using an explanation. | Answer Generation
`task179_participant_extraction` | Given a sentence from a medical study paper, select the tokens representing information about participants. | Entity Detection
`task180_intervention_extraction` | Given a sentence from a medical study paper, select the tokens representing information about intervention in the study. | Entity Detection
`task181_outcome_extraction` | Given a sentence from a medical study paper, select the tokens representing information about outcome of the study. | Entity Detection
`task182_duorc_question_generation` | Writing a question based on a given plot. | Question Generation
`task183_rhyme_generation` | Given an input word, generate a list of words that rhyme exactly with the input. | Answer Generation
`task184_break_generate_question` | Generate a question based on the given steps used to answer it. | Question Generation
`task184_snli_entailment_to_neutral_text_modification` | Given two sentences that agree with each other, modify the second sentence so that they do not clearly agree or disagree. | Answer Generation
`task185_snli_contradiction_to_neutral_text_modification` | Given two sentences that don't agree with each other, modify the second sentence so that they do not clearly agree or disagree. | Answer Generation
`task186_snli_contradiction_to_entailment_text_modification` | Given two sentences that don't agree with each other, modify the second sentence so that they clearly agree with each other. | Answer Generation
`task187_snli_entailment_to_contradiction_text_modification` | Given two sentences that agree with each other, modify the second sentence so that they clearly do not agree. | Answer Generation
`task188_snli_neutral_to_entailment_text_modification` | Given two sentences that do not clearly agree or disagree with each other, modify the second sentence so that they clearly agree. | Answer Generation
`task189_snli_neutral_to_contradiction_text_modification` | Given two sentences that do not clearly agree or disagree with each other, modify the second sentence so that they clearly do not agree. | Answer Generation
`task190_snli_classification` | Given two sentences choose whether they agree/disagree/neither with each other. | Classification
`task191_hotpotqa_question_generation` | Given a set of context, supporting facts and an answer, generate the question asked based on them. | Question Generation
`task192_hotpotqa_sentence_generation` | Given a context paragraph, question and corresponding answer, generate the supporting facts that helps in answering question. | Sentence Generation
`task193_duorc_question_generation` | Generate a question based on a given plot. | Question Generation
`task194_duorc_answer_generation` | Given a plot and a question, answer the question based on the plot. | Answer Generation
`task195_sentiment140_classification` | Given a tweet, classify its sentiment as either positive or negative. | Classification
`task196_sentiment140_answer_generation` | Given a tweet and boolean question, generate yes or no. | Answer Generation
`task197_mnli_domain_answer_generation` | Given two sentences, write a single word describing the common genre to which they belong. | Answer Generation
`task198_mnli_domain_classification` | Given two sentences and 10 genre choices, determine the genre to which the sentences belong. | Classification
`task199_mnli_classification` | Given 2 sentences, determine if they clearly agree or disagree with each other or if they cannot be answered. | Classification
`task200_mnli_entailment_classification` | Given a context statement and 3 sentences as choices, select the sentence that clearly agrees with the context statement. | Classification
`task201_mnli_neutral_classification` | Given a context statement and 3 sentences as choices, select the sentence that neither clearly agrees nor disagrees with the context statement. | Classification
`task202_mnli_contradiction_classification` | Given a context statement and 3 sentences as choices, choose the sentence that clearly disagrees with the context statement. | Classification
`task203_mnli_sentence_generation` | Given a context statement, genre, and label indicating agree/disagree/neither with respect to the context statement, generate a sentence that follows the genre and label specifications. | Answer Generation
`task204_mnli_same_genre_classification` | Given two sentences and the genre they should belong to, determine if they belong to the same genre or not. | Classification
`task205_remove_even_elements` | Given a list of integers, remove all elements that are even. | Answer Generation, Arithmetic
`task206_collatz_conjecture` | Given a list of integers, compute the next number in the *3n+1* problem. | Answer Generation, Arithmetic
`task207_max_element_lists` | Given a list of lists of integers compute the max value for each list. | Answer Generation, Arithmetic
`task208_combinations_of_list` | Given a list of integers of length *n*, find all possible combinations without replacement of length *n-1*. | Answer Generation, Combinatorics
`task209_stancedetection_classification` | Given a topic and an argument, detect whether topic is in favor or against in the argument. | Classification
`task210_logic2text_structured_text_generation` | Given a natural language interpretation, generate a command using logical operations. | Structured Text Generation
`task211_logic2text_classification` | Given a command and corresponding interpretation, classify whether it is the right interpretation or not. | Classification
`task212_logic2text_classification` | Given a command, classify the command in one of seven logic types. | Classification
`task213_rocstories_correct_ending_classification` | Given the title and the first four sentences of a five sentence story, choose the correct story ending. | Classification
`task214_rocstories_incorrect_ending_classification` | Given the title and the first four sentences of a five sentence story, choose the incorrect story ending. | Classification
`task215_rocstories_incorrect_answer_generation` | Given the title and the first four sentences of a five sentence story, write an incorrect story ending. | Answer Generation
`task216_rocstories_correct_answer_generation` | Given the title and the first four sentences of a five sentence story, write a correct story ending. | Answer Generation
`task217_rocstories_ordering_answer_generation` | Given a five sentence story in shuffled order and the title, put the story in the correct order. | Answer Generation
`task218_rocstories_swap_order_answer_generation` | Given a five sentence story and the title, determine which two sentences must be swapped so that the story makes complete sense. | Answer Generation
`task219_rocstories_title_answer_generation` | Given a five sentence story, generate an appropriate title for the story. | Answer Generation
`task220_rocstories_title_classification` | Given a five sentence story, choose an appropriate title for the story from the given options. | Classification
`task221_rocstories_two_choice_classification` | Given three sentences and title of a five sentence story, choose which two sentences from the options given will complete the story. | Classification
`task222_rocstories_two_chioce_slotting_classification` | Given three sentences and title of a five sentence story, choose which two sentences from the given options will complete the story. | Classification
`task223_quartz_explanation_generation` | Given a question and its answer, generate an explanation statement. | Sentence Generation
`task224_scruples_anecdotes_ethical_judgment` | Given an anecdote, judge whether the author is ethically correct or not. | Ethical Judgment
`task225_english_language_answer_generation` | Given a basic English language related question generate the answer with proper context, definitions, and examples. | Answer Generation
`task226_english_language_answer_relevance_classification` | Given a question and answer pair, detect whether the answer is acceptable or not. | Classification
`task227_clariq_classification`	| Given a query and its clarification, classify whether clarification is proper or not by providing 'Yes' or 'No'. | Classification
`task228_arc_answer_generation_easy` | Given a easy science question, provide the answer based on scientific facts and reasoning. | Answer Generation
`task229_arc_answer_generation_hard` | Given a hard science question, provide the answer based on scientific facts and reasoning. | Answer Generation
`task230_iirc_passage_classification` | Given 3 passages and a question, determine which passage can be used to answer the question. | Classification
`task231_iirc_link_classification` | Given a question, context passage, and terms from the passage for further information search, determine which term can be used to answer the question. | Classification
`task232_iirc_link_number_classification` | Given a question and context passage, determine if further information on more than one term from the passage is needed to answer the question. | Classification
`task233_iirc_link_exists_classification` | Given a question and context passage, determine if the passage has any terms that can be used to obtain further information needed to answer the question. | Classification
`task234_iirc_passage_line_answer_generation` | Given a question and context passage, determine which sentence in the passage has terms that can be used to obtain further information needed to answer the question. | Answer Generation
`task235_iirc_question_from_subtext_answer_generation` | Given a context statement, further information on a linked term in the statement, and an answer term, generate a question that can use the information provided to obtain the given answer | Answer Generation
`task236_iirc_question_from_passage_answer_generation` | Given a context passage, further information on a linked term in the statement, and an answer term, generate a question that can use the information provided to obtain the given answer | Answer Generation
`task237_iirc_answer_from_subtext_answer_generation` | Given a context statement, further information on a linked term in the statement, and a question, generate an answer that can use the information provided to solve the question| Answer Generation
`task238_iirc_answer_from_passage_answer_generation` | Given a context passage, further information on a linked term in the statement, and a question, generate an answer that can use the information provided to solve the question| Answer Generation
`task239_tweetqa_answer_generation` | Given a context paragraph of the tweet and question, generate a correct answer. | Answer Generation
`task240_tweetqa_question_generation` | Given a context paragraph of the tweet and answer, generate a correct question. | Question Generation
`task241_tweetqa_classification` | Given a context paragraph of the tweet, question and corresponding answer, generate a label whether the answer is right or wrong. | Classification
`task242_tweetqa_classification` | Given a context paragraph of the tweet, question and corresponding answer, generate a label whether the context is helpful in answering question or not. | Classification
`task243_count_elements_in_set_intersection` | Count the number of elements in the intersection of two given sets. | Counting
`task244_count_elements_in_set_union` |  Count the number of elements in the union of two given sets. | Counting
`task245_check_presence_in_set_intersection` | Check the presence of an element in the intersection of two given sets. | Answer Generation
`task246_dream_question_generation` | Given a conversation, generate a multiple-choice question based on it. | Question Generation
`task247_dream_answer_generation` | Given a conversation and a question, answer the question based on the conversation. | Answer Generation
`task248_dream_classification` | Given a conversation and a question, classify the question. | Classification
`task249_enhanced_wsc_pronoun_disambiguation` | Given a sentence and a pronoun, decide which one of the choices the pronoun is referring to. | Answer Generation, Pronoun Disambiguation
`task250_spl_translation_en_ar` | Translate English questions to Arabic while preserving named entities in the original language. | Translation
`task251_spl_translation_en_fi` | Translate English questions to Finnish while preserving named entities in the original language. | Translation
`task252_spl_translation_en_tr` | Translate English questions to Turkish while preserving named entities in the original language. | Translation
`task253_spl_translation_en_zh` | Translate English questions to Chinese while preserving named entities in the original language. | Translation
`task254_spl_translation_fi_en` | Translate Finnish questions to English while preserving named entities in the original language. | Translation
`task255_spl_translation_it_en` | Translate Italian questions to English while preserving named entities in the original language. | Translation
`task256_spl_translation_de_en` | Translate German questions to English while preserving named entities in the original language. | Translation
`task257_spl_translation_ar_en` | Translate Arabic questions to English while preserving named entities in the original language. | Translation
`task258_spl_translation_fa_en` | Translate Farsi questions to English while preserving named entities in the original language. | Translation
`task259_spl_translation_tr_en` | Translate Turkish questions to English while preserving named entities in the original language. | Translation
`task260_spl_translation_zh_en` | Translate Chinese questions to English while preserving named entities in the original language. | Translation
`task261_spl_translation_es_en` | Translate Spanish questions to English while preserving named entities in the original language. | Translation
`task262_spl_translation_ja_en` | Translate Japanese questions to English while preserving named entities in the original language. | Translation
`task263_spl_translation_pl_en` | Translate Polish questions to English while preserving named entities in the original language. | Translation
`task268_casehold_legal_answer_generation` | Given a prompt from a judicial decision and multiple potential holdings, choose the correct option. | Answer Generation
`task271_europarl_translation`| Translate a sentence in Bulgarian to English. | Translation
`task272_europarl_translation`| Translate a sentence in English to Bulgarian. | Translation
`task273_europarl_classification`| Given a sentence in Bulgarian and its corresponding English translation, verify that the translation is correct. | Classification
`task274_overruling_legal_classification`	| Given a sentence, classify it into overruling or non-overruling. | Classification
`task275_enhanced_wsc_paraphrase_generation` | Given a sentence and an aspect, paraphrase the sentence changing that aspect. | Text Modification
`task276_enhanced_wsc_classification` | Given a sentence and its paraphrase, decide what is the difference between them. | Classification
`task277_stereoset_sentence_generation_stereotype` | Generate sentences with stereotype given context. | Sentence Generation
`task278_stereoset_sentence_generation_antistereotype` | Generate sentences with anti-stereotype given context. | Sentence Generation
`task279_stereoset_classification_stereotype` | Classify sentences into stereotype, anti-stereotype, and unrelated. | Classification
`task280_stereoset_classification_stereotype_type` | Classify sentences into four kinds of stereotypes, including gender, profession, race, and religion. | Classification
`task281_points_of_correspondence` | Find the entity or event that is in common between the given three sentences. | Entity Detection
`task282_scruples_event_time` | Given an anecdote, find whether it has already happened or it may happen in the future.  | Answer Generation
`task283_dream_incorrect_answer_generation`	| Given a conversation and a question, write an incorrect answer to the question. | Incorrect Answer Generation
`task284_imdb_classification` | Given a movie review, classify its sentiment into positive or negative. | Classification
`task285_imdb_answer_generation` | Given a movie review and boolean question, generate answer yes or no. | Answer Generation
`task286_olid_offense_judgment` | Given a tweet judge whether its offensive or not. | Classification
`task287_casehold_legal_incorrect_answer_generation` | Given a prompt from a judicial decision and multiple potential holdings, choose one of the incorrect options. | Incorrect Answer Generation
`task288_gigaword_summarization` | Given a text of article, generate a title for the article. | Summarization
`task289_gigaword_summarization` | Given the text of an article and its title, decide whether the title is appropriate for the article. | Summarization
`task290_tellmewhy_question_answerability` | Given a short story and a question, decide whether or not the question is answerable. | Classification
`task291_semeval_2020_task4_commonsense_validation` | Given two statements, choose the one that makes less sense. | Answer Generation
`task295_semeval_2020_task4_commonsense_reasoning` | Given a statement against commonsense and 3 reasons, choose the best reason explaining why the statement is against commonsense. | Answer Generation
`task296_storycloze_correct_end_classification` | Given four sentences of five sentence story, select correct answer for last (fifth) sentence from the given option. | Classification
`task297_storycloze_incorrect_end_classification` | Given four sentences of five sentence story, select incorrect answer for last (fifth) sentence from the given option. | Incorrect Classification
`task298_storycloze_correct_end_classification` | Given four sentences of five sentence story and fifth sentence, classify whether fifth sentence is proper or not by providing 'Yes' or 'No'. | Classification
`task299_storycloze_sentence_generation` | Given four sentences of five sentence story, provide the position and missing part (fifth sentence) of the story. | Sentence Generation
`task300_storycloze_order_generation` | Given five sentences of story (sentences are shuffled), provide correct order of the story. | Order Generation
`task301_record_question_generation` | Given a passage, generate a fill-in-the-gap question based on it. | Question Generation
`task302_record_classification` | Given a passage and a question, classify the answer to the question based on the options. | Classification
`task303_record_incorrect_answer_generation` | Given a passage and a question, write an incorrect answer for the question. | Incorrect Answer Generation
`task304_numeric_fused_head_resolution` | Given a dialogue and a highlighted number, decide what does the number refer to | Answer Generation
`task305_jeopardy_answer_generation_normal` | Given a category and a trivia clue of relatively easy difficulty, generate the best answer. | Answer Generation
`task306_jeopardy_answer_generation_double` | Given a category and a trivia clue of relatively medium difficulty, generate the best answer. | Answer Generation
`task307_jeopardy_answer_generation_final` | Given a category and a trivia clue of relatively hard difficulty, generate the best answer. | Answer Generation
`task308_jeopardy_answer_generation_all` | Given a category and a trivia clue of varying difficulties, generate the best answer. | Answer Generation
`task312_europarl_sv_en_translation` | Given a Swedish sentence, convert it into English. | Translation
`task313_europarl_en_sv_translation` | Given an English sentence, convert it into Swedish. | Translation
`task314_europarl_sv-en_classification` | Given a Swedish sentence and its corresponding English sentence, classify whether it is correct or not. | Classification
`task315_europarl_sv-en_language_identification` | Given a sentence, identify  whether it is in Swedish or English. | Language Identification
`task316_crows-pairs_classification_stereotype` | Classify a sentence into stereotype or anti-stereotype | Classification
`task317_crows-pairs_classification_stereotype_type` | Classify a sentence into different types of stereotype | Classification
`task318_stereoset_classification_gender` | Given a target pertaining to gender in the two sentences, determine if it is a stereotype. | Classification
`task319_stereoset_classification_profession` | Given a target pertaining to profession in the two sentences, determine if it is a stereotype. | Classification
`task320_stereoset_classification_race` | Given a target pertaining to race in the two sentences, determine if it is a stereotype. | Classification
`task321_stereoset_classification_religion` | Given a target pertaining to religion in the two sentences, determine if it is a stereotype. | Classification
`task322_jigsaw_classification_threat` | Given a comment from online platforms, classify whether or not it contains threats. | Classification
`task323_jigsaw_classification_sexually_explicit` | Given a comment, classify whether it is sexually explicit or not. | Classification
`task324_jigsaw_classification_disagree` | Given a comment, classify whether it expresses disagreement. | Classification
`task325_jigsaw_classification_identity_attack` | Given a comment, classify whether it attacks a person's identity or not. | Classification
`task326_jigsaw_classification_obscene` | Given a comment, classify whether it conveys obscenity or not. | Classification
`task327_jigsaw_classification_toxic` | Given a comment from online platforms, classify whether it is toxic or not. | Classification
`task328_jigsaw_classification_insult` | Given a comment from online platforms, classify whether it is an insult or not. | Classification
`task329_gap_classification` | Given a text containing an ambiguous pronoun, a pronoun, and two candidate names, determine what the pronoun refers to and classify the answers into A, B, or Neither | Classification
`task330_gap_answer_generation` | Given a text containing an ambiguous pronoun and a pronoun, write the name that the pronoun refers to | Answer Generation
`task331_gap_incorrect_answer_generation` | Given a text containing an ambiguous pronoun and a pronoun, write an implausible answer to the question of what is the pronoun reference | Incorrect Answer Generation
`task332_tellmewhy_answer_generation` | Given a short story and a question, answer the question based on the events of the story. | Answer Generation
`task333_hateeval_classification_hate_en` | Given a post in English, classify it into hateful or non-hateful | Classification
`task334_hateeval_classification_hate_es` | Given a post in Spanish, classify it into hateful or non-hateful | Classification
`task335_hateeval_classification_aggresive_en` | Given a hateful post in English, classify it into aggresive or non-aggresive | Classification
`task336_hateeval_classification_aggresive_es` | Given a hateful post in Spanish, classify it into aggresive or non-aggresive | Classification
`task337_hateeval_classification_individual_en` | Given a hateful post in English, classify the target being harassed into individual or generic | Classification
`task338_hateeval_classification_individual_es` | Given a hateful post in Spanish, classify the target being harassed into individual or generic | Classification
`task339_record_answer_generation` | Given a passage and a question, answer the question based on the passage. | Answer Generation
`task344_hybridqa_answer_generation` | Given a question, answer the question based on your knowledge. | Answer Generation
`task345_hybridqa_answer_generation` | Given a question, write the part-of-speech tag for each word in the question. | Answer Generation
`task346_hybridqa_classification` | Given a question, a word, and a POS tag, determine whether the POS tag is True or False based on the part-of-speech tag of the given word in the question. | Classification
`task347_hybridqa_incorrect_answer_generation` | Given a question about part-of-speech tag of a word in the question, write an implausible POS tag to the question. | Incorrect Answer Generation
`task348_squad2.0_unanswerable_question_generation` | Given a passage, generate a question that cannot be answered based on the passage. | Unanswerable Question Generation
`task349_squad2.0_answerable_unanswerable_question_classification` | Given a passage and a question, classify whether or not the question is answerable from the passage. | Classification
`task352_coda-19_classification` | given a paragraph, classify into these categories: background, purpose, method, finding/contribution, and other. | Classification
`task353_casino_classification_negotiation_elicit_pref` | Detecting the usage of elicit-pref negotiation strategy in dialogue utterances. | Classification
`task354_casino_classification_negotiation_no_need` | Detecting the usage of no-need negotiation strategy in dialogue utterances. | Classification
`task355_casino_classification_negotiation_other_need` | Detecting the usage of other-need negotiation strategy in dialogue utterances. | Classification
`task356_casino_classification_negotiation_self_need` | Detecting the usage of self-need negotiation strategy in dialogue utterances. | Classification
`task357_casino_classification_negotiation_small_talk` | Detecting the usage of small-talk negotiation strategy in dialogue utterances. | Classification
`task358_casino_classification_negotiation_uv_part` | Detecting the usage of uv-part negotiation strategy in dialogue utterances. | Classification
`task359_casino_classification_negotiation_vouch_fair` | Detecting the usage of vouch-fair negotiation strategy in dialogue utterances. | Classification
`task363_sst2_polarity_classification` | Given a sentence from a movie review, classify the sentence to positive or negative sentiment. | Classification
`task364_regard_social_impact_classification` | Given a sentence about a person, decide what is the impact of that sentence on the society's perception of that person. | Classification
`task365_synthetic_remove_vowels` | Given a string remove any vowels in that string. | Answer Generation
`task366_synthetic_return_primes` | Given a list of integers return a number if it is prime. | Answer Generation, Arithemetic 
`task367_synthetic_remove_floats`  | Given a list of numbers remove any number if it is not an integer | Answer Generation, Arithemetic          
`task368_synthetic_even_or_odd_calculation`  | Given a list of integers divide even numbers by *4* and multiply odd numbers by *4* then add *2* | Answer Generation, Arithemetic
`task369_synthetic_remove_odds` | Given a list of integers remove any integer if it is odd | Answer Generation, Arithemetic
`task370_synthetic_remove_divisible_by_3` | Given a list of integers remove any integer if it is divisible by *3* | Answer Generation, Arithemetic
`task371_synthetic_product_of_list` | Given a list of lists of integers, find the product of every inner list | Answer Generation, Arithemetic
`task372_synthetic_palindrome_numbers` | Given a list of integers return an integer if the first and last digit are the same | Answer Generation
`task373_synthetic_round_tens_place` | Given a list of integers round them to the tens place | Answer Generation, Arithemetic
`task374_synthetic_pos_or_neg_calculation`| Given a list of integers multiply the negative integers by *-3* multiply the even integers by *2* | Answer Generation, Arithemetic 
`task375_classify_type_of_sentence_in_debate` | Given a debate topic and a sentence from the debate, classify the type of the sentence. | Classification
`task380_boolq_yes_no_question` | Given a passage and a yes/no question, answer the question based on the passage | Answer Generation
`task381_boolq_question_generation` | Given a passage, generate a yes/no question that can be answered based on the passage | Question Generation
`task382_hybridqa_answer_generation` | Given a question about part-of-speech tag of a word in the question, answer the question | Answer Generation
`task394_persianqa_question_generation` | Given a passage, generate a question based on it | Question Generation
`task395_persianqa_answer_generation` | Given a passage and a question, answer the question based on the passage | Answer Generation
`task396_persianqa_classification` | Given a passage and a question, check whether the question is answerable based on the passage or not | Classification
`task376_reverse_order_of_words` |  Reverse the order of words in the given sentence | Answer Generation
`task377_remove_words_of_given_length` | Remove all words of a given length in the sentence | Answer Generation
`task378_reverse_words_of_given_length` | Reverse all words of a given length in the sentence | Answer Generation
`task379_agnews_topic_classification` | Given a news article, classify the article's topic to four classes. | Classification
`task380_boolq_yes_no_question` | Given a passage and a yes/no question, answer the question based on the passage. | Answer Generation
`task381_boolq_question_generation` | Given a passage, generate a yes/no question that can be answered based on the passage. | Question Generation
`task382_hybridqa_answer_generation` | Given a question about part-of-speech tag of a word in the question, answer the question. | Answer Generation
`task383_matres_classification` | Given a context and a verb, answer if the given verb can be anchored in time or not | Classification
`task386_semeval_2018_task3_irony_detection` | Given a tweet judge whether it contains irony or not. | Classification
`task387_semeval_2018_task3_irony_classification` | Given a tweet Classify the kind of irony it has. | Classification
`task391_causal_relationship` |  Given two sentences, decide whether the second sentence can be the result of the first one. | Classification
`task392_inverse_causal_relationship` |  Given two sentences, decide whether the first sentence can be the result of the second one. | Classification
`task393_plausible_result_generation` | Given a sentence, write another sentence that is a likely result of it. | Text Generation
`task394_persianqa_question_generation` | Given a passage, generate a question based on it. | Question Generation
`task395_persianqa_answer_generation` | Given a passage and a question, answer the question based on the passage. | Answer Generation
`task396_persianqa_classification` | Given a passage and a question, check whether the question is answerable based on the passage or not. | Classification
`task400_paws_paraphrase_classification` | Given two sentences, judge whether they are paraphrases of each other | Classification
`task401_numeric_fused_head_reference` | Given a dialogue and a highlighted number, choose the entity the number refers to from the text | Answer Generation
`task403_creak_commonsense_inference` | Given a statement and a explanation, judge whether the statement is true based on the explanation | Classification
`task424_hindienglish_corpora_hi_en_translation` | Given a Hindi sentence, convert it into English. | Translation
`task425_hindienglish_corpora_en_hi_translation` | Given an English sentence, convert it into Hindi. | Translation
`task426_hindienglish_corpora_hi-en_classification` | Given a Hindi sentence and its corresponding English sentence, classify whether it is correct or not. | Classification
`task427_hindienglish_corpora_hi-en_language_identification` | Given a sentence, identify whether it is in Hindi or English. | Language Identification
`task418_persent_title_generation` | Given a document, generate a short title of the document. | Title Generation
`task419_persent_answer_generation` | Given a document, find the main entity about whom the author is writing. | Answer Generation
`task420_persent_document_sentiment_classification` | Given a document and an entity the task is to select the author's sentiment towards the enity. | Document Sentiment Classification
`task421_persent_sentence_sentiment_classification` | Given a sentence and an entity, the task is to select the author's sentiment towards the enity. | Sentence Sentiment Classification
`task422_persent_sentence_sentiment_verification` | Given a sentence, an entity and its sentiment towards the entity, verify if it is the correct sentiment towards the entity. | Sentence Sentiment Verification
`task423_persent_document_sentiment_verification` | Given a document, an entity and its sentiment towards the entity, verify if it is the correct sentiment towards the entity. | Document Sentiment Verification
`task456_matres_intention_classification` | Given a context and a verb, answer if the given verb is about an intention or not | Classification
`task457_matres_conditional_classification` | Given a context and a verb, answer if the given verb is conditional or not | Classification
`task458_matres_negation_classification` | Given a context and a verb, answer if the given verb is a negation or not | Classification
`task459_matres_static_classification` | Given a context and a verb, answer if the given verb is static or not | Classification
`task460_qasper_answer_generation` | Given a context and a question, answer the question based on the context. | Answer Generation
`task461_qasper_question_generation` | Given a cotext, generate a question based on it. | Question Generation
`task462_qasper_classification` | Given a context and a question, classify the question into abstractive, extractice, or yes-no question | Classification
`task463_parsinlu_entailment_classification` | Given  a premise sentence and a hypothesis sentence, determine whether the hypothesis sentence entails, contradicts, or is neutral with respect to the given premise sentence | Classification
`task464_parsinlu_entailment_sentence_generation` | Given a premise sentence and a label, generate the hypothesis sentence based on the label and the premise sentence | Sentence Generation
`task465_parsinlu_qqp_classification` | Given two sentences, determine whether the sentences are paraphrases or not | Classification
`task466_parsinlu_qqp_text_modification` | Given a sentence, paraphrase it | Text Modification
`task467_parsinlu_rc_answer_generation` | Given a passage and a question, answer the question based on the passage. | Answer Generation
`task468_parsinlu_rc_question_generation` | Given a passage, generate a question based on the passage. | Question Generation
`task475_yelp_polarity_classification` | Classify a given Yelp review to positive or negative sentiment | Classification
`task476_cls_english_books_classification` | Classify a given book product review in English to positive or negative sentiment | Classification
`task477_cls_english_dvd_classification` | Classify a given dvd product review in English to positive or negative sentiment | Classification
`task478_cls_english_music_classification` | Classify a given music product review in English to positive or negative sentiment | Classification
`task479_cls_german_books_classification` | Classify a given book product review in German to positive or negative sentiment | Classification
`task480_cls_german_dvd_classification` | Classify a given dvd product review in German to positive or negative sentiment | Classification
`task481_cls_german_music_classification` | Classify a given music product review in German to positive or negative sentiment | Classification
`task482_cls_french_books_classification` | Classify a given book product review in French to positive or negative sentiment | Classification
`task483_cls_french_dvd_classification` | Classify a given dvd product review in French to positive or negative sentiment | Classification
`task484_cls_french_music_classification` | Classify a given music product review in French to positive or negative sentiment | Classification
`task485_cls_japanese_books_classification` | Classify a given book product review in Japanese to positive or negative sentiment | Classification
`task486_cls_japanese_dvd_classification` | Classify a given dvd product review in Japanese to positive or negative sentiment | Classification
`task487_cls_japanese_music_classification` | Classify a given music product review in Japanese to positive or negative sentiment | Classification
`task512_twitter_emotion_classification` | Given a Twitter post, classify the post's emotion to six classes (sadness, joy, love, anger, fear, surprise) | Classification
`task513_argument_stance_classification` | Given a topic and an argument, decide the stance of the argument towards the topic | Classification
`task514_argument_consequence_classification` | Given a topic and an argument, decide whether the argument refers to a consequence of the topic | Classification
`task517_emo_classify_emotion_of_dialogue` | Classify the emotion of a given dialogue | Classification, Sentiment Analysis
`task518_emo_different_dialogue_emotions` | Given different dialogue determine if they have the same emotion | Classification, Sentiment Analysis
`task519_aquamuse_question_generation` | Given an answer generate a question that would be answered by the answer given | Question Generation
`task520_aquamuse_answer_given_in_passage` | Given a passage and a question determine if the question can be answered by the passage | Classification
`task524_parsinlu_food_aspect_classification` | Given a food review and a question about the reviewer's sentiment toward one aspect of the food, classify the sentiment. | Classification
`task525_parsinlu_movie_aspect_classification` | Given a movie review and a question about the reviewer's sentiment toward one aspect of the movie, classify the sentiment. | Classification
`task526_parsinlu_movie_overal_classification` | Given a movie review, classify the overal sentiment of the reviewer toward the movie. | Classification
`task527_parsinlu_food_overal_classification` | Given a food review, classify the overal sentiment of the reviewer toward the food. | Classification
`task528_parsinlu_movie_aspect_detection` | Given a movie review, extract aspects of the movie mentioned in the text. | Text Generation
`task529_parsinlu_food_aspect_detection` | Given a food review, extract aspects of the food mentioned in the text. | Text Generation
`task530_europarl_en_es_translation` | Given a English sentence, convert it into Spanish. | Translation
`task531_europarl_es_en_translation` | Given an Spanish sentence, convert it into English. | Translation
`task532_europarl_en-es_classification` | Given a English sentence and its corresponding Spanish translation, classify whether it is correct or not. | Classification
`task533_europarl_es-en_language_identification` | Given a sentence, identify  whether it is in English or Spanish. | Language Identification
`task534_farstail_entailment` | Given two sentences in Persian, choose whether they agree, disagree, neither with each other. | Classification
`task573_air_dialogue_classification` | Givena a conversation between a flight 'agent' and the 'customer' classify the goal of the conversation. | Classification
`task574_air_dialogue_sentence_generation` | Given a conversation between a flight 'agent' and the 'customer', find the missing dialogue in the conversation. | Sentence Generation
`task575_air_dialogue_classification` | Classification of the sentence spoken by 'agent' and 'customer'. | Classification
`task576_curiosity_dialogs_answer_generation` | Answering multiple choices dialogue act problems. | Answer Generation
`task577_curiosity_dialogs_classification` | Classification of the sentence spoken by 'assistant' and 'user'. | Classification
`task578_curiosity_dialogs_answer_generation` | Given a conversation between 'assistant' and 'user' classify the context of the conversation | Answer Generation
`task607_sbic_intentional_offense_binary_classification` | Determine whether the post is intentionally offensive or not | Binary Classification
`task608_sbic_sexual_offense_binary_classification` | Determine whether the post is sexually offensive/explicit or not | Binary Classification
`task609_sbic_potentially_offense_binary_classification` | Determine whether the post is potentially offensive or not | Binary Classification
`task610_conllpp_ner` | Recognize and label proper nouns (Named Entity Recognition) | NER/Labeling  
`task563_discofuse_answer_generation` | Answer Generation on Dataset Card for DISCOFUSE | Answer Generation
`task550_discofuse_sentence_generation` | Senetence Generation on Dataset Card for DISCOFUSE | Senetence Generation
`task564_discofuse_classification` | Classification on Dataset Card for DISCOFUSE | Classification
`task562_alt_language_identification` | Language Identification on Dataset Card for ALT | Language Identification
`task535_spl_translation_ch_en` |  Language Translate of Dataset Card for ALT from Chinese language to English language while preserving named entities in the original language | Language Translation
`task536_spl_translation_vi_en` | Language Translate of Dataset Card for ALT from Vietnamese language to English language while preserving named entities in the original language | Language Translation
`task537_spl_translation_th_en` | Language Translate of Dataset Card for ALT from Thai language to English language while preserving named entities in the original language | Language Translation
`task538_spl_translation_bu_en` | Language Translate of Dataset Card for ALT from Burmese language to English language while preserving named entities in the original language | Language Translation
`task539_spl_translation_ma_en` | Language Translate of Dataset Card for ALT from Malay language to English language while preserving named entities in the original language | Language Translation
`task540_spl_translation_la_en` | Language Translate of Dataset Card for ALT from Laotian language to English language while preserving named entities in the original language | Language Translation
`task541_spl_translation_kh_en` | Language Translate of Dataset Card for ALT from Khmer language to English language while preserving named entities in the original language | Language Translation
`task542_spl_translation_ja_en` | Language Translate of Dataset Card for ALT from Japanese language to English language while preserving named entities in the original language | Language Translation
`task543_spl_translation_bh_en` | Language Translate of Dataset Card for ALT from Bahasa language to English language while preserving named entities in the original language | Language Translation
`task544_spl_translation_hi_en` | Language Translate of Dataset Card for ALT from Hindi language to English language while preserving named entities in the original language | Language Translation
`task545_spl_translation_fi_en` | Language Translate of Dataset Card for ALT from Filipino language to English language while preserving named entities in the original language | Language Translation
`task546_spl_translation_bg_en` | Language Translate of Dataset Card for ALT from Bengali language to English language while preserving named entities in the original language | Language Translation
`task547_spl_translation_entk_en` | Language Translate of Dataset Card for ALT from English Tokens to English language while preserving named entities in the original language | Language Translation
`task548_spl_translation_en_ch` | Language Translate of Dataset Card for ALT from English language to Chinese language while preserving named entities in the original language | Language Translation
`task549_spl_translation_en_vi` | Language Translate of Dataset Card for ALT from English language to Vietnamese language while preserving named entities in the original language | Language Translation
`task551_spl_translation_en_th` | Language Translate of Dataset Card for ALT from English language to Thai language while preserving named entities in the original language | Language Translation
`task552_spl_translation_en_bu` | Language Translate of Dataset Card for ALT from English language to Burmese language while preserving named entities in the original language | Language Translation
`task553_spl_translation_en_ma` | Language Translate of Dataset Card for ALT from English language to Malay language while preserving named entities in the original language | Language Translation
`task554_spl_translation_en_la` | Language Translate of Dataset Card for ALT from English language to Laotian language while preserving named entities in the original language | Language Translation
`task555_spl_translation_en_kh` | Language Translate of Dataset Card for ALT from English language to Khmer language while preserving named entities in the original language | Language Translation
`task556_spl_translation_en_ja` | Language Translate of Dataset Card for ALT from English language to Japanese language while preserving named entities in the original language | Language Translation
`task557_spl_translation_en_ba` | Language Translate of Dataset Card for ALT from English language to Bahasa language while preserving named entities in the original language | Language Translation
`task558_spl_translation_en_hi` | Language Translate of Dataset Card for ALT from English language to Hindi language while preserving named entities in the original language | Language Translation
`task559_spl_translation_en_fi` | Language Translate of Dataset Card for ALT from English language to Filipino language while preserving named entities in the original language | Language Translation
`task560_spl_translation_en_entk` | Language Translate of Dataset Card for ALT from English language to English tokens while preserving named entities in the original language | Language Translation
`task561_spl_translation_en_bg` | Language Translate of Dataset Card for ALT from English language to Bengali language while preserving named entities in the original language | Language Translation
`task617_ohsumed_abstract_title_generation` | Generating title to Ohsumed dataset abstracts | Title Generation
`task618_ohsumed_medical_subject_headings_answer_generation` | Generating MESH terms to Ohsumed dataset abstracts | Medical subject heading(MESH) term Generation
`task619_ohsumed_yes_no_numerical_answer_generation` | Generating Yes/No answer to Ohsumed dataset questions | Answer Generation
`task620_onestop_english_readability_classification` | Generating labels to Onestop_english dataset texts | Text classification
`task621_ohsumed_yes_no_answer_generation` | Generating Yes/No answers to Ohsumed dataset questions | Answer Generation
`task622_ohsumed_question_answering` | Given a abstract and question, select the best answer from the given choices. | Answer Generation