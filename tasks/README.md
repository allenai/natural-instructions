## Tasks List

This directory contains the tasks that are part of this benchmark.


Name | Summary | Category | Domain | Input Language | Output Language
---- | ----------- | -------- | ----- | ----- | ----- 
`task001_quoref_question_generation`	| Writing questions that require tracking entity references.	| Contextual Question Generation	| Wikipedia	| English	| English
`task002_quoref_answer_generation`	| Answering questions that require tracking entity references.	| Answer Generation -> Contextual Question Answering	| Wikipedia	| English	| English
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
`task046_miscellaneous_question_typing`	| Annotating question-answer pairs with their corresponding type(s).	| Classification
`task047_miscellaneous_answering_science_questions`	| Answering simple science questions.	| Answer Generation
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
`task063_first_i_elements` | Given a list return the first i elements of the list | Answer Generation
`task064_all_elements_except_first_i` | Given a list return all the elements of the list except the first i elements | Answer Generation
`task065_timetravel_consistent_sentence_classification`	| Choosing the option that makes a given short story consistent. | Classification
`task066_timetravel_binary_consistency_classification`	| Identifying if the given sentence is consistent with the given story. | Classification
`task067_abductivenli_answer_generation`	|  Generating text that completes a story based on the beginning and ending.	| Answer Generation
`task068_abductivenli_incorrect_answer_generation`	|  Generating text that modifies a story to be incorrect based on the beginning, middle, and ending.	| Answer Generation
`task069_abductivenli_classification`	|  Choosing text that completes a story based on given beginning and ending.	| Classification
`task070_abductivenli_incorrect_classification`	|  Choosing text that incorrectly completes a story based on given beginning and ending.	| Classification
`task071_abductivenli_answer_generation`	|  Generating text that completes a story based on given beginning and middle.	| Answer Generation
`task072_abductivenli_answer_generation`	|  Generating text that completes a story based on given middle and ending.	| Answer Generation
`task073_commonsenseqa_answer_generation` | Answer questions based on commonsense knowledge. | Answer Generation
`task074_squad1.1_question_generation`	| Generate guestions based on SQuAD 1.1.	| Contextual Question Generation	| Wikipedia	| English	| English
`task075_squad1.1_answer_generation`	| Generate answers to SQuAD 1.1 questions.	| Answer Generation -> Contextual Question Answering	| Wikipedia	| English	| English
`task076_splash_correcting_sql_mistake` | Correct the mistake in a given SQL statement based on feedback. | Structured Query Generation, Text Modification
`task077_splash_explanation_to_sql` | Generate a SQL statement based on a description of what the SQL statement does. | Structured Query Generation
`task078_all_elements_except_last_i` | Given a list return all the elements of the list except the last i elements | Answer Generation
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
`task091_all_elements_from_index_i_to_j` | Given a list return all the elements starting from ith element and ending at jth element | Answer Generation
`task092_check_prime_classification`	|  Identify whether the number is prime or not.	| Mathematics
`task093_conala_normalize_lists` | Given a list of numbers, normalize the list such that the result adds to 1. | Answer Generation, Arithmetic
`task094_conala_calculate_mean` | Given a list of numbers, calculate the mean of the list. | Answer Generation, Arithmetic
`task095_conala_max_absolute_value` | Given a list of numbers, calculate the element with the largest absolute value. | Answer Generation, Arithmetic
`task096_conala_list_index_subtraction` | Given a list of numbers, subtract each element by its index in the list. | Answer Generation, Arithmetic
`task097_conala_remove_duplicates` | Given a list of numbers, remove all of the duplicates in the list. | Text Modification, Arithmetic
`task098_conala_list_intersection` | Given a two lists of numbers, find the intersection of the two lists. | Answer Generation, Arithmetic
`task099_reverse_elements_between_index_i_and_j` | Given a list return all the elements starting from ith element and ending at jth element in reverse order | Answer Generation
`task100_concatenate_all_elements_from_index_i_to_j` | Given a list concatenate all the elements starting from ith element and ending at jth element | Answer Generation
`task101_reverse_and_concatenate_all_elements_from_index_i_to_j` | Given a list reverse and then concatenate all the elements starting from ith element and ending at jth element | Answer Generation
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
`task119_zest_text_modification` | Paraphrase the given question. | Paraphrasing
`task120_zest_text_modification` | Given a question, change the answer with minimum changes. | Question Generation
`task121_zest_text_modification` | Given some questions, combine them to have one new question. | Question Composition
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
`task200_mnli_entailment_classification` | Given a context statement and three sentences as choices, select the sentence that agrees with the context statement. | Question Answering -> Multiple Choice Question Answering, Reasoning->Deductive reasoning
`task201_mnli_neutral_classification` | Given a context statement and three sentences as choices, select the sentence that neither clearly agrees nor disagrees with the context statement. | Multiple Choice Question Answering, Deductive reasoning, Commonsense Reasoning
`task202_mnli_contradiction_classification` | Given a context statement and 3 sentences as choices, choose the sentence that clearly disagrees with the context statement. | Multiple Choice Question Answering, Deductive reasoning, Commonsense Reasoning
`task203_mnli_sentence_generation` | Given a context statement, genre, and label indicating agree/disagree/neither with respect to the context statement, generate a sentence that follows the genre and label specifications. | Sentence Generation
`task204_mnli_same_genre_classification` | Given two sentences and the genre they should belong to, determine if they belong to the same genre or not. | Classification
`task205_remove_even_elements` | Given a list of integers, remove all elements that are even. | Answer Generation, Arithmetic, Numerical Reasoning
`task206_collatz_conjecture` | Given a list of integers, compute the next number in the *3n+1* problem. | Answer Generation, Arithmetic, Numerical Reasoning
`task207_max_element_lists` | Given a list of lists of integers compute the max value for each list. | Answer Generation, Arithmetic, Numerical Reasoning
`task208_combinations_of_list` | Given a list of integers of length *n*, find all possible combinations without replacement of length *n-1*. | Answer Generation, Combinatorics
`task209_stancedetection_classification` | Given a topic and an argument, detect whether topic is in favor or against in the argument. | Classification
`task210_logic2text_structured_text_generation` | Given a natural language interpretation, generate a command using logical operations. | Structured Text Generation
`task211_logic2text_classification` | Given a command and corresponding interpretation, classify whether it is the right interpretation or not. | Classification
`task212_logic2text_classification` | Given a command, classify the command in one of seven logic types. | Classification
`task213_rocstories_correct_ending_classification` | Given the title and the first four sentences of a five sentence story, choose the correct story ending. | Analogical Reasoning, Multiple Choice Question Answering
`task214_rocstories_incorrect_ending_classification` | Given the title and the first four sentences of a five sentence story, choose the incorrect story ending. | Analogical Reasoning, Multiple Choice Incorrect Answer Generation
`task215_rocstories_incorrect_answer_generation` | Given the title and the first four sentences of a five sentence story, write an incorrect story ending. | Analogical Reasoning, Comprehensive Incorrect Answer Generation
`task216_rocstories_correct_answer_generation` | Given the title and the first four sentences of a five sentence story, write a correct story ending. | Story Ending Generation
`task217_rocstories_ordering_answer_generation` | Given a five sentence story in shuffled order and the title, put the story in the correct order. | Order Generation
`task218_rocstories_swap_order_answer_generation` | Given a five sentence story and the title, determine which two sentences must be swapped so that the story makes complete sense. | Wrong Order Detection
`task219_rocstories_title_answer_generation` | Given a five sentence story, generate an appropriate title for the story. | Title Generation
`task220_rocstories_title_classification` | Given a five sentence story, choose an appropriate title for the story from the given options. | Topic Generation, Multiple Choice Question Answering
`task221_rocstories_two_choice_classification` | Given three sentences and title of a five sentence story, choose which two sentences from the options given will complete the story. | Multiple Choice Question Answering
`task222_rocstories_two_chioce_slotting_classification` | Given three sentences and title of a five sentence story, choose which two sentences from the given options will complete the story. | Multiple Choice Question Answering, Order Generation
`task223_quartz_explanation_generation` | Given a question and its answer, generate an explanation statement. | Explanation Generation
`task224_scruples_anecdotes_ethical_judgment` | Given an anecdote, judge whether the author is ethically correct or not. | Ethical Judgment
`task225_english_language_answer_generation` | Given a basic English language related question generate the answer with proper context, definitions, and examples. | Open Question Answering
`task226_english_language_answer_relevance_classification` | Given a question and answer pair, detect whether the answer is acceptable or not. | Classification
`task227_clariq_classification`	| Given a query and its clarification, classify whether clarification is proper or not by providing 'Yes' or 'No'. | Classification
`task228_arc_answer_generation_easy` | Given a easy science question, provide the answer based on scientific facts and reasoning. | Reasoning, Multiple Choice Question Answering
`task229_arc_answer_generation_hard` | Given a hard science question, provide the answer based on scientific facts and reasoning. | Reasoning, Multiple Choice Question Answering
`task230_iirc_passage_classification` | Given 3 passages and a question, determine which passage can be used to answer the question. | Reasoning, Multiple Choice Question Answering
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
`task264_paper_reviews_accept_or_reject_classification` | Given a set of reviews, classify paper into accept or reject | Classification
`task265_paper_reviews_language_identification` | Given a paper review, identify it is in the english or spanish language | Language Identification
`task266_paper_reviews_reviewer_perspective_classification` | Given a paper review, classify into five evaluation metric | Classification
`task267_concatenate_and_reverse_all_elements_from_index_i_to_j` | Given a list concatenate and then mirror/reverse all the elements starting from ith element and ending at jth element | Answer Generation
`task268_casehold_legal_answer_generation` | Given a prompt from a judicial decision and multiple potential holdings, choose the correct option. | Answer Generation
`task269_csrg_counterfactual_story_generation` | Given premise, initial context with ending, and counterfactul context, generate new story ending supporting counterfactual. | Answer generation
`task270_csrg_counterfactual_context_generation` | Given premise, initial context with ending, and new counterfactul ending, generate counterfactual context which supports the new story ending. 
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
`task292_storycommonsense_character_text_generation` | Given a short story, provide all the characters in that story. | Text Generation
`task293_storycommonsense_emotion_text_generation` | Given a sentence, context (optional) and character; provide emotions expressed by the character in the sentence. | Text Generation
`task294_storycommonsense_motiv_text_generation` | Given a sentence, context (optional) and character; provide motivation of the character in the sentence. | Text Generation
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
`task309_race_answer_generation` | Given an article, a question and four options; provide correct answer for the question based on the article. | Answer Generation
`task310_race_classification` | Given an article, a question and four options; provide incorrect answer for the question based on the article. | Classification
`task311_race_question_generation` | Generate a question based on the given article and an answer. | Question Generation
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
`task340_winomt_classification_gender_pro` | Given a sentence and a profession that is mentioned in the sentence, identify its gender. pro means the gender aggrees with the cultural stereotype of the profession | classification
`task341_winomt_classification_gender_anti` | Given a sentence and a profession that is mentioned in the sentence, identify its gender. anti means the gender disagrees with the cultural stereotype of the profession | classification
`task342_winomt_classification_profession_pro` | Given a sentence and a gender, identify the profession mentioned in the sentence with the given gender. pro means the gender aggrees with the cultural stereotype of the profession | classification
`task343_winomt_classification_profession_anti` | Given a sentence and a gender, identify the profession mentioned in the sentence with the given gender. anti means the gender disaggrees with the cultural stereotype of the profession | classification
`task344_hybridqa_answer_generation` | Given a question, answer the question based on your knowledge. | Answer Generation
`task345_hybridqa_answer_generation` | Given a question, write the part-of-speech tag for each word in the question. | Answer Generation
`task346_hybridqa_classification` | Given a question, a word, and a POS tag, determine whether the POS tag is True or False based on the part-of-speech tag of the given word in the question. | Classification
`task347_hybridqa_incorrect_answer_generation` | Given a question about part-of-speech tag of a word in the question, write an implausible POS tag to the question. | Incorrect Answer Generation
`task348_squad2.0_unanswerable_question_generation` | Given a passage, generate a question that cannot be answered based on the passage. | Unanswerable Question Generation
`task349_squad2.0_answerable_unanswerable_question_classification` | Given a passage and a question, classify whether or not the question is answerable from the passage. | Classification
`task350_winomt_classification_gender_identifiability_pro` | Given a sentence and a profession, identify whether the profession's gender is identifiable. pro means the gender agrees with the cultural stereotype of the profession | classification
`task351_winomt_classification_gender_identifiability_anti` | Given a sentence and a profession, identify whether the profession's gender is identifiable. anti means the gender disagrees with the cultural stereotype of the profession | classification
`task352_coda-19_classification` | given a paragraph, classify into these categories: background, purpose, method, finding/contribution, and other. | Classification
`task353_casino_classification_negotiation_elicit_pref` | Detecting the usage of elicit-pref negotiation strategy in dialogue utterances. | Classification
`task354_casino_classification_negotiation_no_need` | Detecting the usage of no-need negotiation strategy in dialogue utterances. | Classification
`task355_casino_classification_negotiation_other_need` | Detecting the usage of other-need negotiation strategy in dialogue utterances. | Classification
`task356_casino_classification_negotiation_self_need` | Detecting the usage of self-need negotiation strategy in dialogue utterances. | Classification
`task357_casino_classification_negotiation_small_talk` | Detecting the usage of small-talk negotiation strategy in dialogue utterances. | Classification
`task358_casino_classification_negotiation_uv_part` | Detecting the usage of uv-part negotiation strategy in dialogue utterances. | Classification
`task359_casino_classification_negotiation_vouch_fair` | Detecting the usage of vouch-fair negotiation strategy in dialogue utterances. | Classification
`task360_spolin_yesand_response_generation` | Given a prompt, generate the "yes, ands" response | Response Generation
`task361_spolin_yesand_prompt_response_classification` | Given a prompt and a response, classify whether the response is "yes, ands" type | Classification
`task362_spolin_yesand_prompt_response_sub_classification` | Given a prompt and two responses, identify which response is "yes, ands" type | Classification
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
`task376_reverse_order_of_words` |  Reverse the order of words in the given sentence | Answer Generation
`task377_remove_words_of_given_length` | Remove all words of a given length in the sentence | Answer Generation
`task378_reverse_words_of_given_length` | Reverse all words of a given length in the sentence | Answer Generation
`task379_agnews_topic_classification` | Given a news article, classify the article's topic to four classes. | Classification
`task380_boolq_yes_no_question` | Given a passage and a yes/no question, answer the question based on the passage | Answer Generation
`task381_boolq_question_generation` | Given a passage, generate a yes/no question that can be answered based on the passage | Question Generation
`task382_hybridqa_answer_generation` | Given a question about part-of-speech tag of a word in the question, answer the question | Answer Generation
`task383_matres_classification` | Given a context and a verb, answer if the given verb can be anchored in time or not | Classification
`task384_socialiqa_question_classification` | You're given context, an answer and question. Your task is to classify whether the question is correct or not. | Classification
`task385_socialiqa_incorrect_answer_generation` | You're given a context, a question, three options. Your task is to return an incorrect answer from the option. | Incorrect Answer Generation
`task386_semeval_2018_task3_irony_detection` | Given a tweet judge whether it contains irony or not. | Classification
`task387_semeval_2018_task3_irony_classification` | Given a tweet Classify the kind of irony it has. | Classification
`task388_torque_token_classification` | Given a passage, identify a token from the passage representing an event | Token Classification
`task389_torque_generate_temporal_question` | Given a passage, generate a temporal question | Question Generation
`task390_torque_text_span_selection` | Given a passage, a temporal question and a list of events in the passage, return a text span from the list of events that answers the given question | Text Span Selection
`task391_causal_relationship` |  Given two sentences, decide whether the second sentence can be the result of the first one. | Classification
`task392_inverse_causal_relationship` |  Given two sentences, decide whether the first sentence can be the result of the second one. | Classification
`task393_plausible_result_generation` | Given a sentence, write another sentence that is a likely result of it. | Text Generation
`task394_persianqa_question_generation` | Given a passage, generate a question based on it. | Question Generation
`task395_persianqa_answer_generation` | Given a passage and a question, answer the question based on the passage | Answer Generation
`task396_persianqa_classification` | Given a passage and a question, check whether the question is answerable based on the passage or not | Classification
`task397_semeval_2018_task1_tweet_anger_detection` | Given a tweet judge whether the author was angry or not | Classification
`task398_semeval_2018_task1_tweet_joy_detection` | Given a tweet judge whether the author was happy or not | Classification
`task399_semeval_2018_task1_tweet_sadness_detection` | Given a tweet judge whether the author was sad or not | Classification
`task400_paws_paraphrase_classification` | Given two sentences, judge whether they are paraphrases of each other | Classification
`task401_numeric_fused_head_reference` | Given a dialogue and a highlighted number, choose the entity the number refers to from the text | Answer Generation
`task402_grailqa_paraphrase_generation` | Given a question and answer pair, paraphrase the question. | Text Generation
`task403_creak_commonsense_inference` | Given a statement and a explanation, judge whether the statement is true based on the explanation | Classification
`task404_grailqa_paraphrase_validation` | Given two questions, decide whether the second one is a valid paraphrase of the first one | Classification
`task405_narrativeqa_question_generation` | Given a plot summary, create questions that can be answered based on it | Question Generation
`task406_mickey_fr_sentence_perturbation_generation` | Given a sentence in French, perform perturbations and generate new sentence in French. | Sentence Generation
`task407_mickey_hi_sentence_perturbation_generation` | Given a sentence in Hindi, perform perturbations and generate new sentence in Hindi. | Sentence Generation
`task408_mickey_it_sentence_perturbation_generation` | Given a sentence in Italian, perform perturbations and generate new sentence in Italian. | Sentence Generation
`task409_mickey_nl_sentence_perturbation_generation` | Given a sentence in Dutch, perform perturbations and generate new sentence in Dutch. | Sentence Generation
`task410_mickey_ru_sentence_perturbation_generation` | Given a sentence in Russian, perform perturbations and generate new sentence in Russian. | Sentence Generation
`task411_mickey_vi_sentence_perturbation_generation` | Given a sentence in Vietnamese, perform perturbations and generate new sentence in Vietnamese. | Sentence Generation
`task412_mickey_zh_sentence_perturbation_generation` | Given a sentence in Chinese, perform perturbations and generate new sentence in Chinese. | Sentence Generation
`task413_mickey_en_sentence_perturbation_generation` | Given a sentence in English, perform perturbations and generate new sentence in English. | Sentence Generation
`task414_mickey_ar_sentence_perturbation_generation` | Given a sentence in Arabic, perform perturbations and generate new sentence in Arabic. | Sentence Generation
`task415_mickey_bg_sentence_perturbation_generation` | Given a sentence in Bulgarian, perform perturbations and generate new sentence in Bulgarian. | Sentence Generation
`task416_mickey_de_sentence_perturbation_generation` | Given a sentence in German, perform perturbations and generate new sentence in German. | Sentence Generation
`task417_mickey_es_sentence_perturbation_generation` | Given a sentence in Spanish, perform perturbations and generate new sentence in Spanish. | Sentence Generation
`task418_persent_title_generation` | Given a document, generate a short title of the document. | Title Generation
`task419_persent_answer_generation` | Given a document, find the main entity about whom the author is writing. | Answer Generation
`task420_persent_document_sentiment_classification` | Given a document and an entity the task is to select the author's sentiment towards the enity. | Document Sentiment Classification
`task421_persent_sentence_sentiment_classification` | Given a sentence and an entity, the task is to select the author's sentiment towards the enity. | Sentence Sentiment Classification
`task422_persent_sentence_sentiment_verification` | Given a sentence, an entity and its sentiment towards the entity, verify if it is the correct sentiment towards the entity. | Sentence Sentiment Verification
`task423_persent_document_sentiment_verification` | Given a document, an entity and its sentiment towards the entity, verify if it is the correct sentiment towards the entity. | Document Sentiment Verification
`task424_hindienglish_corpora_hi_en_translation` | Given a Hindi sentence, convert it into English. | Translation
`task425_hindienglish_corpora_en_hi_translation` | Given an English sentence, convert it into Hindi. | Translation
`task426_hindienglish_corpora_hi-en_classification` | Given a Hindi sentence and its corresponding English sentence, classify whether it is correct or not. | Classification
`task427_hindienglish_corpora_hi-en_language_identification` | Given a sentence, identify whether it is in Hindi or English. | Language Identification
`task428_senteval_inversion` | Given a sentence, judge whether or not two consecutive word have been inverted. | Classification
`task429_senteval_tense` | Given a sentence, specify the tense of the main verb. | Classification
`task430_senteval_subject_count` | Given a sentence, specify singularity or plurality of the subject. | Classification
`task431_senteval_object_count` | Given a sentence, specify singularity or plurality of the object. | Classification
`task432_alt_en_hi_translation` | Given an English language sentence translate it into Hindi language. | Translation
`task433_alt_hi_en_translation` | Given an Hindi language sentence translate it into English language. | Translation
`task434_alt_en_hi_answer_generation` | Generate answer yes or no for english and hindi translation pair. | Answer Generation
`task435_alt_en_ja_translation` | Given an English language sentence translate it into Japanese language. | Translation
`task436_alt_ja_en_translation` | Given an Japanese language sentence translate it into English language. | Translation
`task437_alt_en_ja_answer_generation` | Generate answer yes or no for english and japanese translation pair. | Answer Generation
`task438_eng_guj_parallel_corpus_en_gu_translation` | Translation from English to Gujarati sentences. | Translation
`task439_eng_guj_parallel_corpus_gu_en_translation` | Translation from Gujarati to English sentences. | Translation
`task440_eng_guj_parallel_corpus_gu-en_classification` | Given a sentence in Gujarati and its corresponding English translation, verify that the translation is correct. | Classification
`task441_eng_guj_parallel_corpus_gu-en_language_identification` | Given a sentence, identify if it is in the English or Gujarati language. | Language Identification
`task442_com_qa_paraphrase_question_generation` | Generating paraphrases of com_qa questions | Question Generation
`task443_com_qa_ans_question_generation` | Generating questions for com_qa answers | Question Generation
`task444_com_qa_question_paraphrases_answer_generation` | Generating answers for com_qa question paraphrases | Answer Generation
`task445_com_qa_wikipedia_answer_generation` | Generating wikipedia links for com_qa questions | Answer Generation
`task446_opus_paracrawl_en_so_translation` | Translating English text to Somali | Translation
`task447_opus_paracrawl_classification` | Generating the language of the text | Classification
`task448_opus_paracrawl_en_tl_translation` | Translating English text to Tagalog | Translation
`task449_opus_paracrawl_ig_en_translation` | Translating Igbo text to English | Translation
`task450_opus_paracrawl_so_en_translation` | Translating Somali text to English | Translation
`task451_opus_paracrawl_tl_en_translation` | Translating Tagalog text to English | Translation
`task452_opus_paracrawl_en_ig_translation` | Translating English text to Igbo | Translation
`task453_swag_answer_generation` | Given a statement context, complete the partial next sentence | Answer Generation
`task454_swag_incorrect_answer_generation` | Given a statement context, complete the partial next sentence with incorrect statement | Incorrect Answer Generation
`task455_swag_context_generation` | Given a statement, generate its context or previous statement | Answer Generation
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
`task469_mrqa_answer_generation` | Generating answers from MRQA OOD dataset | Answer Generation  
`task470_mrqa_question_generation` | Generating question using context passage from MRQA OOD dataset | Question Generation
`task471_haspart_answer_generation` | Generating entity which is in has-part-relationship with input entity | Answer Generation  
`task472_haspart_classification` | Identifying whether given two entities has in-part-relationship or not.  | Classification
`task473_parsinlu_mc_classification` | Given a question, pick the correct option among a list of multiple candidates. | Multiple-Choice Question
`task474_parsinlu_mc_classification` | Given a question, classify the question based on the required knowledge. | Classification
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
`task488_extract_all_alphabetical_elements_from_list_in_order` | Given a list return all the alphabetical elements from the list in same order as they appear in the list | Answer Generation
`task489_mwsc_question_generation` | Generating questions based on the given sentence | Question Generation  
`task490_mwsc_options_generation` | Generating options to mwsc questions | Options Generation
`task491_mwsc_answer_generation` | Generating answers to mwsc questions | Answer Generation  
`task492_mwsc_incorrect_answer_generation` | Generating incorrect answers to mwsc questions | Incorrect Answer Generation
`task493_review_polarity_classification` | Classify amazon review into positive or negative | Classification
`task494_review_polarity_answer_generation` | Given pair of amazon review and polarity, generate True or False when a review matches polarity | Answer Generation
`task495_semeval_headline_classification` | Classify edited news headlines into funny and not funny | Classification
`task496_semeval_answer_generation` | Generate answer yes or no based on given edited sentence and label | Answer Generation
`task497_extract_all_numbers_from_list_in_order` | Given a list return all the numbers from the list in same order as they appear in the list | Answer Generation
`task498_scruples_anecdotes_whoiswrong_classification` | Given a real-life anecdote of a complex ethical situation, identify who is ethically wrong here | Classification
`task499_extract_and_add_all_numbers_from_list` | Given a list extract all the numbers from the list and return their sum/addition | Answer Generation
`task500_scruples_anecdotes_title_generation` | Given a real-life anecdote of a complex ethical situation, generate a title that describes the main event/root cause of the situation | Title Generation
`task501_scruples_anecdotes_post_type_verification` | Given a real-life anecdote of a complex ethical situation, verify if the claim about the type of the post is true or not | Verification
`task502_scruples_anecdotes_whoiswrong_verification` | Given a real-life anecdote of a complex ethical situation, verify who is wrong in the situation | Verification
`task503_scruples_anecdotes_isanswerable` | Given a real-life anecdote of a complex ethical situation, can it be clearly answered, who is ethically wrong here ? | Binary Classification
`task504_count_all_alphabetical_elements_in_list` | Given a list return the count of all the alphabetical elements from the list | Answer Generation
`task505_count_all_numerical_elements_in_list` | Given a list return the count of all the numerical elements from the list | Answer Generation
`task506_position_of_all_alphabetical_elements_in_list` | Given a list return the position of all the alphabetical elements from the list | Answer Generation
`task507_position_of_all_numerical_elements_in_list` | Given a list return the position of all the numerical elements from the list | Answer Generation
`task508_scruples_dilemmas_more_ethical_isidentifiable` | Given a pair of action statements, can you conclusively identify which statement is less ethical or not ? | Verification
`task509_collate_of_all_alphabetical_and_numerical_elements_in_list_separately` | Given a list collate all the alphabetical elements at the start of the list followed by all the numerical elements of the list | Answer Generation
`task510_reddit_tifu_title_summarization` | Given the text of a social media post, generate a title summarizing the post | Summarization 
`task511_reddit_tifu_long_text_summarization` | Given the text of a social media post, generate a short summary the post | Summarization 
`task512_twitter_emotion_classification` | Given a Twitter post, classify the post's emotion to six classes (sadness, joy, love, anger, fear, surprise) | Classification
`task513_argument_stance_classification` | Given a topic and an argument, decide the stance of the argument towards the topic | Classification
`task514_argument_consequence_classification` | Given a topic and an argument, decide whether the argument refers to a consequence of the topic | Classification
`task515_senteval_odd_word_out` | Given a sentence judge whether a single word has been replaced with another word. | Classification
`task516_senteval_conjoints_inversion` | Given a sentence judge whether two clausal conjoints have been inverted. | Classification
`task517_emo_classify_emotion_of_dialogue` | Classify the emotion of a given dialogue | Classification, Sentiment Analysis
`task518_emo_different_dialogue_emotions` | Given different dialogue determine if they have the same emotion | Classification, Sentiment Analysis
`task519_aquamuse_question_generation` | Given an answer generate a question that would be answered by the answer given | Question Generation
`task520_aquamuse_answer_given_in_passage` | Given a passage and a question determine if the question can be answered by the passage | Classification
`task521_trivia_question_classification` | Given a text from a trivia quiz, decide the category the question belongs to | Classification
`task522_news_editorial_summary` Given an article text, select spans of text that show a summary of the thesis of the article. | Summarization
`task523_find_if_numbers_or_alphabets_are_more_in_list` | Given a list find if the count of alphabets is more, less, or same as that of numbers in the list | Answer Generation
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
`task535_alt_translation_ch_en` |  Language Translate of Dataset Card for ALT from Chinese language to English language while preserving named entities in the original language | Language Translation
`task536_alt_translation_vi_en` | Language Translate of Dataset Card for ALT from Vietnamese language to English language while preserving named entities in the original language | Language Translation
`task537_alt_translation_th_en` | Language Translate of Dataset Card for ALT from Thai language to English language while preserving named entities in the original language | Language Translation
`task538_alt_translation_bu_en` | Language Translate of Dataset Card for ALT from Burmese language to English language while preserving named entities in the original language | Language Translation
`task539_alt_translation_ma_en` | Language Translate of Dataset Card for ALT from Malay language to English language while preserving named entities in the original language | Language Translation
`task540_alt_translation_la_en` | Language Translate of Dataset Card for ALT from Laotian language to English language while preserving named entities in the original language | Language Translation
`task541_alt_translation_kh_en` | Language Translate of Dataset Card for ALT from Khmer language to English language while preserving named entities in the original language | Language Translation
`task542_alt_translation_ja_en` | Language Translate of Dataset Card for ALT from Japanese language to English language while preserving named entities in the original language | Language Translation
`task543_alt_translation_bh_en` | Language Translate of Dataset Card for ALT from Bahasa language to English language while preserving named entities in the original language | Language Translation
`task544_alt_translation_hi_en` | Language Translate of Dataset Card for ALT from Hindi language to English language while preserving named entities in the original language | Language Translation
`task545_alt_translation_fi_en` | Language Translate of Dataset Card for ALT from Filipino language to English language while preserving named entities in the original language | Language Translation
`task546_alt_translation_bg_en` | Language Translate of Dataset Card for ALT from Bengali language to English language while preserving named entities in the original language | Language Translation
`task547_alt_translation_entk_en` | Language Translate of Dataset Card for ALT from English Tokens to English language while preserving named entities in the original language | Language Translation
`task548_alt_translation_en_ch` | Language Translate of Dataset Card for ALT from English language to Chinese language while preserving named entities in the original language | Language Translation
`task549_alt_translation_en_vi` | Language Translate of Dataset Card for ALT from English language to Vietnamese language while preserving named entities in the original language | Language Translation
`task550_discofuse_sentence_generation` | Senetence Generation on Dataset Card for DISCOFUSE | Senetence Generation
`task551_alt_translation_en_th` | Language Translate of Dataset Card for ALT from English language to Thai language while preserving named entities in the original language | Language Translation
`task552_alt_translation_en_bu` | Language Translate of Dataset Card for ALT from English language to Burmese language while preserving named entities in the original language | Language Translation
`task553_alt_translation_en_ma` | Language Translate of Dataset Card for ALT from English language to Malay language while preserving named entities in the original language | Language Translation
`task554_alt_translation_en_la` | Language Translate of Dataset Card for ALT from English language to Laotian language while preserving named entities in the original language | Language Translation
`task555_alt_translation_en_kh` | Language Translate of Dataset Card for ALT from English language to Khmer language while preserving named entities in the original language | Language Translation
`task556_alt_translation_en_ja` | Language Translate of Dataset Card for ALT from English language to Japanese language while preserving named entities in the original language | Language Translation
`task557_alt_translation_en_ba` | Language Translate of Dataset Card for ALT from English language to Bahasa language while preserving named entities in the original language | Language Translation
`task558_alt_translation_en_hi` | Language Translate of Dataset Card for ALT from English language to Hindi language while preserving named entities in the original language | Language Translation
`task559_alt_translation_en_fi` | Language Translate of Dataset Card for ALT from English language to Filipino language while preserving named entities in the original language | Language Translation
`task560_alt_translation_en_entk` | Language Translate of Dataset Card for ALT from English language to English tokens while preserving named entities in the original language | Language Translation
`task561_alt_translation_en_bg` | Language Translate of Dataset Card for ALT from English language to Bengali language while preserving named entities in the original language | Language Translation
`task562_alt_language_identification` | Language Identification on Dataset Card for ALT | Language Identification
`task563_discofuse_answer_generation` | Answer Generation on Dataset Card for DISCOFUSE | Answer Generation
`task564_discofuse_classification` | Classification on Dataset Card for DISCOFUSE | Classification
`task565_circa_answer_generation` | Given a question generate an answer that is relevant to the question. | Answer Generation
`task566_circa_classification` | Given two sentences, check if they have the same meaning. | Classification
`task567_circa_text_generation` | Given a question, Predict the context of the given question. | Text Generation
`task568_circa_question_generation` | Given an answer, Predict the question. | Question Generation
`task569_recipe_nlg_text_generation` | Predict the title given its required ingredients and directions. | Text Generation
`task570_recipe_nlg_ner_generation` | Generate the ner given its required ingredients given. | ner Generation
`task571_recipe_nlg_ner_generation` | Generate the ner given its directions. | ner Generation
`task572_recipe_nlg_text_generation` |  Generate the unknown step by knowing the other steps given in the directions. | Text Generation
`task573_air_dialogue_classification` | Givena a conversation between a flight 'agent' and the 'customer' classify the goal of the conversation. | Classification
`task574_air_dialogue_sentence_generation` | Given a conversation between a flight 'agent' and the 'customer', find the missing dialogue in the conversation. | Sentence Generation
`task575_air_dialogue_classification` | Classification of the sentence spoken by 'agent' and 'customer'. | Classification
`task576_curiosity_dialogs_answer_generation` | Answering multiple choices dialogue act problems. | Answer Generation
`task577_curiosity_dialogs_classification` | Classification of the sentence spoken by 'assistant' and 'user'. | Classification
`task578_curiosity_dialogs_answer_generation` | Given a conversation between 'assistant' and 'user' classify the context of the conversation | Answer Generation
`task579_socialiqa_classification` | Given a context, a question and an answer; classify whether the answer is correct or not. | Classification
`task580_socialiqa_answer_generation` | Given a context, a question and three options; provide correct answer for the question based on the context. | Answer Generation
`task581_socialiqa_question_generation` | Generate a question based on the given context and an answer. | Question Generation
`task582_naturalquestion_answer_generation` | You are given an open-domain question and return an answer based on factual information | Answer Generation
`task583_udeps_eng_coarse_pos_tagging` | Given a sentence, a word in that sentence and the position of that word in the sentence, find the parts-of-speech tag of the word | Classification
`task584_udeps_eng_fine_pos_tagging` | Given a sentence, a word in that sentence and the position of that word in the sentence, find the parts-of-speech tag of the word | Classification
`task585_preposition_classification` | Given two words, you have to generate which preposition connects both. | Classification
`task586_amazonfood_polarity_classification` | Given a review of an amazon food product, you have to classify if the review is positive or negative. | Classification
`task587_amazonfood_polarity_correction_classification` | Given a review of amazon food products and it's polarity, you have to classify whether the polarity is correct or not. | Classification
`task588_amazonfood_rating_classification` | Given a review of amazon food products, you have to classify the rating out of 5. | Classification
`task589_amazonfood_summary_text_generation` | Given a review of amazon's food product, you have to generate the summary of the review. | Text Generation
`task590_amazonfood_summary_correction_classification` | Given a review of amazon's food product and its summary, you have to classify whether the summary is correct or not. | Classification
`task591_sciq_answer_generation` | Given a scientific question, generate a correct answer to the given question | Answer Generation
`task592_sciq_incorrect_answer_generation` | Given a scientific question, generate an incorrect answer to the given question | Incorrect Answer Generation
`task593_sciq_explanation_generation` | Given a scientific question and its correct answer, generate supporting facts for the answer. | Explanation Generation
`task594_sciq_question_generation` | Given a scientific passage and an answer, generate a question for the given answer. | Question Generation
`task595_mocha_answer_generation` | Generating answers to MOCHA questions | Answer Generation
`task596_mocha_question_generation` | Generating questions based on MOCHA | Question Generation
`task597_cuad_answer_generation` | Generating answers to CUAD questions | Answer Generation
`task598_cuad_answer_generation` | Generating starting index of the answers to CUAD questions | Answer Generation
`task599_cuad_question_generation` | Generating questions based on CUAD | Question Generation
`task600_find_the_longest_common_substring_in_two_strings` | Given two strings return the longest common substring in those two strings | Answer Generation
`task601_flores_translation_sntoen` | Translating the text from sinhali to english | Translation
`task602_wikitext-103_answer_generation` | Generate title for the given passage| Answer Generation
`task603_wikitext-103_fill_in_the_blank` | Filling the blanks in the given passage text | Question Answering -> Fill in the Blank
`task604_flores_translation_entosn` | Translating the text from english to sinhali | Translation
`task605_find_the_longest_common_subsequence_in_two_lists` | Given two lists return the longest common subsequence in those two lists | Answer Generation
`task606_sum_of_all_numbers_in_list_between_positions_i_and_j` | Given a list extract and then return sum of all the numbers between two positions i and j | Answer Generation
`task607_sbic_intentional_offense_binary_classification` | Determine whether the post is intentionally offensive or not | Binary Classification
`task608_sbic_sexual_offense_binary_classification` | Determine whether the post is sexually offensive/explicit or not | Binary Classification
`task609_sbic_potentially_offense_binary_classification` | Determine whether the post is potentially offensive or not | Binary Classification
`task610_conllpp_ner` | Recognize and label proper nouns (Named Entity Recognition) | NER/Labeling
`task611_mutual_multi_turn_dialogue` | Given a conversation between two people and 4 options on how the conversation should continue, choose the most reasonable option | Multiple-Choice Question
`task612_yorubabbc_classification` | Given a news article headline from Yoruba BBC, classify the label of the headline. | Classification
`task613_politifact_text_generation` | Given a statement from a politifact.com you task is to generate the subject of discussion of the statement. | Text Generation
`task614_glucose_cause_event_detection` | Given a story and a selected sentence, find an event in the story that caused that sentence | Sentence Generation
`task615_moviesqa_answer_generation` | Given a question from an open movie database, generate an answer for that. | Answer Generation
`task616_cola_classification` | Given a sentence you have to return if it is acceptable or unacceptable. | Classification
`task617_amazonreview_category_text_generation` | Given an Amazon product review your task is to generate the category of product. | Text Generation
`task618_amazonreview_summary_text_generation` | Given an Amazon product review your task is to generate the summary of the review. | Text Generation
`task619_ohsumed_abstract_title_generation` | Generating title to Ohsumed dataset abstracts | Title Generation
`task620_ohsumed_medical_subject_headings_answer_generation` | Generating MESH terms to Ohsumed dataset abstracts | Medical subject heading(MESH) term Generation
`task621_ohsumed_yes_no_numerical_answer_generation` | Generating Yes/No answer to Ohsumed dataset questions | Answer Generation
`task622_replace_alphabets_in_a_list_by_their_position_in_english_alphabet` | Given a list replace all the alphabets in it with their position in the English Alphabet | Answer Generation
`task623_ohsumed_yes_no_answer_generation` | Generating Yes/No answers to Ohsumed dataset questions | Answer Generation
`task624_ohsumed_question_answering` | Given a abstract and question, select the best answer from the given choices. | Answer Generation
`task625_xlwic_true_or_false_answer_generation` | Determine whether both the sentences use the aforementioned word with the same meaning | Answer Generation
`task626_xlwic_sentence_based_on_given_word_sentence_generation` | Generating a sentence from a given word | Sentence Generation
`task627_xlwic_word_with_same_meaning_sentence_generation` | Generating a sentence using a given word and sentence where the word is used with the same meaning as in the given sentence | Sentence Generation
`task628_xlwic_word_with_different_meaning_sentence_generation` | Generating a sentence using a given word and sentence where the word is used with a different meaning than in the given sentence | Sentence Generation
`task629_dbpedia_14_classification` | Classifying the topic names of the text (dbpedia_14 dataset) | Classification
`task630_dbpedia_14_classification` | Verfying if the title of the text is correct(dbpedia_14 dataset) | Classification
`task631_dbpedia_14_incorrect_answer_generation` | Generating incorrect answers from specified categories | Incorrect answer generation
`task632_dbpedia_14_classification` | Verifying if the text is about a person (dbpedia_14 dataset) | Classification
`task633_dbpedia_14_answer_generation` | Generating answer to question ((dbpedia_14 dataset)) | Answer Generation
`task634_allegro_reviews_classification` | Classify the given product review to specified categories | Classification
`task635_allegro_reviews_answer_generation` | Generating "yes" or "no" to question whether the review is a positive review | Answer Generation
`task636_extract_and_sort_unique_alphabets_in_a_list` | Given a list extract all the unique alphabets from it and sort them alphabetically | Answer Generation
`task637_extract_and_sort_unique_digits_in_a_list` | Given a list extract all the unique digits used in the number in it and sort them in ascending order | Answer Generation
`task638_multi_woz_classification` | Classifying dialouge into User and System | Classification
`task639_multi_woz_user_utterance_generation`| Generate a User utterance when System's reply is given | User Utterance Generation
`task640_esnli_classification` | Given a premise and hypothesis, determine if the hypothesis entails, contradicts, or is neutral to the premise. | Classification
`task641_esnli_classification` | Classification based on if two sentences agree, disasgree, or neutral. | Classification
`task642_esnli_classification` | Classification based on if two statements agree/disagree or can't be determined. | Classification
`task643_refresd_classification` | Classification based on if an english and french sentence are different or equivalent. | Classification
`task644_refresd_translation` | Translation from english to french sentences. | Translation  
`task645_summarization` | Generating summary for Data | Summarization
`task646_answer_generation` | Find pronoun from the sentence | Answer Generation
`task647_answer_generation` | Pronoun Quote Finder | Answer Generation
`task648_answer_generation` | Find subject to the pronoun in the sentence | Answer Generation
`task649_race_blank_question_generation` | Generate a fill-in-the-blank question based on the given article and an answer. | Question Generation
`task650_opus100_ar_en_translation` | Given an Arabic sentence, translate it into English. | Translation
`task651_opus100_en_ar_translation` | Given an English sentence, translate it into Arabic. | Translation
`task652_parsinlu_en_fa_translation` | Given an English question, translate it into Persian. | Translation
`task653_parsinlu_fa_en_translation` | Given a Persian question, translate it into English. | Translation
`task654_bible_fa_en_translation` | Given a Persian sentence from the Bible, translate it into English. | Translation
`task655_bible_en_fa_translation` | Given an English sentence from the Bible, translate it into Persian. | Translation
`task656_quran_en_fa_translation` | Given an English sentence from the Quran, translate it into Persian. | Translation
`task657_quran_fa_en_translation` | Given a Persian sentence from the Quran, translate it into English. | Translation
`task658_tep_en_fa_translation` | Given an English sentence, translate it into Persian. | Translation
`task659_tep_fa_en_translation` | Given a Persian sentence, translate it into English. | Translation
`task660_mizan_fa_en_translation` | Given a Persian sentence, translate it into English. | Translation
`task661_mizan_en_fa_translation` | Given an English sentence, translate it into Persian. | Translation
`task662_global_voices_fa_en_translation` | Given a Persian sentence, translate it into English. | Translation
`task663_global_voices_en_fa_translation` | Given an English sentence, translate it into Persian. | Translation
`task664_mmmlu_answer_generation_abstract_algebra` | Answering mutlitple choice questions on abstract algebra | Answer Generation
`task665_mmmlu_answer_generation_anatomy` | Answering mutlitple choice questions on anatomy | Answer Generation
`task666_mmmlu_answer_generation_astronomy` | Answering mutlitple choice questions on astronomy | Answer Generation
`task667_mmmlu_answer_generation_business_ethics` | Answering mutlitple choice questions on business ethics | Answer Generation
`task668_extreme_abstract_summarization` | Generate a summary of this abstract. | Summarization
`task669_ambigqa_answer_generation` | Given an open-domain, provide an answer for that question. | Answer Generation
`task670_ambigqa_question_generation` | Given an ambiguous question, return a question which clarifies the given question. | Question Generation
`task671_ambigqa_text_generation` | Given an ambiguous question, provide one clarifying question and answer for the generated question. | Text Generation
`task672_nummersense` | Given a cloze question, identify the missing numerical value| Answer Generation
`task672_amazon_and_yelp_summarization_dataset_summarization` | Generating summaries to amazon/yelp reviews | Summarization
`task673_google_wellformed_query_classification` | Given a query, classify whether it's a good or bad query | Classification
`task674_google_wellformed_query_sentence_generation` | Given a set of queries, find out the query which is not well-formed | Sentence Generation
`task675_google_wellformed_query_sentence_generation` | Given a set of queries, find out the query which is well-formed | Sentence Generation
`task676_ollie_relationship_answer_generation` | Generating relationship based on given inputs in Ollie dataset | Answer Generation
`task677_ollie_sentence_answer_generation` | Generating sentences based on given inputs in Ollie dataset | Answer Generation
`task678_ollie_actual_relationship_answer_generation` | Generating the exact form of relationship based on given inputs in Ollie dataset | Answer Generation
`task679_hope_edi_english_text_classification` | Classify text in english from Hope EDI dataset | Classification
`task680_hope_edi_tamil_text_classification` | Classify text in tamil from Hope EDI dataset | Classification
`task681_hope_edi_malayalam_text_classification` | Classify text in malayalam from Hope EDI dataset | Classification
`task682_online_privacy_policy_text_classification` | Classify privacy policy texts from OPP-115 Dataset | Classification
`task683_online_privacy_policy_text_purpose_answer_generation` | Generate the purpose of privacy policy texts from OPP-115 Dataset | Answer Generation
`task684_online_privacy_policy_text_information_type_generation` | Generate the type of information used by website, mentioned in privacy policy texts from OPP-115 Dataset | Answer Generation
`task685_mmmlu_answer_generation_clinical_knowledge` | Answering mutlitple choice questions on clinical knowledge | Answer Generation
`task686_mmmlu_answer_generation_college_biology` | Answering mutlitple choice questions on college biology | Answer Generation
`task687_mmmlu_answer_generation_college_chemistry` | Answering mutlitple choice questions on college chemistry | Answer Generation
`task688_mmmlu_answer_generation_college_computer_science` | Answering mutlitple choice questions on college computer science | Answer Generation
`task689_mmmlu_answer_generation_college_mathematics` | Answering mutlitple choice questions on college mathematics | Answer Generation
`task690_mmmlu_answer_generation_college_medicine` | Answering mutlitple choice questions on college medicine | Answer Generation
`task691_mmmlu_answer_generation_college_physics` | Answering mutlitple choice questions on college physics | Answer Generation
`task692_mmmlu_answer_generation_computer_security` | Answering mutlitple choice questions on computer security | Answer Generation
`task693_mmmlu_answer_generation_conceptual_physics` | Answering mutlitple choice questions on conceptual physics | Answer Generation
`task694_mmmlu_answer_generation_econometrics` | Answering mutlitple choice questions on econometrics | Answer Generation
`task695_mmmlu_answer_generation_electrical_engineering` | Answering mutlitple choice questions on electrical engineering | Answer Generation
`task696_mmmlu_answer_generation_elementary_mathematics` | Answering mutlitple choice questions on elementary mathematics | Answer Generation
`task697_mmmlu_answer_generation_formal_logic` | Answering mutlitple choice questions on formal logic | Answer Generation
`task698_mmmlu_answer_generation_global_facts` | Answering mutlitple choice questions on global facts | Answer Generation
`task699_mmmlu_answer_generation_high_school_biology` | Answering mutlitple choice questions on high school biology | Answer Generation
`task700_mmmlu_answer_generation_high_school_chemistry` | Answering mutlitple choice questions on high school chemistry | Answer Generation
`task701_mmmlu_answer_generation_high_school_computer_science` | Answering mutlitple choice questions on high school computer science | Answer Generation
`task702_mmmlu_answer_generation_high_school_european_history` | Answering mutlitple choice questions on high school european history | Answer Generation
`task703_mmmlu_answer_generation_high_school_geography` | Answering mutlitple choice questions on high school geography | Answer Generation
`task704_mmmlu_answer_generation_high_school_government_and_politics` | Answering mutlitple choice questions on high school government and politics | Answer Generation
`task705_mmmlu_answer_generation_high_school_macroeconomics` | Answering mutlitple choice questions on high school macroeconomics | Answer Generation
`task706_mmmlu_answer_generation_high_school_mathematics` | Answering mutlitple choice questions on high school mathematics | Answer Generation
`task707_mmmlu_answer_generation_high_school_microeconomics` | Answering mutlitple choice questions on high school microeconomics | Answer Generation
`task708_mmmlu_answer_generation_high_school_physics` | Answering mutlitple choice questions on high school physics | Answer Generation
`task709_mmmlu_answer_generation_high_school_psychology` | Answering mutlitple choice questions on high school psychology | Answer Generation
`task710_mmmlu_answer_generation_high_school_statistics` | Answering mutlitple choice questions on high school statistics | Answer Generation
`task711_mmmlu_answer_generation_high_school_us_history` | Answering mutlitple choice questions on high school us history | Answer Generation
`task712_mmmlu_answer_generation_high_school_world_history` | Answering mutlitple choice questions on high school world history | Answer Generation
`task713_mmmlu_answer_generation_human_aging` | Answering mutlitple choice questions on human aging | Answer Generation
`task714_mmmlu_answer_generation_human_sexuality` | Answering mutlitple choice questions on human sexuality | Answer Generation
`task715_mmmlu_answer_generation_international_law` | Answering mutlitple choice questions on international law | Answer Generation
`task716_mmmlu_answer_generation_jurisprudence` | Answering mutlitple choice questions on jurisprudence | Answer Generation
`task717_mmmlu_answer_generation_logical_fallacies` | Answering mutlitple choice questions on logical fallacies | Answer Generation
`task718_mmmlu_answer_generation_machine_learning` | Answering mutlitple choice questions on machine learning | Answer Generation
`task719_mmmlu_answer_generation_management` | Answering mutlitple choice questions on management | Answer Generation
`task720_mmmlu_answer_generation_marketing` | Answering mutlitple choice questions on marketing | Answer Generation
`task721_mmmlu_answer_generation_medical_genetics` | Answering mutlitple choice questions on medical genetics | Answer Generation
`task722_mmmlu_answer_generation_random_topic` | Answering mutlitple choice questions on miscellaneous | Answer Generation
`task723_mmmlu_answer_generation_moral_disputes` | Answering mutlitple choice questions on moral disputes | Answer Generation
`task724_mmmlu_answer_generation_moral_scenarios` | Answering mutlitple choice questions on moral scenarios | Answer Generation
`task725_mmmlu_answer_generation_nutrition` | Answering mutlitple choice questions on nutrition | Answer Generation
`task726_mmmlu_answer_generation_philosophy` | Answering mutlitple choice questions on philosophy | Answer Generation
`task727_mmmlu_answer_generation_prehistory` | Answering mutlitple choice questions on prehistory | Answer Generation
`task728_mmmlu_answer_generation_professional_accounting` | Answering mutlitple choice questions on professional accounting | Answer Generation
`task729_mmmlu_answer_generation_professional_law` | Answering mutlitple choice questions on professional law | Answer Generation
`task730_mmmlu_answer_generation_professional_medicine` | Answering mutlitple choice questions on professional medicine | Answer Generation
`task731_mmmlu_answer_generation_professional_psychology` | Answering mutlitple choice questions on professional psychology | Answer Generation
`task732_mmmlu_answer_generation_public_relations` | Answering mutlitple choice questions on public relations | Answer Generation
`task733_mmmlu_answer_generation_security_studies` | Answering mutlitple choice questions on security studies | Answer Generation
`task734_mmmlu_answer_generation_sociology` | Answering mutlitple choice questions on sociology | Answer Generation
`task735_mmmlu_answer_generation_us_foreign_policy` | Answering mutlitple choice questions on us foreign policy | Answer Generation
`task736_mmmlu_answer_generation_virology` | Answering mutlitple choice questions on virology | Answer Generation
`task737_mmmlu_answer_generation_world_religions` | Answering mutlitple choice questions on world religions | Answer Generation
`task738_perspectrum_classification` | Decide whether the given perspective supports or undermines the given claim. | Classification
`task739_lhoestq_question_generation` | Given a passage, generate an appropriate question based on the passage. | Question Generation
`task740_lhoestq_answer_generation_quantity` | Given a passage and a question, answer the question based on the passage to output a numerical value. | Answer Generation
`task741_lhoestq_answer_generation_place` | Given a passage and a question, answer the question based on the passage to output a particular place or position of something. | Answer Generation
`task742_lhoestq_answer_generation_frequency` | Given a passage and a question, answer the question based on the passage to output the frequency with which some things occur. | Answer Generation
`task743_eurlex_summarization` | Generate headline (summary) for legal act article | Summarization  
`task744_eurlex_classification` | Identify the legal act article whether it is Regulation, Decision or Directive | Classification
`task745_ai2_arithmetic_questions_arithmetic` | Given an arithmetic question, compute a solution | Arithmetic
`task746_yelp_restaurant_review_classification` | Restaurant review classification based on its sentiment (i.e., positive or negative) | Classification
`task747_glucose_cause_emotion_detection` | Given a story and a selected sentence, find an emotion or human drive in the story that caused that sentence | Sentence Generation
`task748_glucose_reverse_cause_event_detection` | Given a story and a selected sentence, find an event that is directly caused or made possible by that sentence | Sentence Generation
`task749_glucose_reverse_cause_emotion_detection` | Given a story and a selected sentence, find an emotion or a human drive that is directly caused or made possible by that sentence | Sentence Generation
`task750_aqua_multiple_choice_answering` | Given a mathematical question , find the most suitable numerical answer | Answer Generation
`task751_svamp_subtraction_question_answering` |  Given a mathematical question involving subtraction, find the most suitable numerical answer | Answer Generation
`task752_svamp_multiplication_question_answering`|    Given a mathematical question involving multiplication, find the most suitable numerical answer | Answer Generation
`task753_svamp_addition_question_answering` |   Given a mathematical question involving addition , find the most suitable numerical answer | Answer Generation
`task754_svamp_common-division_question_answering` |   Given a mathematical question involving division, find the most suitable numerical answer | Answer Generation
`task755_find_longest_substring_and_replace_its_sorted_lowercase_version_in_both_lists` | Given two strings find the longest common substring in the strings, then convert it to all lowercase, and sort it alphabetically, and finally place it back at the same position in the two lists | Answer Generation
`task756_find_longert_substring_and_return_all_unique_alphabets_in_it` | Given two strings find the longer of the two, then lowercase it and return all unique alphabets in it | Answer Generation
`task757_msr_sqa_question_generation` | Given a table from msr_sqa dataset, generate a question based on the information presented | Question generation
`task758_msr_sqa_question_answer_generation` | Given a table from msr_sqa dataset and a question based on that table, generate a correct answer based on the table | Answer generation
`task759_msr_sqa_incorrect_answer_generation` | Given a table from msr_sqa dataset and a question based on that table, generate an incorrect correct answer based on the table | Incorrect Answer Generation
`task760_msr_sqa_long_text_generation` | Given a table from msr_sqa dataset, generate a long text passage based on the information in the tabular data | Long Text generation
`task761_app_review_classification` | Given a app review,classify whether it's Poitive or Negative | Classification
`task762_emea_fr_sk_translation` | Translate French sentences to Slovak while preserving named entities in the original language | Translation
`task763_emea_es_lt_translation` | Translate Spanish sentences to Lithuanian while preserving named entities in the original language | Translation
`task764_emea_bg_el_classification` | Identify whether translated sentence is Greek or not. | Classification
`task765_emea_bg_el_translation` | Translate Bulgarian sentences to Greek while preserving named entities in the original language | Translation
`task766_craigslist_bargains_classification` | Classifying items in Craigslist Bargains | Classification
`task767_craigslist_bargains_classification` | Classifying offer type in Craigslist Bargains | Classification
`task768_qed_text_span_selection` | Selecting one word answers from the span of a sentence from a passage to answer questions| Text Span Selection
`task769_qed_summarization` | Generating titles for passage | Summarization
`task770_pawsx_english_text_modification` | Given a sentence in English, provide an equivalent paraphrase in said language | Text Modification
`task771_pawsx_korean_text_modification` | Given a sentence in Korean, provide an equivalent paraphrase in said language | Text Modification
`task772_pawsx_french_text_modification` | Given a sentence in French, provide an equivalent paraphrase in said language | Text Modification
`task773_pawsx_spanish_text_modification` | Given a sentence in Spanish, provide an equivalent paraphrase in said language | Text Modification
`task774_pawsx_german_text_modification` | Given a sentence in German, provide an equivalent paraphrase in said language | Text Modification
`task775_pawsx_chinese_text_modification` | Given a sentence in Chinese, provide an equivalent paraphrase in said language | Text Modification
`task776_pawsx_japanese_text_modification` | Given a sentence in Japanese, provide an equivalent paraphrase in said language | Text Modification
`task777_pawsx_english_korean_translation` | Given a sentence in English, provide an equivalent translation to Korean | Translation
`task778_pawsx_english_french_translation` | Given a sentence in English, provide an equivalent translation to French | Translation
`task779_pawsx_english_spanish_translation` | Given a sentence in English, provide an equivalent translation to Spanish | Translation
`task780_pawsx_english_german_translation` | Given a sentence in English, provide an equivalent translation to German | Translation
`task781_pawsx_english_chinese_translation` | Given a sentence in English, provide an equivalent translation to Chinese | Translation
`task782_pawsx_english_japanese_translation` | Given a sentence in English, provide an equivalent translation to Japanese | Translation
`task783_pawsx_korean_english_translation` | Given a sentence in Korean, provide an equivalent translation to English | Translation
`task784_pawsx_korean_french_translation` | Given a sentence in Korean, provide an equivalent translation to French | Translation
`task785_pawsx_korean_spanish_translation` | Given a sentence in Korean, provide an equivalent translation to Spanish | Translation
`task786_pawsx_korean_german_translation` | Given a sentence in Korean, provide an equivalent translation to German | Translation
`task787_pawsx_korean_chinese_translation` | Given a sentence in Korean, provide an equivalent translation to Chinese | Translation
`task788_pawsx_korean_japanese_translation` | Given a sentence in Korean, provide an equivalent translation to Japanese | Translation
`task789_pawsx_french_english_translation` | Given a sentence in French, provide an equivalent translation to English | Translation
`task790_pawsx_french_korean_translation` | Given a sentence in French, provide an equivalent translation to Korean | Translation
`task791_pawsx_french_spanish_translation` | Given a sentence in French, provide an equivalent translation to Spanish | Translation
`task792_pawsx_french_german_translation` | Given a sentence in French, provide an equivalent translation to German | Translation
`task793_pawsx_french_chinese_translation` | Given a sentence in French, provide an equivalent translation to Chinese | Translation
`task794_pawsx_french_japanese_translation` | Given a sentence in French, provide an equivalent translation to Japanese | Translation
`task795_pawsx_spanish_english_translation` | Given a sentence in Spanish, provide an equivalent translation to English | Translation
`task796_pawsx_spanish_korean_translation` | Given a sentence in Spanish, provide an equivalent translation to Korean | Translation
`task797_pawsx_spanish_french_translation` | Given a sentence in Spanish, provide an equivalent translation to French | Translation
`task798_pawsx_spanish_german_translation` | Given a sentence in Spanish, provide an equivalent translation to German | Translation
`task799_pawsx_spanish_chinese_translation` | Given a sentence in Spanish, provide an equivalent translation to Chinese | Translation
`task800_pawsx_spanish_japanese_translation` | Given a sentence in Spanish, provide an equivalent translation to Japanese | Translation
`task801_pawsx_german_english_translation` | Given a sentence in German, provide an equivalent translation to English | Translation
`task802_pawsx_german_korean_translation` | Given a sentence in German, provide an equivalent translation to Korean | Translation
`task803_pawsx_german_french_translation` | Given a sentence in German, provide an equivalent translation to French | Translation
`task804_pawsx_german_spanish_translation` | Given a sentence in German, provide an equivalent translation to Spanish | Translation
`task805_pawsx_german_chinese_translation` | Given a sentence in German, provide an equivalent translation to Chinese | Translation
`task806_pawsx_german_japanese_translation` | Given a sentence in German, provide an equivalent translation to Japanese | Translation
`task807_pawsx_chinese_english_translation` | Given a sentence in Chinese, provide an equivalent translation to English | Translation
`task808_pawsx_chinese_korean_translation` | Given a sentence in Chinese, provide an equivalent translation to Korean | Translation
`task809_pawsx_chinese_french_translation` | Given a sentence in Chinese, provide an equivalent translation to French | Translation
`task810_pawsx_chinese_spanish_translation` | Given a sentence in Chinese, provide an equivalent translation to Spanish | Translation
`task811_pawsx_chinese_german_translation` | Given a sentence in Chinese, provide an equivalent translation to German | Translation
`task812_pawsx_chinese_japanese_translation` | Given a sentence in Chinese, provide an equivalent translation to Japanese | Translation
`task813_pawsx_japanese_english_translation` | Given a sentence in Japanese, provide an equivalent translation to English | Translation
`task814_pawsx_japanese_korean_translation` | Given a sentence in Japanese, provide an equivalent translation to Korean | Translation
`task815_pawsx_japanese_french_translation` | Given a sentence in Japanese, provide an equivalent translation to French | Translation
`task816_pawsx_japanese_spanish_translation` | Given a sentence in Japanese, provide an equivalent translation to Spanish | Translation
`task817_pawsx_japanese_german_translation` | Given a sentence in Japanese, provide an equivalent translation to German | Translation
`task818_pawsx_japanese_chinese_translation` | Given a sentence in Japanese, provide an equivalent translation to Chinese | Translation
`task819_pec_sentiment_classification` | Given a contextual post, classify the post as holding positive or negative sentiment | Classification
`task820_protoqa_answer_generation` | Given a question, generate a relevant answer to the question | Answer Generation
`task821_protoqa_question_generation` | Given a group of answers, generate a question for all answers | Question Generation  
`task823_peixian-rtgender_sentiment_analysis` | Analyze the sentiment of responses under posters from social media | Classification
`task827_copa_commonsense_reasoning` | Given a premise and two alternative,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task828_copa_commonsense_cause_effect` | Given a pair of sentences, judge whether the second sentence is the cause or effect of the first on. | Classification
`task829_giga_fren_translation` | Translation from English language to French language | Translation
`task830_poleval2019_mt_translation` | Translation from English language to Polish language | Translation
`task831_giga_fren_classification` | Classify whether the given English sentence is correctly converted to French sentence | Classification
`task832_poleval2019_mt_classification` | Classify whether the given Polish sentence is correctly converted to English sentence | Classification
`task833_poem_sentiment_classification` | Classify whether the given poem text is positive or negative | Classification
`task834_mathdataset_classification` | Classify the type of a math word problem
`task835_mathdataset_answer_generation` | Find the numerical answer for a math word problem
`task836_viquiquad_question_generation` | Given a passage in the Catalan language, generate contextual questions
`task837_viquiquad_answer_generation` | Given a passage and asked a question in the Catalan language, answer that question
`task838_cdt_classification` | Given a tweet, determine if it has bullying content. (based on cdt) | Classification
`task839_cdt_classification` | Given a tweet and prompt, determine if it has bullying content. (based on cdt) | Classification
`task840_para_pdt_en_es_translation` | Translate English questions to Spanish while preserving named entities in the original language. (based on para_pdt) | Translation
`task841_para_pdt_de_en_translation` | Translate German questions to English while preserving named entities in the original language. (based on para_pdt) | Translation
`task842_para_pdt_cs_en_translation` | Translate Czech questions to English while preserving named entities in the original language. (based on para_pdt) | Translation
`task843_financial_phrasebank_classification` | Classifying news into positive, neutral, and negative (based on financial_phrasebank) | Classification
`task844_financial_phrasebank_classification` | Classifying if (news, polarity) is valid or not (based on financial_phrasebank) | Classification
`task845_pubmedqa_question_generation` | Generating question from context and answer (based on pubmed_QA) | Question Generation
`task846_pubmedqa_classification` | Classifying if the given answer pertains to the question or not (based on pubmed_QA)| Classification
`task847_pubmedqa_question_generation` | Generating question from context (based on pubmed_QA) | Question Generation
`task848_pubmedqa_classification` | Classifying if the objective is present or not (based on pubmed_QA) | Classification
`task849_pubmedqa_answer_generation` | Generating answer from context and question (based on pubmed_QA) | Answer Generation
`task850_synthetic_longest_palindrome` | Given a string find the longest substring that is a palindrome. | Answer Generation
`task851_synthetic_multiply_evens` | Given a list of lists of integers multiply the even numbers in every list | Answer Generation, Arthimetic
`task852_synthetic_multiply_odds` | Given a list of lists of integers multiply the odd numbers in every list | Answer Generation, Arthimetic
`task853_hippocorpus_long_text_generation` | Generating long text given summaries (based on HIPPOCORPUS) | Long Text Generation
`task854_hippocorpus_classification` | Classifying whether a story is imagined, recalled, or retold (based on HIPPOCORPUS) | Classification
`task855_conv_ai_2_classification` | Classifying whether one conversation participant is a bot or human (based on conv_ai_2) | Classification
`task856_conv_ai_2_classification` | Classifying whether a conversation starter is written by a bot or a human (based on conv_ai_2) | Classification
`task857_inquisitive_question_generation` | Generating inquisitive questions | Inquisitive Question generation
`task858_inquisitive_span_detection` | Detecting span of sentence | Span Detection
`task859_prost_question_generation` | Question generation | Question generation
`task860_prost_mcq_generation` | Generating MCQs | MCQ generation
`task861_prost_mcq_answers_generation` | Generating answers of MCQs | MCQ Answer generation
`task861_asdiv_addsub_question_answering` | Given a mathematical question , find the most suitable numerical answer| Answer Generation
`task862_asdiv_multidiv_question_answering` |Given a mathematical question , find the most suitable numerical answer| Answer Generation
`task863_asdiv_multiop_question_answering` |Given a mathematical question , find the most suitable numerical answer| Answer Generation
`task864_asdiv_singleop_question_answering` |Given a mathematical question , find the most suitable numerical answer| Answer Generation
`task865_mawps_addsub_question_answering` |Given a mathematical question , find the most suitable numerical answer|Answer Generation
`task866_mawps_multidiv_question_answering` |Given a mathematical question , find the most suitable numerical answer| Answer Generation
`task867_mawps_multiop_question_answering` |Given a mathematical question , find the most suitable numerical answer| Answer Generation
`task868_mawps_singleop_question_answering` |Given a mathematical question , find the most suitable numerical answer|Answer Generation
`task868_cfq_mcd1_explanation_to_sql` | Generating queries (based on CFQ MCD1) | Structured Query Generation  
`task869_cfq_mcd1_sql_to_explanation` | Checking if queries match natural language query description | Structured Query Classification
`task870_msmarco_answer_generation` | Generating answers based on natural language passage and related query from MS MARCO | Answer Generation
`task871_msmarco_question_generation` | Generating questions based on natural language passage from MS MARCO | Question Generation
`task872_opus_xhosanavy_translation_eng_xhosa` | Translate a sentence in English to Xhosa | Translation
`task873_opus_xhosanavy_translation_xhosa_eng` | Translate a sentence in Xhosa to English | Translation
`task874_opus_xhosanavy_sr` |  Recognize primary subjects in sentences | Primary Subject Recognition
`task875_emotion_classification` | Classify sentences by emotions | Classification
`task877_kde4_translation` | Localizing English phrases to Hindi language | Translation
`task878_kde4_translation` | Localizing English phrases to Telugu language | Translation
`task879_schema_guided_dstc8_classification` | Classifying sentence as question or not | Classification
`task880_schema_guided_dstc8_classification` | Classifying sentence into one of five action categories | Classification
`task881_schema_guided_dstc8_classification` | Identifying which one of five services the sentence is related to  | Classification
`task886_quail_question_generation` | Generating questions based on passages | Question Generation
`task887_quail_answer_generation` | Generating answer for a given question based on passages | Answer Generation
`task888_reviews_classification` | Classifying whether a review is positive or negative | Classification
`task889_goemotions_classification` | Classifying the sentence to an emotion class | Classification
`task890_gcwd_classification` | Classifying writer's stance to Global Warming | Classification
`task891_gap_coreference_resolution` | Finding names for given pronouns | Coreference Resolution
`task892_gap_reverse_coreference_resolution` | Finding pronouns for given names | Reverse Coreference Resolution
`task893_gap_fill_the_blank_coreference_resolution` | Fill the blanks with corresponding pronouns | Coreference Resolution
`task896_miam_language_classification` | Classify the language for Dialogue utterances | Classification
`task897_freebase_qa_topic_question_generation` | Generate question for the given topic | Question Generation 
`task898_freebase_qa_answer_generation` | Answering questions based on an open ended topic | Answer Generation
`task899_freebase_qa_topic_generation` | Generate the specific topic for a given question | Topic Generation
`task900_freebase_qa_category_classification` | Classify the general category for questions | Classification
`task901_freebase_qa_category_question_generation` | Generate trivia type questions based on a broad category | Question Generation
`task902_deceptive_opinion_spam_classification` | Identity polarity of hotel reviews | Classification  
`task903_deceptive_opinion_spam_classification` | Given hotel reviews and it's polarity, determine whether it's true or false | Classification
`task904_hate_speech_offensive_classification` | Classify tweets into hate speech, offensive or neither | Classification  
`task905_hate_speech_offensive_classification` | Given tweet and it's category, determine whether it's true or false | Classification
`task906_dialogre_identify_names` | Text Identification with DialogRE | Answer Generation
`task907_dialogre_identify_relationships` | Classifying Relationships with DialogRE | Answer Generation
`task908_dialogre_identify_familial_relationships` | Classifying Familial Relationships with DialogRE | Answer Generation
`task909_dialogre_prevalent_speakers` | Classifying Prevalent Speakers with DialogRE | Answer Generation
`task910_bianet_classification`| Classifying whether two sentences are translations of each other | Classification
`task911_bianet_translation`| Generating a translation of an English sentence into Kurdish | Translation
`task912_bianet_classification` | Classifying a given sentence into English or Kurdish | Classification
`task913_bianet_translation` | Generating a translation of an English sentence into Turkish | Translation
`task914_bianet_translation` | Generating a translation of a Kurdish sentence into Turkish| Translation
`task917_coqa_question_generation`| Given a passage, generate a question | Question Generation
`task918_coqa_answer_generation` | Given a passage and a question, generate an answer for that question | Answer Generation
`task919_coqa_incorrect_answer_generation` | Given a passage and a question, generate an incorrect answer which is irrelevant for that question and passage | Incorrect Answer Generation
`task921_code_x_glue_information_retreival` | Given a code, calculate the number of "for loops" in the cpp program | Information Retreival
`task922_event2mind_word_generation` | Generating emotion words from Event2Mind based on PersonX | Word Generation
`task923_event2mind_classifier` | Classifying results based on sentiment values from Event2Mind | Classifier
`task924_event2mind_word_generation` | Generating emotion words from Event2Mind based on Other Person | Word Generation
`task925_coached_conv_pref_classifier` | Classifying results to find next speaker from coached_conv_pref | Classifier
`task926_coached_conv_pref_word_generation` | Generating movie names from PersonX name from coached_conv_pref | Word/Phrase Generation
`task927_yelp_negative_to_positive_style_transfer` | Given a negative review change it to a postive review | Sentence Generation
`task928_yelp_positive_to_negative_style_transfer` | Given a postive review change it to a negative review | Sentence Generation
`task929_products_reviews_classification` | Classifying generated_reviews_enth whether the review is Good Review or Bad Review | Classification
`task930_dailydialog_classification` | Classifying Data of DailyDialog whether the topic of conversation is Tourism or Not in the dialogue | Classification
`task931_dailydialog_classification` | Classifying Data of DailyDialog whether happy or sad emotion in the dialogue | Classification
`task932_dailydialog_classification` | Classifying Data of DailyDialog whether there is question in the dialogue or not | Classification
`task933_wiki_auto_style_transfer` | Rewrite wikipedia sentences in simple English. | Style Transfer 
`task934_turk_simplification` | Given a sentence your task is to generate possible numbers of simplified sentences. | Text Generation
`task935_defeasible_nli_atomic_classification` | Given a premise, hypothesis and an update, indentify whether the update strengthens or weakens the hypothesis. | Classification
`task936_defeasible_nli_snli_classification` | Given a premise, hypothesis and an update, indentify whether the update strengthens or weakens the hypothesis. | Classification
`task937_defeasible_nli_social_classification` | Given a hypothesis and an update, indentify whether the update strengthens or weakens the hypothesis. | Classification
`task938_copa_hi_commonsense_reasoning` |Given a premise and two alternative in hindi, select the alternative that more plausibly has a causal relation with the premise | Answer Generation|
`task939_copa_hi_commonsense_cause_effect` |Given a pair of sentences in hindi, judge whether the second sentence is the cause or effect of the first on. |Answer Generation |
`task940_copa_gu_commonsense_reasoning` | Given a premise and two alternative in gujarati, select the alternative that more plausibly has a causal relation with the premise|Answer Generation |
`task941_copa_gu_commonsense_cause_effect` |Given a pair of sentences in gujarati, judge whether the second sentence is the cause or effect of the first on. | Answer Generation|
`task942_copa_mr_commonsense_reasoning` | Given a premise and two alternative in marathi, select the alternative that more plausibly has a causal relation with the premise| Answer Generation|
`task943_copa_mr_commonsense_cause_effect` | Given a pair of sentences in marathi, judge whether the second sentence is the cause or effect of the first on.| Answer Generation|
`task944_wiki_cloze_as_multiple_choice_question_answering` | Given a cloze question in assamese, identify the missing word| Multiple Choice Question Answering|
`task945_wiki_cloze_bn_multiple_choice_question_answering` | Given a cloze question in bengali, identify the missing word| Multiple Choice Question Answering|
`task946_wiki_cloze_gu_multiple_choice_question_answering` |Given a cloze question in gujarati, identify the missing word | Multiple Choice Question Answering|
`task947_wiki_cloze_hi_multiple_choice_question_answering` | Given a cloze question in hindi, identify the missing word| Multiple Choice Question Answering|
`task948_wiki_cloze_kn_multiple_choice_question_answering` | Given a cloze question in kannada, identify the missing word| Multiple Choice Question Answering|
`task949_wiki_cloze_ml_multiple_choice_question_answering` | Given a cloze question in malayalam, identify the missing word| Multiple Choice Question Answering|
`task950_wiki_cloze_mr_multiple_choice_question_answering` | Given a cloze question in marathi, identify the missing word| Multiple Choice Question Answering|
`task951_wiki_cloze_or_multiple_choice_question_answering` | Given a cloze question in odia, identify the missing word| Multiple Choice Question Answering|
`task952_wiki_cloze_pa_multiple_choice_question_answering` | Given a cloze question in punjabi, identify the missing word| Multiple Choice Question Answering|
`task953_wiki_cloze_ta_multiple_choice_question_answering` | Given a cloze question in tamil, identify the missing word| Multiple Choice Question Answering|
`task954_wiki_cloze_te_multiple_choice_question_answering` | Given a cloze question in telugu, identify the missing word| Multiple Choice Question Answering|
`task955_wiki_auto_style_transfer` | Elaborate wikipedia sentences. | Style Transfer 
`task956_leetcode_420_strong_password_check` | Check if the given password is strong | Answer Generation 
`task957_e2e_nlg_text_generation_generate` | Generate a restaurant description from a data table. | Tabular Text Operation
`task958_e2e_nlg_text_generation_parse` | Parse a restaurant description into a data table. | Tabular Text Operation
`task959_e2e_nlg_text_generation_identify` | Identify the named entity that is the subject of the excerpt. | Named Entity Recognition
`task960_ancora-ca-ner_named_entity_recognition` | Named Entity Recognition for each token in BSC-TeMU/ancora-ca-ner catalan sentences | Named Entity Recognition
`task961_ancora-ca-ner_text_auto_completion` | Text Auto Completion of partial Catalan sentences | Sentence Generation
`task962_ancora-ca-ner_missing_word_prediction` | Generating a missing word on Catalan Sentences | Sentence Generation
`task963_librispeech_asr_next_word_prediction` | Predicting next word on librispeech data | Word Generation
`task964_librispeech_asr_text_auto_completion` | Text Auto Completion of partial English sentences | Sentence Generation
`task965_librispeech_asr_missing_word_prediction` | Generating a missing word on English Sentences | Sentence Generation
`task966_ruletaker_fact_checking_based_on_given_context` | Fact checking based on given context | Fact checking based on context
`task967_ruletaker_incorrect_fact_generation_based_on_given_paragraph` | Generate incorrect fact based on given paragraph | Incorrect Fact Generation
`task968_xcopa_commonsense_reasoning_et` | Given a premise and two alternative in Estonian,  select the alternative that more plausibly has a causal relation with the premise | Causal Reasoning
`task969_xcopa_commonsense_cause_effect_et` | Given a pair of sentences in Estonian, judge whether the second sentence is the cause or effect of the first on. | Causal Reasoning
`task970_sherliic_causal_relationship` | Determine if A and B share a casual relationship |Classification
`task974_prachathai67k_sentiment_classification` | Classify the sentiment of a given article on the given genre |Classification
`task975_prachathai67k_same_genre_classification` | Determine if the two articles given share the same sentiment fot the given genre |Classification
`task976_pib_indian_language_identification` | Identify the language of the given statement from the 11 languages listed |Classification
`task977_pib_translation_oriya_urdu`| Translate from oriya to urdu | Translation
`task978_pib_translation_urdu_oriya`| Translate from urdu to oriya | Translation
`task979_pib_translation_malayalam_oriya`| Translate from malayalam to oriya | Translation
`task980_pib_translation_oriya_malayalam`| Translate from oriya to malayalam | Translation
`task981_pib_translation_bengali_tamil`| Translate from bengali to tamil | Translation
`task982_pib_translation_tamil_bengali`| Translate from tamil to bengali | Translation
`task983_pib_translation_gujarati_marathi`| Translate from gujarati to marathi | Translation
`task984_pib_translation_marathi_gujarati`| Translate from marathi to gujarati | Translation
`task985_pib_translation_hindi_oriya`| Translate from hindi to oriya | Translation
`task986_pib_translation_oriya_hindi`| Translate from oriya to hindi | Translation
`task987_pib_translation_english_oriya`| Translate from english to oriya | Translation
`task988_pib_translation_oriya_english`| Translate from oriya to english | Translation
`task989_pib_translation_marathi_urdu`| Translate from marathi to urdu | Translation
`task990_pib_translation_urdu_marathi`| Translate from urdu to marathi | Translation
`task991_pib_translation_english_tamil`| Translate from english to tamil | Translation
`task992_pib_translation_tamil_english`| Translate from tamil to english | Translation
`task993_pib_translation_hindi_tamil`| Translate from hindi to tamil | Translation
`task994_pib_translation_tamil_hindi`| Translate from tamil to hindi | Translation
`task995_pib_translation_bengali_english`| Translate from bengali to english | Translation
`task996_pib_translation_english_bengali`| Translate from english to bengali | Translation
`task997_pib_translation_bengali_oriya`| Translate from bengali to oriya | Translation
`task998_pib_translation_oriya_bengali`| Translate from oriya to bengali | Translation
`task999_pib_translation_malayalam_tamil`| Translate from malayalam to tamil | Translation
`task1000_pib_translation_tamil_malayalam`| Translate from tamil to malayalam | Translation
`task1001_pib_translation_gujarati_urdu`| Translate from gujarati to urdu | Translation
`task1002_pib_translation_urdu_gujarati`| Translate from urdu to gujarati | Translation
`task1003_pib_translation_bengali_malayalam`| Translate from bengali to malayalam | Translation
`task1004_pib_translation_malayalam_bengali`| Translate from malayalam to bengali | Translation
`task1005_pib_translation_malayalam_punjabi`| Translate from malayalam to punjabi | Translation
`task1006_pib_translation_punjabi_malayalam`| Translate from punjabi to malayalam | Translation
`task1007_pib_translation_english_punjabi`| Translate from english to punjabi | Translation
`task1008_pib_translation_punjabi_english`| Translate from punjabi to english | Translation
`task1009_pib_translation_bengali_hindi`| Translate from bengali to hindi | Translation
`task1010_pib_translation_hindi_bengali`| Translate from hindi to bengali | Translation
`task1011_pib_translation_hindi_punjabi`| Translate from hindi to punjabi | Translation
`task1012_pib_translation_punjabi_hindi`| Translate from punjabi to hindi | Translation
`task1013_pib_translation_gujarati_telugu`| Translate from gujarati to telugu | Translation
`task1014_pib_translation_telugu_gujarati`| Translate from telugu to gujarati | Translation
`task1015_pib_translation_punjabi_tamil`| Translate from punjabi to tamil | Translation
`task1016_pib_translation_tamil_punjabi`| Translate from tamil to punjabi | Translation
`task1017_pib_translation_hindi_malayalam`| Translate from hindi to malayalam | Translation
`task1018_pib_translation_malayalam_hindi`| Translate from malayalam to hindi | Translation
`task1019_pib_translation_oriya_telugu`| Translate from oriya to telugu | Translation
`task1020_pib_translation_telugu_oriya`| Translate from telugu to oriya | Translation
`task1021_pib_translation_english_malayalam`| Translate from english to malayalam | Translation
`task1022_pib_translation_malayalam_english`| Translate from malayalam to english | Translation
`task1023_pib_translation_english_hindi`| Translate from english to hindi | Translation
`task1024_pib_translation_hindi_english`| Translate from hindi to english | Translation
`task1025_pib_translation_bengali_punjabi`| Translate from bengali to punjabi | Translation
`task1026_pib_translation_punjabi_bengali`| Translate from punjabi to bengali | Translation
`task1027_pib_translation_marathi_telugu`| Translate from marathi to telugu | Translation
`task1028_pib_translation_telugu_marathi`| Translate from telugu to marathi | Translation
`task1029_pib_translation_marathi_punjabi`| Translate from marathi to punjabi | Translation
`task1030_pib_translation_punjabi_marathi`| Translate from punjabi to marathi | Translation
`task1031_pib_translation_bengali_telugu`| Translate from bengali to telugu | Translation
`task1032_pib_translation_telugu_bengali`| Translate from telugu to bengali | Translation
`task1033_pib_translation_gujarati_hindi`| Translate from gujarati to hindi | Translation
`task1034_pib_translation_hindi_gujarati`| Translate from hindi to gujarati | Translation
`task1035_pib_translation_tamil_urdu`| Translate from tamil to urdu | Translation
`task1036_pib_translation_urdu_tamil`| Translate from urdu to tamil | Translation
`task1037_pib_translation_telugu_urdu`| Translate from telugu to urdu | Translation
`task1038_pib_translation_urdu_telugu`| Translate from urdu to telugu | Translation
`task1039_pib_translation_oriya_punjabi`| Translate from oriya to punjabi | Translation
`task1040_pib_translation_punjabi_oriya`| Translate from punjabi to oriya | Translation
`task1041_pib_translation_gujarati_malayalam`| Translate from gujarati to malayalam | Translation
`task1042_pib_translation_malayalam_gujarati`| Translate from malayalam to gujarati | Translation
`task1043_pib_translation_gujarati_punjabi`| Translate from gujarati to punjabi | Translation
`task1044_pib_translation_punjabi_gujarati`| Translate from punjabi to gujarati | Translation
`task1045_pib_translation_hindi_telugu`| Translate from hindi to telugu | Translation
`task1046_pib_translation_telugu_hindi`| Translate from telugu to hindi | Translation
`task1047_pib_translation_english_telugu`| Translate from english to telugu | Translation
`task1048_pib_translation_telugu_english`| Translate from telugu to english | Translation
`task1049_pib_translation_malayalam_telugu`| Translate from malayalam to telugu | Translation
`task1050_pib_translation_telugu_malayalam`| Translate from telugu to malayalam | Translation
`task1051_pib_translation_punjabi_urdu`| Translate from punjabi to urdu | Translation
`task1052_pib_translation_urdu_punjabi`| Translate from urdu to punjabi | Translation
`task1053_pib_translation_hindi_urdu`| Translate from hindi to urdu | Translation
`task1054_pib_translation_urdu_hindi`| Translate from urdu to hindi | Translation
`task1055_pib_translation_marathi_oriya`| Translate from marathi to oriya | Translation
`task1056_pib_translation_oriya_marathi`| Translate from oriya to marathi | Translation
`task1057_pib_translation_english_urdu`| Translate from english to urdu | Translation
`task1058_pib_translation_urdu_english`| Translate from urdu to english | Translation
`task1059_pib_translation_malayalam_urdu`| Translate from malayalam to urdu | Translation
`task1060_pib_translation_urdu_malayalam`| Translate from urdu to malayalam | Translation
`task1061_pib_translation_bengali_marathi`| Translate from bengali to marathi | Translation
`task1062_pib_translation_marathi_bengali`| Translate from marathi to bengali | Translation
`task1063_pib_translation_gujarati_tamil`| Translate from gujarati to tamil | Translation
`task1064_pib_translation_tamil_gujarati`| Translate from tamil to gujarati | Translation
`task1065_pib_translation_punjabi_telugu`| Translate from punjabi to telugu | Translation
`task1066_pib_translation_telugu_punjabi`| Translate from telugu to punjabi | Translation
`task1067_pib_translation_bengali_gujarati`| Translate from bengali to gujarati | Translation
`task1068_pib_translation_gujarati_bengali`| Translate from gujarati to bengali | Translation
`task1069_pib_translation_bengali_urdu`| Translate from bengali to urdu | Translation
`task1070_pib_translation_urdu_bengali`| Translate from urdu to bengali | Translation
`task1071_pib_translation_malayalam_marathi`| Translate from malayalam to marathi | Translation
`task1072_pib_translation_marathi_malayalam`| Translate from marathi to malayalam | Translation
`task1073_pib_translation_oriya_tamil`| Translate from oriya to tamil | Translation
`task1074_pib_translation_tamil_oriya`| Translate from tamil to oriya | Translation
`task1075_pib_translation_tamil_telugu`| Translate from tamil to telugu | Translation
`task1076_pib_translation_telugu_tamil`| Translate from telugu to tamil | Translation
`task1077_pib_translation_gujarati_oriya`| Translate from gujarati to oriya | Translation
`task1078_pib_translation_oriya_gujarati`| Translate from oriya to gujarati | Translation
`task1079_pib_translation_english_gujarati`| Translate from english to gujarati | Translation
`task1080_pib_translation_gujarati_english`| Translate from gujarati to english | Translation
`task1081_pib_translation_hindi_marathi`| Translate from hindi to marathi | Translation
`task1082_pib_translation_marathi_hindi`| Translate from marathi to hindi | Translation
`task1083_pib_translation_marathi_tamil`| Translate from marathi to tamil | Translation
`task1084_pib_translation_tamil_marathi`| Translate from tamil to marathi | Translation
`task1085_pib_translation_english_marathi`| Translate from english to marathi | Translation
`task1086_pib_translation_marathi_english`| Translate from marathi to english | Translation
`task1087_two_number_sum` | Given a list of integers and a target sum, return a pair of integers that sum to the target | Answer Generation
`task1088_array_of_products` | Given an integer array in the input, return an array such that its element at each location is equal to the product of elements at every other location in the input array" | Answer Generation
`task1089_check_monotonic_array` | Check if the given array is monotonic or not  | Answer Generation
`task1090_ted_translation_en_gl` | Translate a sentence in English to Galician. | Translation
`task1091_ted_translation_en_it` | Translate a sentence in English to Italian. | Translation
`task1092_ted_translation_en_pl` | Translate a sentence in English to Polish. | Translation
`task1093_ted_translation_en_fa` | Translate a sentence in English to Farsi. | Translation
`task1094_ted_translation_en_pt` | Translate a sentence in English to Portugese. | Translation
`task1095_ted_translation_ja_gl` | Translate a sentence in Japanese to Galician. | Translation
`task1096_ted_translation_ja_it` | Translate a sentence in Japanese to Italian. | Translation
`task1097_ted_translation_ja_pl` | Translate a sentence in Japanese to Polish. | Translation
`task1098_ted_translation_ja_fa` | Translate a sentence in Japanese to Farsi. | Translation
`task1099_ted_translation_ja_pt` | Translate a sentence in Japanese to Portugese. | Translation
`task1100_ted_translation_es_gl` | Translate a sentence in Spanish to Galician. | Translation
`task1101_ted_translation_es_it` | Translate a sentence in Spanish to Italian. | Translation
`task1102_ted_translation_es_pl` | Translate a sentence in Spanish to Polish. | Translation
`task1103_ted_translation_es_fa` | Translate a sentence in Spanish to Farsi. | Translation
`task1104_ted_translation_es_pt` | Translate a sentence in Spanish to Portugese. | Translation
`task1105_ted_translation_ar_gl` | Translate a sentence in Arabic to Galician. | Translation
`task1106_ted_translation_ar_it` | Translate a sentence in Arabic to Italian. | Translation
`task1107_ted_translation_ar_pl` | Translate a sentence in Arabic to Polish. | Translation
`task1108_ted_translation_ar_fa` | Translate a sentence in Arabic to Farsi. | Translation
`task1109_ted_translation_ar_pt` | Translate a sentence in Arabic to Portugese. | Translation
`task1110_ted_translation_he_gl` | Translate a sentence in Hebrew to Galician. | Translation
`task1111_ted_translation_he_it` | Translate a sentence in Hebrew to Italian. | Translation
`task1112_ted_translation_he_pl` | Translate a sentence in Hebrew to Polish. | Translation
`task1113_ted_translation_he_fa` | Translate a sentence in Hebrew to Farsi. | Translation
`task1114_ted_translation_he_pt` | Translate a sentence in Hebrew to Portugese. | Translation
`task1115_alt_ja_id_translation` | Given a Japanese language sentence translate it into Bahasa Indonesia language. | Translation
`task1116_alt_id_ja_translation` | Given a Bahasa Indonesia language sentence translate it into Japanese language. | Translation
`task1117_alt_ja_id_answer_generation` | Generate answer yes or no for Japanese and Bahasa Indonesia translation pair. | Answer Generation
`task1118_alt_ja_fil_translation` | Given a Japanese language sentence translate it into Filipino language. | Translation
`task1119_alt_fil_ja_translation` | Given a Filipino language sentence translate it into Japanese language. | Translation
`task1120_alt_ja_fil_answer_generation` | Generate answer yes or no for Japanese and Filipino translation pair. | Answer Generation
`task1121_alt_ja_khm_translation` | Given a Japanese language sentence translate it into Khmer language. | Translation
`task1122_alt_khm_ja_translation` | Given a Khmer language sentence translate it into Japanese language. | Translation
`task1123_alt_ja_khm_answer_generation` | Generate answer yes or no for Japanese and Khmer translation pair. | Answer Generation
`task1124_alt_ja_lo_translation` | Given a Japanese language sentence translate it into Lao language. | Translation
`task1125_alt_lo_ja_translation` | Given a Lao language sentence translate it into Japanese language. | Translation
`task1126_alt_ja_lo_answer_generation` | Generate answer yes or no for Japanese and Lao translation pair. | Answer Generation
`task1127_alt_ja_th_translation` | Given a Japanese language sentence translate it into Thai language. | Translation
`task1128_alt_th_ja_translation` | Given a Thai language sentence translate it into Japanese language. | Translation
`task1129_alt_ja_th_answer_generation` | Generate answer yes or no for Japanese and Thai translation pair. | Answer Generation
`task1130_xcsr_vi_commonsense_mc_classification` | Answering multiple choice commonsense question in Vietnamese language. | Classification
`task1131_xcsr_es_commonsense_mc_classification` | Answering multiple choice commonsense question in Spanish language. | Classification
`task1132_xcsr_ur_commonsense_mc_classification` | Answering multiple choice commonsense question in Urdu language. | Classification
`task1133_xcsr_nl_commonsense_mc_classification` | Answering multiple choice commonsense question in Dutch language. | Classification
`task1134_xcsr_hi_commonsense_mc_classification` | Answering multiple choice commonsense question in Hindi language. | Classification
`task1135_xcsr_en_commonsense_mc_classification` | Answering multiple choice commonsense question in English language. | Classification
`task1136_xcsr_fr_commonsense_mc_classification` | Answering multiple choice commonsense question in French language. | Classification
`task1137_xcsr_pt_commonsense_mc_classification` | Answering multiple choice commonsense question in Portuguese language. | Classification
`task1138_xcsr_de_commonsense_mc_classification` | Answering multiple choice commonsense question in German language. | Classification
`task1139_xcsr_ru_commonsense_mc_classification` | Answering multiple choice commonsense question in Russian language. | Classification
`task1140_xcsr_pl_commonsense_mc_classification` | Answering multiple choice commonsense question in Polish language. | Classification
`task1141_xcsr_zh_commonsense_mc_classification` | Answering multiple choice commonsense question in Chinese language. | Classification
`task1142_xcsr_ar_commonsense_mc_classification` | Answering multiple choice commonsense question in Arabic language. | Classification
`task1143_xcsr_it_commonsense_mc_classification` | Answering multiple choice commonsense question in Italian language. | Classification
`task1144_xcsr_sw_commonsense_mc_classification` | Answering multiple choice commonsense question in Swahili language. | Classification
`task1145_xcsr_jap_commonsense_mc_classification` | Answering multiple choice commonsense question in Japanese language. | Classification
`task1146_country_capital` | Given a country, return it's capital city  | Answer Generation
`task1147_country_currency` | Given a country, return it's currency  | Answer Generation
`task1148_maximum_ascii_value` | Given a string, return the character with maximum ascii value  | Answer Generation
`task1149_item_check_edible` | Given an item, check if it is edible or not  | Classification
`task1150_delete_max_min` | Given a list of integers, delete the minimum and maximum element from the list  | Answer Generation
`task1151_swap_max_min` | Given a list of unique integers, swap the minimum and maximum element in the list  | Answer Generation
`task1152_bard_analogical_reasoning_causation` | Given an analogy that relates actions with their consequences, give the appropriate consequence of the given action | Answer Generation
`task1153_bard_analogical_reasoning_affordance` | Given an analogy that signifies affordances give the appropriate affordance of the given action | Answer Generation
`task1154_bard_analogical_reasoning_travel` | Given an analogy that relates places/locations to the associated travel mode, give the appropriate travel mode for the given place | Answer Generation
`task1155_bard_analogical_reasoning_trash_or_treasure` | Given an analogy that relates items to whether they are trash or treasure, is the given item `trash` or `treasure`? | Answer Generation
`task1156_bard_analogical_reasoning_tools` | Given an analogy that relates actions to the tools used to perform the action, give the appropriate tool for the given action | Answer Generation
`task1157_bard_analogical_reasoning_rooms_for_containers` | Given an analogy that relates objects to the associated rooms, give the appropriate room for the given object | Answer Generation
`task1158_bard_analogical_reasoning_manipulating_items` | Given an analogy that on manipulating items in a kitchen, give with the appropriate word | Answer Generation
`task1159_bard_analogical_reasoning_containers` | Given an analogy that relates items to the associated containers, give the appropriate container for the given item | Answer Generation
`task1161_coda19_title_generation` | Given a paragraph from a research paper, your task is to generate the title of the paper | Title Generation
`task1162_coda19_title_classification` | Given a paragraph from the research paper and the title, your task is to classify whether title belong to paper. | Classification
`task1163_coda19_section_classification` | Given a sentence from a research paper, your task is to classify among the section the sentence belongs. | Classification
`task1164_coda19_section_correction_classification` | Given a sentence from a research paper and the section, your task is to classify whether the sentence belongs to that sentence. | Classification
`task1167_penn_treebank_coarse_pos_tagging` | Given a sentence, a word in that sentence and the position of that word in the sentence, find the parts-of-speech tag of the word | Classification
`task1168_brown_coarse_pos_tagging` | Given a sentence, a word in that sentence and the position of that word in the sentence, find the parts-of-speech tag of the word | Classification
`task1168_xcopa_commonsense_reasoning_ht` | Given a premise and two alternative in Haitian,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1169_xcopa_commonsense_cause_effect_ht` | Given a pair of sentences in Haitian, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1170_xcopa_commonsense_reasoning_id` | Given a premise and two alternative in Indonesian,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1171_xcopa_commonsense_cause_effect_id` | Given a pair of sentences in Indonesian, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1172_xcopa_commonsense_reasoning_it` | Given a premise and two alternative in Italian,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1173_xcopa_commonsense_cause_effect_it` | Given a pair of sentences in Italian, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1174_xcopa_commonsense_reasoning_sw` | Given a premise and two alternative in Swahili,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1175_xcopa_commonsense_cause_effect_sw` | Given a pair of sentences in Swahili, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1176_xcopa_commonsense_reasoning_ta` | Given a premise and two alternative in Tamil,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1177_xcopa_commonsense_cause_effect_ta` | Given a pair of sentences in Tamil, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1178_xcopa_commonsense_reasoning_th` | Given a premise and two alternative in Thai,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1179_xcopa_commonsense_cause_effect_th` | Given a pair of sentences in Thai, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1180_xcopa_commonsense_reasoning_tr` | Given a premise and two alternative in Turkish,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1181_xcopa_commonsense_cause_effect_tr` | Given a pair of sentences in Turkish, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1182_xcopa_commonsense_reasoning_vi` | Given a premise and two alternative in Vietnamese,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1183_xcopa_commonsense_cause_effect_vi` | Given a pair of sentences in Vietnamese, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1184_xcopa_commonsense_reasoning_zh` | Given a premise and two alternative in Chinese,  select the alternative that more plausibly has a causal relation with the premise | Answer Generation 
`task1185_xcopa_commonsense_cause_effect_zh` | Given a pair of sentences in Chinese, judge whether the second sentence is the cause or effect of the first on. | Classification
`task1186_nne_hrngo_classification` | Evaluate naturalness of system generated reference. | Classification 
`task1187_politifact_classification` | Given a statement and subject of discussion, your task is to classify whether it's a correct subject or not. | Classification
`task1188_count_max_freq_char` | Given a string with duplicate characters, find the character which is ocurring with the maximum frequency  | Answer Generation
`task1189_check_char_in_string` | Given a string S and a character c, check if c is present in S or not  | Answer Generation
`task1190_add_integer_to_list` | Given a list of integers and an integer k, add k to every element in the list  | Answer Generation
`task1191_food_veg_nonveg` | Given the name of an indian dish, classify it as non vegetarian or a vegetarian dish  | Classification
`task1192_food_flavor_profile` | Given the name of an indian dish, classify it's flavor as spicy or sweet  | Classification
`task1193_food_course_classification` | Given the name of an indian dish, classify it's course as main course, dessert or snack  | Classification
`task1194_kth_largest_element` | Given a list of integers and an integer k, find the kth largest element in the list  | Classification
`task1195_disflqa_disfluent_to_fluent_conversion` | Given a disfluent sentence, modify it to make it a fluent sentence | Text Modification
`task1196_atomic_classification_oeffect` | Given a tuple, determine whether, as a result of the Head, personY or others will be affected as mentioned in the Tail or not. | Classification | Sociology	| English	| English
`task1197_atomic_classification_oreact` | Given a tuple, determine whether, as a result of the Head, personY or others feel what is mentioned in the Tail or not. | Classification | Sociology	| English	| English
`task1198_atomic_classification_owant` | Given a tuple, determine whether, as a result of the Head, personY or others will want what is mentioned in the Tail or not. | Classification | Sociology	| English	| English | Sociology	| English	| English
`task1199_atomic_classification_xattr` | Given a tuple, determine whether, as a result of the Head, personX will be seen as what is mentioned in the Tail or not. | Classification | Sociology	| English	| English | Sociology	| English	| English | Sociology	| English	| English
`task1200_atomic_classification_xeffect` | Given a tuple, determine whether, as a result of the Head, personX will be affected as mentioned in the Tail or not. | Classification | Sociology	| English	| English
`task1201_atomic_classification_xintent` | Given a tuple, determine whether The tail is the intention of the PersonX from the Head or not. | Classification | Sociology	| English	| English
`task1202_atomic_classification_xneed` | Given a tuple, determine whether PersonX needs what is mentioned in the Tail before the Head or not. | Classification | Sociology	| English	| English
`task1203_atomic_classification_xreact` | Given a tuple, determine whether, as a result of the Head, personX feels what is mentioned in the Tail or not. | Classification | Sociology	| English	| English
`task1204_atomic_classification_hinderedby` | Given a tuple, determine whether the Head can be hindered by what is mentioned in the Tail or not. | Classification | Sociology	| English	| English
`task1205_atomic_classification_isafter` | Given a tuple, determine whether the Head happens after the Tail or not. | Classification | Sociology	| English	| English
`task1206_atomic_classification_isbefore` | Given a tuple, determine whether the Head happens before the Tail or not. | Classification | Sociology	| English	| English | Sociology	| English	| English
`task1207_atomic_classification_atlocation` | Given a tuple, determine whether the Head is located or can be found at/in/on the Tail or not. | Classification | Sociology	| English	| English | Sociology	| English	| English | Sociology	| English	| English
`task1208_atomic_classification_xreason` | Given a tuple, determine whether The Tail is the reason for the Head or not. | Classification | Sociology	| English	| English
`task1209_atomic_classification_objectuse` | Given a tuple, determine whether the Head is used for the Tail or not. | Classification | Sociology	| English	| English
`task1210_atomic_classification_madeupof` | Given a tuple, determine whether the Head is made of the Tail or not. | Classification | Sociology	| English	| English | Sociology	| English	| English
`task1211_atomic_classification_hassubevent` | Given a tuple, determine whether the Head includes an event or an action in the Tail or not. | Classification | Sociology	| English	| English
`task1212_atomic_classification_hasproperty` | Given a tuple, determine whether the Head can be characterized by being or having the Tail or not. | Classification | Sociology	| English	| English
`task1213_atomic_classification_desires` | Given a tuple, determine whether the Head desires the Tail or not. | Classification | Sociology	| English	| English
`task1214_atomic_classification_xwant` | Given a tuple, determine whether, as a result of the Head, personX wants what is mentioned in the Tail or not. | Classification | Sociology	| English	| English
`task1215_atomic_classification_capableof` | Given a tuple, ddetermine whether the Head is capable of the Tail or not. | Classification | Sociology	| English	| English
`task1216_atomic_classification_causes` | Given a tuple, determine whether the Head causes the Tail or not. | Classification | Sociology	| English	| English
`task1217_atomic_answer_generation` | Given a sentence, fill in the blank with a plausible word. | Fill in the Blank | Sociology	| English	| English
`task1218_ted_translation_en_ja` | Translate a sentence in English to Japanese. | Translation
`task1219_ted_translation_en_es` | Translate a sentence in English to Spanish. | Translation
`task1220_ted_translation_en_ar` | Translate a sentence in English to Arabic. | Translation
`task1221_ted_translation_en_he` | Translate a sentence in English to Hebrew. | Translation
`task1222_ted_translation_ja_en` | Translate a sentence in Japanese to English. | Translation
`task1223_ted_translation_ja_es` | Translate a sentence in Japanese to Spanish. | Translation
`task1224_ted_translation_ja_ar` | Translate a sentence in Japanese to Arabic. | Translation
`task1225_ted_translation_ja_he` | Translate a sentence in Japanese to Hebrew. | Translation
`task1226_ted_translation_es_en` | Translate a sentence in Spanish to English. | Translation
`task1227_ted_translation_es_ja` | Translate a sentence in Spanish to Japanese. | Translation
`task1228_ted_translation_es_ar` | Translate a sentence in Spanish to Arabic. | Translation
`task1229_ted_translation_es_he` | Translate a sentence in Spanish to Hebrew. | Translation
`task1230_ted_translation_ar_en` | Translate a sentence in Arabic to English. | Translation
`task1231_ted_translation_ar_ja` | Translate a sentence in Arabic to Japanese. | Translation
`task1232_ted_translation_ar_es` | Translate a sentence in Arabic to Spanish. | Translation
`task1233_ted_translation_ar_he` | Translate a sentence in Arabic to Hebrew. | Translation
`task1234_ted_translation_he_en` | Translate a sentence in Hebrew to English. | Translation
`task1235_ted_translation_he_ja` | Translate a sentence in Hebrew to Japanese. | Translation
`task1236_ted_translation_he_es` | Translate a sentence in Hebrew to Spanish. | Translation
`task1237_ted_translation_he_ar` | Translate a sentence in Hebrew to Arabic. | Translation
`task1238_ted_translation_gl_en` | Translate a sentence in Galician to English. | Translation
`task1239_ted_translation_gl_ja` | Translate a sentence in Galician to Japanese. | Translation
`task1240_ted_translation_gl_es` | Translate a sentence in Galician to Spanish. | Translation
`task1241_ted_translation_gl_ar` | Translate a sentence in Galician to Arabic. | Translation
`task1242_ted_translation_gl_he` | Translate a sentence in Galician to Hebrew. | Translation
`task1243_ted_translation_gl_it` | Translate a sentence in Galician to Italian. | Translation
`task1244_ted_translation_gl_pl` | Translate a sentence in Galician to Polish. | Translation
`task1245_ted_translation_gl_fa` | Translate a sentence in Galician to Farsi. | Translation
`task1246_ted_translation_gl_pt` | Translate a sentence in Galician to Portugese. | Translation
`task1247_ted_translation_it_en` | Translate a sentence in Italian to English. | Translation
`task1248_ted_translation_it_ja` | Translate a sentence in Italian to Japanese. | Translation
`task1249_ted_translation_it_es` | Translate a sentence in Italian to Spanish. | Translation
`task1250_ted_translation_it_ar` | Translate a sentence in Italian to Arabic. | Translation
`task1251_ted_translation_it_he` | Translate a sentence in Italian to Hebrew. | Translation
`task1252_ted_translation_it_gl` | Translate a sentence in Italian to Galician. | Translation
`task1253_ted_translation_it_pl` | Translate a sentence in Italian to Polish. | Translation
`task1254_ted_translation_it_fa` | Translate a sentence in Italian to Farsi. | Translation
`task1255_ted_translation_it_pt` | Translate a sentence in Italian to Portugese. | Translation
`task1256_ted_translation_pl_en` | Translate a sentence in Polish to English. | Translation
`task1257_ted_translation_pl_ja` | Translate a sentence in Polish to Japanese. | Translation
`task1258_ted_translation_pl_es` | Translate a sentence in Polish to Spanish. | Translation
`task1259_ted_translation_pl_ar` | Translate a sentence in Polish to Arabic. | Translation
`task1260_ted_translation_pl_he` | Translate a sentence in Polish to Hebrew. | Translation
`task1261_ted_translation_pl_gl` | Translate a sentence in Polish to Galician. | Translation
`task1262_ted_translation_pl_it` | Translate a sentence in Polish to Italian. | Translation
`task1263_ted_translation_pl_fa` | Translate a sentence in Polish to Farsi. | Translation
`task1264_ted_translation_pl_pt` | Translate a sentence in Polish to Portugese. | Translation
`task1265_ted_translation_fa_en` | Translate a sentence in Farsi to English. | Translation
`task1266_ted_translation_fa_ja` | Translate a sentence in Farsi to Japanese. | Translation
`task1267_ted_translation_fa_es` | Translate a sentence in Farsi to Spanish. | Translation
`task1268_ted_translation_fa_ar` | Translate a sentence in Farsi to Arabic. | Translation
`task1269_ted_translation_fa_he` | Translate a sentence in Farsi to Hebrew. | Translation
`task1270_ted_translation_fa_gl` | Translate a sentence in Farsi to Galician. | Translation
`task1271_ted_translation_fa_it` | Translate a sentence in Farsi to Italian. | Translation
`task1272_ted_translation_fa_pl` | Translate a sentence in Farsi to Polish. | Translation
`task1273_ted_translation_fa_pt` | Translate a sentence in Farsi to Portugese. | Translation
`task1274_ted_translation_pt_en` | Translate a sentence in Portugese to English. | Translation
`task1275_ted_translation_pt_ja` | Translate a sentence in Portugese to Japanese. | Translation
`task1276_ted_translation_pt_es` | Translate a sentence in Portugese to Spanish. | Translation
`task1277_ted_translation_pt_ar` | Translate a sentence in Portugese to Arabic. | Translation
`task1278_ted_translation_pt_he` | Translate a sentence in Portugese to Hebrew. | Translation
`task1279_ted_translation_pt_gl` | Translate a sentence in Portugese to Galician. | Translation
`task1280_ted_translation_pt_it` | Translate a sentence in Portugese to Italian. | Translation
`task1281_ted_translation_pt_pl` | Translate a sentence in Portugese to Polish. | Translation
`task1282_ted_translation_pt_fa` | Translate a sentence in Portugese to Farsi. | Translation
`task1283_hrngo_quality_classification` | Evaluate quality of system generated reference. | Classification
`task1284_hrngo_informativeness_classification` | Evaluate informativeness of system generated reference. | Classification
`task1285_kpa_keypoint_matching_assisted_suicide_topic` | Given an argument and a keypoint under the topic "Assisted suicide should be a criminal offence", answer if the keypoint summarizes the argument | Classification
`task1286_kpa_keypoint_matching_homeschooling_topic` | Given an argument and a keypoint under the topic "Homeschooling should be banned", answer if the keypoint summarizes the argument | Classification
`task1287_kpa_keypoint_matching_marriage_topic` | Given an argument and a keypoint under the topic "We should abandon marriage", answer if the keypoint summarizes the argument | Classification
`task1288_kpa_keypoint_matching_capital_punishment_topic` | Given an argument and a keypoint under the topic "We should abolish capital punishment", answer if the keypoint summarizes the argument | Classification
`task1289_kpa_keypoint_matching_intellectual_property_rights` | Given an argument and a keypoint under the topic "We should abolish intellectual property rights", answer if the keypoint summarizes the argument | Classification
`task1290_kpa_keypoint_matching_atheism_topic` | Given an argument and a keypoint under the topic "We should adopt atheism", answer if the keypoint summarizes the argument | Classification
`task1291_kpa_keypoint_matching_libertarianism_topic` | Given an argument and a keypoint under the topic "We should adopt libertarianism", answer if the keypoint summarizes the argument | Classification
`task1292_kpa_keypoint_matching_human_cloning_topic` | Given an argument and a keypoint under the topic "We should ban human cloning", answer if the keypoint summarizes the argument | Classification
`task1293_kpa_keypoint_matching_military_companies_topic` | Given an argument and a keypoint under the topic "We should ban private military companies", answer if the keypoint summarizes the argument | Classification
`task1294_kpa_keypoint_matching_child_actors_topic` | Given an argument and a keypoint under the topic "We should ban the use of child actors", answer if the keypoint summarizes the argument | Classification
`task1295_kpa_keypoint_matching_guantanamo_bay_detection_camp_topic` | Given an argument and a keypoint under the topic "We should close Guantanamo Bay detention camp", answer if the keypoint summarizes the argument | Classification
`task1296_kpa_keypoint_matching_mandatory_retirement_topic` | Given an argument and a keypoint under the topic "We should end mandatory retirement", answer if the keypoint summarizes the argument | Classification
`task1297_kpa_keypoint_matching_nuclear_weapons_topic` | Given an argument and a keypoint under the topic "We should fight for the abolition of nuclear weapons", answer if the keypoint summarizes the argument | Classification
`task1298_kpa_keypoint_matching_urbanization_topic` | Given an argument and a keypoint under the topic "We should fight urbanization", answer if the keypoint summarizes the argument | Classification
`task1299_kpa_keypoint_matching_compulsory_voting` | Given an argument and a keypoint under the topic "We should introduce compulsory voting", answer if the keypoint summarizes the argument | Classification
`task1300_kpa_keypoint_matching_cannabis_topic` | Given an argument and a keypoint under the topic "We should legalize cannabis", answer if the keypoint summarizes the argument | Classification
`task1301_kpa_keypoint_matching_prostitution_topic` | Given an argument and a keypoint under the topic "We should legalize prostitution", answer if the keypoint summarizes the argument | Classification
`task1302_kpa_keypoint_matching_sex_selection_topic` | Given an argument and a keypoint under the topic "We should legalize sex selection", answer if the keypoint summarizes the argument | Classification
`task1303_kpa_keypoint_matching_flag_burning_topic` | Given an argument and a keypoint under the topic "We should prohibit flag burning", answer if the keypoint summarizes the argument | Classification
`task1304_kpa_keypoint_matching_women_in_combat_topic` | Given an argument and a keypoint under the topic "We should prohibit women in combat", answer if the keypoint summarizes the argument | Classification
`task1305_kpa_keypoint_matching_journalism_topic` | Given an argument and a keypoint under the topic "We should subsidize journalism", answer if the keypoint summarizes the argument | Classification
`task1306_kpa_keypoint_matching_space_exploration_topic` | Given an argument and a keypoint under the topic "We should subsidize space exploration", answer if the keypoint summarizes the argument | Classification
`task1307_kpa_keypoint_matching_vocational_education_topic` | Given an argument and a keypoint under the topic "We should subsidize vocational education", answer if the keypoint summarizes the argument | Classification
`task1308_amazonreview_category_classification` | You're given a review from Amazon and category of the product based on the review, classify whether review match the category. | Classification
`task1309_amazonreview_summary_classification` | You're given a review from Amazon and summary of the review, classify whether summary match the original review. | Classification
`task1310_amazonreview_rating_classification` | You're given a review from Amazon. Your task is to generate a rating for the product on a scale of 1-5 based on the review. | Classification
`task1311_amazonreview_rating_classification` | You're given a review from Amazon and rating of the review, classify whether rating match the review. | Classification
`task1312_amazonreview_polarity_classification` | You are given a review of Amazon's food products. Your task is to divide them into two classes: negative or positive. | Classification
`task1313_amazonreview_polarity_classification` | You're given a review from Amazon and polarity of the review, classify whether review match the polarity. | Classification
`task1314_country_abbreviation` | Given a country name, return the abbrevation name of the given country | Answer Generation
`task1315_find_range_array` | Given a list of integers, find the range of the list  | Answer Generation
`task1316_remove_duplicates_string` | Given a string, remove all the duplicate characters from the string  | Answer Generation
`task1317_country_calling_code` | Given a country name, return the calling code of the given country | Answer Generation
`task1318_country_national_dish` | Given a country name, return the national dish name of the given country | Answer Generation
`task1319_country_by_barcode_prefix` | Given a country name, return the barcode prefix of the given country | Answer Generation
`task1320_country_domain_tld` | Given a country name, return the Top Level Domain (TLD) of the given country | Answer Generation
`task1321_country_continent` | Given a country name, return the continent name of the given country | Answer Generation
`task1322_country_government_type` | Given a country name, return the government type of the given country | Answer Generation
`task1323_open_subtitles_hi_en_translation` | Translating Hindi to English (based on Open Subtitles) | Language Translation  
`task1324_open_subtitles_te_en_translation` | Translating Telugu to English (based on Open Subtitles) | Language Translation
`task1325_qa_zre_question_generation_on_subject_relation` | Generating questions by including a specific subject and certain relation to Context (based on qa_zre dataset) | Question Generation  
`task1326_qa_zre_question_generation_from_answer` | Generating questions from answers (based on qa_zre dataset)| Question Generation
`task1327_qa_zre_answer_generation_from_question` | Generating answers from questions (based on qa_zre dataset) | Answer Generation  
`task1328_qa_zre_relation_generation_from_question` | Classify relation between question and context (based on qa_zre dataset) | Classificationrelation 
`task1329_open_subtitles_en_hi_translation` | Translating English to Hindi (based on Open Subtitles) | Language Translation  
`task1330_open_subtitles_en_te_translation` | Translating English to Telugu (based on Open Subtitles) | Language Translation
`task1331_reverse_array` | Given a list of integers, reverse the order of the items in the list  | Answer Generation
`task1332_check_leap_year` | Given a year, check if it is a leap year or not | Classification
`task1333_check_validity_date_ddmmyyyy` | Given a date in dd/mm/yyyy format, check if it is a valid date or not | Classification
`task1334_sqac_answer_generation`                                | Generating answers to SQAC questions          | Answer Generation    
`task1335_sqac_question_generation`                              | Classifying race of speaker of sentence       | Race Classifier      
`task1336_peixian_equity_evaluation_corpus_gender_classifier`    | Classifying gender of speaker of sentence     | Gender Classifier     
`task1338_peixian_equity_evaluation_corpus_sentiment_classifier` | Classifying the sentiment within the sentence | Sentiment Classifier 
`task1339_peixian_equity_evaluation_corpus_text_completion`      | Replacing blanks within text for an emption   | Text completion
`task1340_msr_text_compression_compression` | Generating Compressed text based on MSR dataset | Compression
`task1341_msr_text_classification` | Generating Classification of text in MSR dataset | Classification
`task1342_amazon_us_reviews_title` | Generating Title for Amazon US review dataset | Title Generation
`task1343_amazon_us_reviews_rating` | Generating Rating for Amazon US review dataset | Rating generation
`task1344_glue_entailment_classification` | Checking if the second sentance entails the first or not | Classification
`task1345_glue_qqp_question_paraprashing` | Paraphrasing a question to generate a similar question | Text Modification
`task1346_glue_cola_grammatical_correctness_classification` | Checking grammatical correctness of a statement. | Classification
`task1347_glue_sts-b_similarity_classification` | Classifying two sentence based on semantic similarity on the scale of 0 - 5. | Classification
`task1350_opus100_translation_en_gu` | Translate a sentence in English to Gujarati | Translation  
`task1351_opus100_translation_gu_en` | Translate a sentence in Gujarati to English | Translation
`task1352_hind_encorp_translation_hi_en` | Translate a sentence in Hindi to English | Translation  
`task1353_hind_encorp_translation_en_hi` | Translate a sentence in English to Hindi | Translation
`task1354_sent_comp_classification` | Given text and headline classify if headline matches text or not | Classification
`task1355_sent_comp_summarization` | Given text generate summary about the text | Summarization
`task1356_xlsum_title_generation` | Generating title for the text in xlsum | Title Generation
`task1357_xlsum_summary_generation` | Generating summary for the text in xlsum | Summary Generation
`task1358_xlsum_title_generation` | Generates title for the text in xlsum | Title Generation
`task1359_numer_sense_answer_generation` | Generates answer to numer sense | Answer Generation
`task1360_numer_sense_multiple_choice_qa_generation` | Generating answers to numer sense | Multiple Choice QA Generation
`task1361_movierationales_classification` | Classification (based on Movie Rationales) | Classification
`task1364_hans_answer_generation` | Generating answers (based on Hans) | Answer Generation
`task1365_opustedtalks_translation` | Translation from English to Croatian using Opus_Ted Dataset | Translation
`task1366_healthfact_classification` | Find if claim belongs to a predefined category using given paragraph | Classification
`task1367_opustedtalks_translation` | Translation from Croatian to English using Opus_Ted Dataset | Translation
`task1368_healthfact_sentence_generation` | Generate a claim based on a given paragraph | Sentence Generation
`task1369_healthfact_sentence_generation` | Generate an explanation for a claim based on a given paragraph | Sentence Generation
`task1370_newscomm_classification` | Classifying the language of given statement | Classification
`task1371_newscomm_translation` | Translating news commentaries given in English to French language based on the news_Commentary dataset | Language Translation
`task1373_newscomm_translation` | Translating news commentaries given in German to Spanish language based on the news_Commentary dataset | Language Translation
`task1374_newscomm_translation` | Translating news commentaries given in Arabic to Czeck language based on the news_Commentary dataset | Language Translation
`task1375_newscomm_translation` | Translating news commentaries given in Dutch to Portuguese language based on the news_Commentary dataset | Language Translation
`task1376_newscomm_translation` | Translating news commentaries given in Italian to Zhuang language based on the news_Commentary dataset | Language Translation
`task1377_newscomm_translation` | Translating news commentaries given in French to Russian language based on the news_Commentary dataset | Language Translation
`task1378_quarel_correct_answer_generation` | Given a sentence and a question, write the correct answer based on the sentence. | Answer Generation
`task1379_quarel_incorrect_answer_generation` | Given a sentence and a question, write the incorrect answer based on the sentence. | Incorrect Answer Generation
`task1380_quarel_correct_option_generation` | Given a sentence and a question, choose the correct option number instead of exact answer based on the sentence. | Answer Generation
`task1381_quarel_incorrect_option_generation` | Given a sentence and a question, choose the incorrect option number instead of exact answer based on the sentence. | Incorrect Answer Generation
`task1382_quarel_write_correct_answer` | Writing a correct answer to a given question based on a given sentence. | Answer Generation
`task1383_quarel_write_incorrect_answer` | Writing a incorrect answer to a given question based on a given sentence. | Incorrect Answer Generation
`task1384_deal_or_no_dialog_classification` | Given a dialogue, classify whether both participants agree to the deal | Classification
`task1394_meta_woz_task_classification` | Given two task sentences, detect the domains of the task | Classification
`task1395_europa_ecdc_tm_en_sv_translation` | Translate English sentences to Swedish | Translation
`task1396_europa_ecdc_tm_en_de_translation` | Translate English sentences to German | Translation
`task1397_europa_ecdc_tm_fr_en_translation` | Translate French sentences to English | Translation
`task1398_obqa_question_generation` | Given a fact, generate a question that can be answered using the fact | Question Generation
`task1399_obqa_answer_generation` | Given a fact and question, generate an answer to the question | Answer Generation
`task1400_obqa_incorrect_answer_generation` | Given a fact and question, generate an incorrect answer to the question | Incorrect Answer Generation
`task1401_obqa_sentence_generation` | Given a question and answer pair, generate a fact statement | Sentence Generation
`task1402_clue_question_generation` | Given a Chinese passage, generate a question based on the passage | Question Generation
`task1403_check_validity_date_mmddyyyy` | Given a date in mm/dd/yyyy format, check if it is a valid date or not | Classification
`task1404_date_conversion` | Given a date in a particular format, convert it into some other format | Answer Generation
`task1405_find_median` | Given a list of integers, find the median of the input list | Answer Generation
`task1406_kth_smallest_element` | Given a list of integers and an integer k, find the kth smallest element in the list | Answer Generation
`task1407_dart_question_generation` | Generate fill-in-the-blank style questions from RDF triplets of the DART dataset | Question Generation
`task1408_dart_similarity_classification` | Classify whether two sentences (from DART) are similar or not based on their relationships | Relevance Verification
`task1409_dart_text_generation` | Generating sentences based on DART RDF relationships | Sentence Generation
`task1410_dart_relationship_extraction` | Extracting RDF relationships from DART sentences | Relationship Extraction
`task1411_dart_subject_identification` | Given a sentence (from DART), identify the subject of the sentence | Token Classification
`task1413_dart_object_identification` | Given a sentence (from DART), identify the object of the sentence | Token Classificationn
`task1414_ajgt_twitter_ar_classification` | Classify Arabic tweets (based on `ajgt_twitter_ar`) as having positive or negative sentiment | Sentiment Analysis
`task1415_youtube_caption_corrections_grammar_correction` | Given a set of closed captions (from `youtube_caption_corrections`), produce a grammatically correct version of those captions | Grammar Error Correction
`task1416_youtube_caption_corrections_incorrect_grammar_classification` | Given a set of closed captions (from `youtube_caption_corrections`), classify which words are grammatically incorrect | Grammar Error Detection
`task1418_bless_semantic_relation_classification` | Given a pair of words, deduce the type of relationship between them | Classification
`task1419_mathqa_gain` |  Given a math problem on gain and options to choose from, find the correct option that answers the problem | Multiple-Choice Question
`task1420_mathqa_general` |  Given a general math problem and options to choose from, find the correct option that answers the problem | Multiple-Choice Question
`task1421_mathqa_other` |  Given a math problem and options to choose from, find the correct option that answers the problem | Multiple-Choice Question
`task1422_mathqa_physics` |  Given a problem on physics and options to choose from, find the correct option that answers the problem | Multiple-Choice Question
`task1423_mathqa_geometry` |  Given a problem on geometry and options to choose from, find the correct option that answers the problem | Multiple-Choice Question
`task1424_mathqa_probability` |  Given a problem on probability and options to choose from, find the correct option that answers the problem | Multiple-Choice Question
`task1425_country_iso_numeric` | Given a country name, return the numeric ISO of the given country | Answer Generation
`task1426_country_independence_year` | Given a country name, return the year of independence of the given country | Answer Generation
`task1427_country_region_in_world` | Given a country name, return the located region in the world map of the given country | Answer Generation
`task1428_country_surface_area` | Given a country name, return the surface area in square-kilometer of the given country | Answer Generation
`task1429_evalution_semantic_relation_classification` | Given a pair of words, deduce the type of relationship between them | Classification
`task1431_head_qa_answer_generation` | Answering a multiple-choice question | Answer Generation
`task1432_head_qa_language_translation_en_to_es` | Translation from English to Spanish | Language Translation 
`task1433_head_qa_language_translation_es_to_en` | Translation from Spanish to English | Language Translation 
`task1434_head_qa_classification` | Classifying questions into topics | Classification
`task1435_ro_sts_parallel_language_translation_ro_to_en` | Translation from Romanian to English | Language Translation 
`task1436_ro_sts_parallel_language_translation_en_to_ro` | Translation from English to Romanian | Language Translation 
`task1437_doqa_cooking_question_generation` | Given a paragraph about cooking, and a set of conversational question answers about the paragraph, generate a relevant question to the topic of the paragraph | Question Generation -> Contextual Question Generation, Dialogue Understanding
`task1438_doqa_cooking_answer_generation` | Given a paragraph about cooking, and a set of conversational question answers about the paragraph, answer a follow-up question from the paragraph | Question Answering -> Contextual Question Answering -> Extractive, Dialogue Understanding
`task1439_doqa_cooking_isanswerable` | Given a paragraph about cooking, and a set of conversational question answers about the paragraph, say whether the follow-up question can be answered from the passage| Classification, Dialogue Understanding 
`task1440_doqa_movies_question_generation` | Given a paragraph about movies, and a set of conversational question answers about the paragraph, generate a relevant question to the topic of the paragraph | Question Generation -> Contextual Question Generation, Dialogue Understanding
`task1441_doqa_movies_answer_generation` | Given a paragraph about movies, and a set of conversational question answers about the paragraph, answer a follow-up question from the paragraph | Question Answering -> Contextual Question Answering -> Extractive, Dialogue Understanding
`task1442_doqa_movies_isanswerable` | Given a paragraph about movies, and a set of conversational question answers about the paragraph, say whether the follow-up question can be answered from the passage| Classification, Dialogue Understanding 
`task1443_string_to_number` | Given a string of spelled out digits return the number the string represents | Answer Generation
`task1444_round_power_of_two` | Given a list of integers round them to the nearest power of two | Answer Generation, Arthimetic
`task1445_closest_integers` | Given a list of integers return the difference between the two closest integers | Answer Generation, Arthimetic
`task1446_farthest_integers` | Given a list of integers return the difference between the two farthest integers | Answer Generation, Arthimetic
`task1447_drug_extraction_ade` | Given a sentence from the ADE dataset, return the list of tokens that mentions names of the drugs or medicines from the ADE Dataset. | Entity Detection
`task1448_disease_entity_extraction_ncbi_dataset` | Given a sentence from the NCBI dataset, return the list of tokens that mentions names of the diseases or disorders from the NCBI Dataset. | Entity Detection
`task1449_disease_entity_extraction_bc5cdr_dataset` | Given a sentence from the BC5CDR dataset, return the list of tokens that mentions names of the diseases or disorders from the BC5CDR Dataset. | Entity Detection
`task1451_drug_dose_extraction` | Given a sentence and a drug from the ADE dataset, return the list of tokens that mentions of dose of that particular drug. | Entity Detection
`task1452_location_entity_extraction_btc_corpus` | Given a sentence from the BTC dataset, return the list of tokens that mentions of locations/places. | Entity Detection
`task1453_person_entity_extraction_btc_corpus` | Given a sentence from the BTC dataset, return the list of tokens that mentions of person names. | Entity Detection
`task1479_organization_entity_extraction_btc_corpus` | Given a sentence from the BTC dataset, return the list of tokens that mentions of companies or organizations. | Entity Detection
`task1480_gene_extraction_jnlpba_dataset` | Given a sentence from the JNLPBA dataset, return the list of tokens that mentions of genes or proteins. | Entity Detection
`task1481_gene_extraction_bc2gm_dataset` | Given a sentence from the BC2GM dataset, return the list of tokens that mentions of genes or proteins. | Entity Detection
`task1482_gene_extraction_chemprot_dataset` | Given a sentence from the ChemProt dataset, return the list of tokens that mentions of protein. | Entity Detection
`task1483_chemical_extraction_chemprot_dataset` | Given a sentence from the ChemProt dataset, return the list of tokens that mentions of chemical substances. | Entity Detection
`task1484_gene_extraction_linnaeus_dataset` | Given a sentence from the Linnaues dataset, return the list of tokens that mentions of genes. | Entity Detection
`task1485_organ_extraction_anem_dataset` | Given a sentence from the AnEM dataset, return the list of tokens that mentions of organs in the body. | Entity Detection
`task1486_cell_extraction_anem_dataset` | Given a sentence from the AnEM dataset, return the list of tokens that mentions of cells in the body. | Entity Detection
`task1487_organism_substance_extraction_anem_dataset` | Given a sentence from the AnEM dataset, return the list of tokens that mentions of organs in the body. | Entity Detection
`task1488_sarcasmdetection_headline_classification` | Given a news headline in English, classify whether it is sarcastic or non-sarcastic in nature. | Classification
`task1489_sarcasmdetection_tweet_classification` | Given a twitter in English, classify whether it is sarcastic or non-sarcastic in nature. | Classification
`task1490_bengali_personal_hate_speech_binary_classification` | Given a hateful post in Bengali, classify whether it is personal or non-personal in nature. | Classification
`task1491_bengali_political_hate_speech_binary_classification` | Given a hateful post in Bengali, classify whether it is political or non-political in nature. | Classification
`task1492_bengali_religious_hate_speech_binary_classification` | Given a hateful post in Bengali, classify whether it is religious or non-religious in nature. | Classification
`task1493_bengali_geopolitical_hate_speech_binary_classification` | Given a hateful post in Bengali, classify whether it is geopolitical or non-geopolitical in nature. | Classification
`task1494_bengali_hate_speech_classification` | Given a hateful post in Bengali, classify whether it is political, geopolitical, religious or personal in nature. | Classification
`task1495_adverse_drug_event_classification` | Given a sentence, classify whether it contains any adverse drug event. | Classification
`task1496_bengali_reviews_sentiment_classification` | Given a restaurant review in Bengali, classify whether the sentiment is positive or negative. | Classification
`task1497_bengali_book_reviews_sentiment_classification` | Given a book review in Bengali, classify whether the sentiment is positive or negative. | Classification
`task1498_24hour_to_12hour_clock` | Given a timestamp in 24-hour format, convert it to 12-hour format | Answer Generation
`task1499_dstc3_summarization` | Summarization of conversations in DSTC 3 | Summarization
`task1500_dstc3_classification` | Classification of Price Range in conversations in DSTC 3| Classification
`task1501_dstc3_answer_generation` | Generating answers to DSTC 3 conversations related questions | Answer Generation
`task1502_hatexplain_classification` | Classification of type of tweet in Hatexplain | Classification
`task1503_hatexplain_classification` | Identification of target community in tweet in Hatexplain | Classification
`task1504_hatexplain_answer_generation` | Passage Selection of offensive or hate speech phrases in tweets is Hatexplain | Answer Generation
`task1505_root09_semantic_relation_classification` | Given a pair of words, deduce the type of relationship between them | Classification
`task1506_celebrity_minimal_dob_span` | Find the date of birth of a celebrity given a sentence bio | Answer Generation
`task1507_boolean_temporal_reasoning` | Given a statement about date and time values, deduce whether it is true or false | Classification
`task1508_wordnet_antonyms` | Given an adjective, generate its antonym | Answer Generation
`task1509_evalution_antonyms` | Given a word generate its antonym | Answer Generation
`task1510_evalution_relation_extraction` | Given a phrase describing the relationship between two words, extract the words and the lexical relationship between them | Answer Generation
`task1514_flores_translation_entone` | Translate from English to Nepali | Translation
`task1515_imppres_longtextgeneration` | Given a premise, generate hypothesis | Text Generation
`task1516_imppres_naturallanguageinference` | Classify a given premise and hypothesis pair | Classification
`task1517_limit_classfication` | Classifying sentence based on the condition that it contains a motion of a physical entity or not.| Classification
`task1518_limit_answer_generation` | Identifying the entities in a sentence where these entities take part in a physical motion. | Question Answering
`task1519_qa_srl_question_generation` | Using given sentence and a verb,generating questions which can be answered from the sentence. | Question Generation
`task1520_qa_srl_answer_generation` | Generating answers to the questions based on the given sentence| Question Answering
`task1529_scitail1.1_classification` | Determining if there is entailment between Hypothesis and Premise | Classification
`task1530_scitail1.1_sentence_generation` | Generating a Premise that entails the Hypothesis | Text Generation
`task1531_daily_dialog_type_classification` | Classify the input sentence into one of the 5 classes : unknown, commissive, question, information, directive| Classification
`task1532_daily_dialog_emotion_classification` | Classify the conversation sentences of input passage into the following emotions: anger, disgust, fear, happiness, sadness, No emotion | Classification
`task1533_daily_dialog_formal_classification` | Classify the conversation sentences of input passage into the following outputs: formal and informal | Classification
`task1534_daily_dialog_question_classification` | Classify if the first sentence of a conversation is a question | Classification
`task1535_daily_dialog_uniqueness_classification` | Classify if the conversation sentences of the input passage convey more than 2 unique emotions  | Classification
`task1536_daily_dialog_happiness_classification` | Classify if the conversation sentences of the input passage convey only happiness emotion or not.| Classification
`task1537_tamil_offenseval_dravidian_classification` | Given a statement in Tamil, classify whether it is offensive or not | Classification
`task1538_malayalam_offenseval_dravidian_classification` | Given a statement in Malayalam, classify whether it is offensive or not | Classification
`task1539_kannada_offenseval_dravidian_classification` | Given a statement in Kannada, classify whether it is offensive or not | Classification
`task1540_parsed_pdfs_summarization` | Given a text, generate a title for it | Summarization
`task1541_agnews_classification` | Given a short article, classify the article based on its category | Classification
`task1542_every_ith_element_from_starting` | Given a list return every ith element of the list starting from the 1st element | Answer Generation
`task1543_conll2002_parts_of_speech_tagging_answer_generation` | Given a question in Dutch language, write the part-of-speech tag for each word in the question | Answer Generation
`task1544_conll2002_named_entity_recognition_answer_generation` | Given a question in Dutch language, write the named entities from the question if present | Answer Generation
`task1545_conll2002_person_name_extraction_answer_generation` | Given a question in Dutch language, write the named entities from the question if present | Answer Generation
`task1546_conll2002_location_name_extraction_answer_generation` | Given a question in Dutch language, write the location names from the question if present | Answer Generation
`task1548_wiqa_binary_classification` | Binary Classification (based on steps in wiqa) | Answer Generation
`task1549_wiqa_answer_generation_missing_step` | Generating answer to place missing step in a series (based on wiqa) | Answer Generation
`task1551_every_ith_element_from_kth_element` | Given a list return every ith element of the list starting from the kth element | Answer Generation
`task1552_scitail_question_generation` | Generating questions (based on SciTail) | Question Generation
`task1553_cnn_dailymail_summarization` | Generating summary to news articles | Summarization
`task1554_scitail_classification` | Classifying supporting and non supporting statements from SciTail  | Classification
`task1555_scitail_answer_generation` | Generating answers to SciTail Sentence-Questions | Answer Generation
`task1556_scitail_passage_generation` | Generating passage based on SciTail Question-Answer | Passage Generation
`task1557_jfleg_answer_generation` | Generating answers (based on jfleg) | Answer Generation  
`task1558_jfleg_incorrect_answer_generation` | Generating incorrect answers (based on jfleg) | Incorrect Answer Generation
`task1559_blimp_binary_classification` | Classifying sentences (based on Blimp) | Binary Classification  
`task1560_blimp_binary_classification` | Classifying sentences (based on Blimp) | Binary Classification 
`task1561_clickbait_new_bg_summarization` | Providing a title summary to passage from Clickbait_new_bg dataset | Summarization
`task1562_clickbait_new_bg_answer_generation` | Generating fake news score from passage in Clickbait_new_bg dataset | Classification
`task1563_clickbait_new_bg_answer_generation` | Generating click bait score from passage in Clickbait_new_bg dataset | Classification
`task1564_triviaqa_answer_generation` | Generating answers to questions in TriviaQA dataset | Answer generation
`task1565_triviaqa_classification` | Finding answer to multiple choice questions in TriviaQA dataset | Answer generation
`task1566_propara_structured_text_generation` | Generate entities from given text | Structured Text Generation
`task1567_propara_question_generation` | Generate question from the given passage | Question Generation
`task1568_propara_classification` | Based on the passage, event, and entity, classify locations | Classification
`task1569_cmrc2018_question_generation` | Generate question from the given passage | Question Generation
`task1570_cmrc2018_answer_generation` | Generate the right answer to a given question from the context passage | Answer Generation
`task1571_cmrc2018_answer_generation_starting_index` | Generate starting index of the answer span to a given question from the context passage | Answer Generation
`task1572_samsum_summary` | Generate a summary of given conversations | Summarization
`task1573_samsum_classification` | Classify whether given two dialogue sentences are sequential or not | Classification
`task1574_amazon_reviews_multi_language_identification` | Classification of product review language | Classification
`task1575_amazon_reviews_multi_sentiment_classification` |Classification of product reviews into good or bad| Classification
`task1576_amazon_reviews_multi_english_language_classification` | Classification of reviews based on whether it is English or not|Classification
`task1577_amazon_reviews_multi_japanese_language_classification` | Classification of reviews based on whether it is Japanese or not|Classification
`task1578_gigaword_summarization` | Generating summary to gigaword passages | Summary Generation
`task1579_gigaword_incorrect_summarization` | Generating incorrect summary to gigaword passages | Incorrect Summary Generation
`task1580_eqasc-perturbed_question_generation` | Generating questions for eQASC facts | Question Generation
`task1581_eqasc-perturbed_answer_generation` | Generating answers for eQASC facts and questions | Answer Generation
`task1582_bless_hypernym_generation` | Given a concept word, generate a hypernym for it | Answer Generation
`task1583_bless_meronym_classification` | Given an object and a part, decide whether the object has that part | Classification
`task1584_evalution_meronym_classification` | Given an object and a part, decide whether the object has that part | Classification
`task1585_root09_hypernym_generation` | Given a concept word, generate a hypernym for it | Answer Generation
`task1586_scifact_title_generation` | Title Generation | Title_Generation
`task1587_scifact_classification` | Classification | Classification
`task1588_tecla_classification` | Classification | Classification
`task1589_scifact_classification` | Classification | Classification
`task1590_diplomacy_text_generation` | Text generation based on diplomacy_detection | Text_Generation
`task1591_allocine_classification` | Classification (based on allocine) | Classification  
`task1592_yahoo_answers_topics_classfication` | Classification based on yahoo_answers_topics | Classification
`task1593_yahoo_answers_topics_classification` | Classification based on yahoo_answers_topics | Classification  
`task1594_yahoo_answers_topics_question_generation` | Question Generation based on yahoo_answers_topics | Question_Generation
`task1595_event2mind_text_generation_1` | Creating text (emotional reaction) based on event2Mind event prompts | Text Generation
`task1596_event2mind_text_generation_2` | Creating text (intent) based on event2Mind event prompts | Text Generation
`task1597_nyc_slot_filling` | Categorizing elements of information from text from the NYC database | Slot Filling
`task1598_nyc_long_text_generation` | Creating sentences based off of some information from the NYC database | Long Text Generation
`task1599_smcalflow_classification` | Classify given utterance into user or agent | Classification
`task1600_smcalflow_sentence_generation`| Given a agents' reply, generate a users' utterance | Sentence Generation
`task1601_webquestions_answer_generation` | Given a question and URL, generate an answer | Answer Generation
`task1602_webquestion_question_genreation` | Given an answer and URL, generate a question | Question Generation
`task1603_smcalflow_sentence_generation` | Given a user utterance, generate agents' utterance | Sentence Generation
`task1604_ethos_text_classification` | Classifying text to Hate or Not Hate | Text Classification
`task1605_ethos_text_classification` | Classifying text to Violence or Not Violence | Text Classification
`task1606_ethos_text_classification` | Classifying if text has Gender Crticism | Text Classification
`task1607_ethos_text_classification` | Classifying text to Religious Criticism | Text Classification
`task1608_xquad_en_answer_generation` | Generating answers to xquad en questions | Answer Generation
`task1609_xquad_en_question_generation` | Generating questions (based on xquad en) | Question Generation
`task1610_xquad_es_answer_generation` | Generating answers to xquad es (Spanish) questions | Answer Generation
`task1611_xquad_es_question_generation` | Generating questions (based on xquad es (Spanish)) | Question Generation
`task1612_sick_label_classification` | Classification of labels correctly to show relation between two sentences (based on the sick dataset)| Classification
`task1613_sick_given_category_generate_sentence` | Generate a sentence based  that meets the given criteria  (based on the sick dataset) | Sentence Generation
`task1614_sick_text_modify` | Derive a sentence from the given sentence (based on the sick dataset) | Text modification
`task1615_sick_tclassify_b_relation_a` | Classify the correct relation between the second and first sentence (based on the sick dataset) | Classification
`task1616_cc_alligned_translate_eng_tel` | Translate from English to Telugu | Translation
`task1617_cc_alligned_translate_tel_eng` | Translate from Telugu to English | Translation
`task1618_cc_alligned_classify_tel_eng` | Classify if a sentence is in Telugu or English Language | Language Classification
`task1619_menyo20k-mt_en_yo_translation` | Given an English sentence convert it to Yoruba. | Translation
`task1620_menyo20k-mt_yo_en_translation` | Given a sentence in Yoruba convert it to English. | Translation
`task1621_menyo20k-mt_en_yo_language_identification` | Given a sentence identify if it is in Yoruba or English. | Language Identification
`task1622_disfl_qa_text_modication` | Given a disfluent question, convert it to a proper question. | Text Modification
`task1623_disfl_qa_disfluent_question_classification` | Given a question, predict whether it is disfluent or proper. | Classification
`task1624_disfl_qa_question_yesno_classification` | Given a context and a question, predict if a question is answerable or not based on the context. | Classification
`task1625_disfl_qa_asnwer_generation` | Given a context and a question, return an answer to the question based on context. | Answer Generation
`task1626_copa_hr_question_answering` | Given a sentence and 2 labels, select the correct label | Answer Selection
`task1627_copa_hr_classification` | Given a question and two label, classify the group in which the choice and the statement are related | Classification
`task1628_copa_hr_question_answering` | Given a sentence and four label, select the correct label. | Answer Selection 
`task1629_copa_hr_classification` | Given two statements, classify the relation between them | Classification
`task1630_openpi_classification` | Given a passage as input, print the output as the category to which the passage belongs | Classification
`task1631_openpi_answer_generation` | Use the given information to generate a grammatically correct sentence as output | Answer Generation
`task1637_doqa2.1_cooking_text_summarization` | Generating title from text (based on DoQA 2.1 cooking data) | Text Summarization
`task1638_doqa2.1_movies_text_summarization` | Generating title from text (based on DoQA 2.1 movie data) | Text Summarization
`task1639_doqa2.1_travel_text_summarization` | Generating title from text (based on DoQA 2.1 travel data) | Text Summarization
`task1640_aqa1.0_answerable_unanswerable_question_classification` | Classifying questions (based on AQA 1.0) | Classification
`task1645_medical_question_pair_dataset_text_classification` | Classification of Medical Question Pair Dataset in two categories | Text Classification
`task1646_dataset_card_for_catalonia_independence_corpus_text_classification` | Classification of Catalonia Independence Corpus into three categories | Text Classification
`task1647_opus_books_en-pt_translation` | Translation from English to Portuguese using opus dataset | Translation
`task1648_opus_books_en-sv_translation` | Translation from English to Swedish using opus dataset | Translation
`task1649_opus_books_en-no_translation`	| Translation from English to Norwegian using opus dataset | Translation
`task1650_opus_books_en-fi_translation` | Translation from English to Finnish using opus dataset | Translation
`task1651_opus_books_en-es__translation` | Translation from English to Spanish using opus dataset | Translation
`task1652_opus_books_ca-en_translation` | Translation from Catalan to English using opus dataset | Translation
`task1654_mkb_translation`|Translation of sentence from English to Hindi|Translation
`task1655_mkb_translation`|Translation of sentence from Hindi to English|Translation 
`task1656_gooaq_answer_generation`|short_answer generation for given question|Answer_Generation
`task1657_gooaq_question_generation`|question generation for a given answer|Question Generation
`task1658_billsum_summarization` | Generating summary (based on billsum) | Summarization
`task1659_title_generation` | Generating Title (based on billsum) | Title Generation
`task1660_super_glue_question_generation` | Generating guestions (based on super_glue) | Question Generation  
`task1661_super_glue_classification` | Classification (based on super_glue) | Classification
`task1662_cedr_ru_classification`| Generating correct emotion label corresponding to the given Russian text. | Classification
`task1663_cedr_ru_incorrect_classification` | Generating incorrect emotion label corresponding to the given Russian text. | Incorrect Classification
`task1664_winobias_text_generation` | Identifying coreferences in a given sentence and generating the set of coreference words in the sentence. | Text Generation
`task1665_trainglecopa_question_generation` | Generating a Question for the given premise from traingleCOPA dataset | Question Generation
`task1666_cail2018_answer_generation`| Generating answers (based on cail2018) | Answer Generation
`task1667_cail2018_answer_generation` | Generating answers (based on cail2018) | Answer Generation
`task1669_md_gender_bias_text_modification` | Modifying text (based on md gender bias) | Text Modification
`task1670_md_gender_bias_text_modification` | Modifying text (based on md gender bias) | Text Modification
`task1676_xquad-ca_translation` | Translate questions from Catalan to English in the XQuAD-ca dataset | Translation
`task1677_xquad-ca_translation` | Translate questions from English to Catalan in the XQuAD-ca dataset | Translation
`task1678_mathqa_answer_selection` | Selecting answers to mathqa questions | Answer Selection
`task1685_menyo20k_translation` | Language translation from English to Yoruba | Translation  
`task1686_menyo20k_translation` | Language translation from Yoruba to English| Translation  
`task1689_qed_amara_translation` | Language translation from English to French| Translation  
`task1690_qed_amara_translation` | Language translation from French to English | Translation  
`task1691_qed_amara_translation` | Language translation from English to Spanish | Translation  
`task1692_qed_amara_translation` | Language translation from Spanish to English | Translation  
`task1703_ljspeech_textmodification` | Digit to Text in ljspeech | Text Modification 
`task1704_ljspeech_textmodification` | Text to Digit in ljspeech | Text Modification
`task1705_ljspeech_classification` | Finding Proper Nouns in ljspeech | Classification
`task1706_ljspeech_classification` | Correct Punctuation in ljspeech| Classification
`task1711_poki_text_generation` | Given a title, generate a short poem that should look like written by a kid. | Text Generation
`task1712_poki_classification` | Given a short poem, classify whether is written by an elementary kid or a high school kid. | Classification
`task1713_convai3_sentence_generation` | Given a user's request, predict what the user is trying to do. | Sentence Generation
`task1714_convai3_sentence_generation` | Given a user's intent and computer response, predict what will the user's response will be. | Sentence Generation
`task1719_civil_comments_url_extraction` | Extraction of Urls| Answer Generation 
`task1720_civil_comments_toxicity_classification` | Classify toxicity | Classification
`task1721_civil_comments_obscenity_classification` | Classify Obscenity | Classification
`task1722_civil_comments_threat_classification` | Classify Threat | Classification
`task1723_civil_comments_sexuallyexplicit_classification` | Classify Sexually Explicit Content| Classification
`task1724_civil_comments_insult_classification` | Classify Insult | Classification
`task1725_civil_comments_severtoxicity_classification` | Classify Severe Toxicity | Classification
`task1726_mathqa_correct_answer_generation` | Generate correct answers for math questions | Answer Generation
