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
`task044_essential_terms_identifying_essential_words`	| Identifying words or phrases of the question that are essential for choosing the correct answer.	| Verification
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
`task058_multirc_question_answering`	| Reading Comprehension Over Multiple Sentences.	| Answer Generation
`task059_ropes_story_generation`	| Generating a story about relations in the given paragraph.	| Long Text Generation
`task060_ropes_question_generation`	| Constructing questions regarding relations in the given paragraph.	| Question Generation
`task061_ropes_answer_generation`	| Answering questions regarding relations in the given paragraph.	| Answering Generation
`task062_bigbench_repeat_copy_logic`	|  Generating text that follows simple logical operations such as "repeat", "before", "after" etc.	| Logic
`task073_CommonsenseQA_answer_generation`	|  Answering questions based on commonsense knowledge.	| Answer Generation
`task085_unnatural_addsub_arithmetic`	|  Performing Arithmetic with swapped operator symbols.	| Arithmetic
`task086_translated_symbol_arithmetic`	|  Performing Arithmetic with translated operator symbols.	| Arithmetic
`task087_new_operator_addsub_arithmetic`	|  Performing Arithmetic with newly defined operator symbols.	| Arithmetic
`task088_identify_typo_verification`	|  Identifying typo in a sentence.	| Verification
`task089_swap_words_verification`	|  Identifying swapped words in a sentence.	| Verification
`task090_equation_learner_algebra`	|  Answering based on the given equation.	| Algebra
`task091_operation_finder_arithmetic`	|  Finding the arithmetic operator.	| Arithmetic
`task092_check_prime_classification`	|  Finding whether the number is prime or not.	| Mathematics







