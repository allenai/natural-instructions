
# Task Hierarchy

## Guidelines / FAQs for Contributors:

- Massaging the task hierarchy categories is somewhat encouraged.
- `src/auto_add_domain.py` is helpful for adding domains for all tasks in any particular dataset

## Task Categories

- `Translation`
- `Question Answering`
- `Program Execution`
- `Question Generation`
- `Sentiment Analysis`
- `Text Categorization`
- `Text Matching`
- `Toxic Language Detection`
- `Cause Effect Classification`
- `Information Extraction`
- `Textual Entailment`
- `Wrong Candidate Generation`
- `Named Entity Recognition`
- `Commonsense Classification`
- `Fill in The Blank`
- `Text Completion`
- `Sentence Composition`
- `Title Generation`
- `Language Identification`
- `Question Understanding`
- `Sentence Perturbation`
- `Answerability Classification`
- `Summarization`
- `Coreference Resolution`
- `Text Quality Evaluation`
- `Text to Code`
- `Paraphrasing`
- `Dialogue Generation`
- `Question Rewriting`
- `Word Semantics`
- `Pos Tagging`
- `Linguistic Probing`
- `Story Composition`
- `Speaker Identification`
- `Word Analogy`
- `Data to Text`
- `Stereotype Detection`
- `Negotiation Strategy Detection`
- `Dialogue Act Recognition`
- `Gender Classification`
- `Coherence Classification`
- `Explanation`
- `Ethics Classification`
- `Word Relation Classification`
- `Sentence Ordering`
- `Answer Verification`
- `Mathematics`
- `Intent Identification`
- `Keyword Tagging`
- `Code to Text`
- `Dialogue State Tracking`
- `Text Simplification`
- `Stance Detection`
- `Fact Verification`
- `Grammar Error Detection`
- `Section Classification`
- `Number Conversion`
- `Style Transfer`
- `Speaker Relation Classification`
- `Irony Detection`
- `Question Decomposition`
- `Overlap Extraction`
- `Grammar Error Correction`
- `Spelling Error Detection`
- `Entity Generation`
- `Sentence Expansion`
- `Discourse Connective Identification`
- `Discourse Relation Classification`
- `Poem Generation`
- `Entity Relation Classification`
- `Punctuation Error Detection`
- `Spam Classification`
- `Paper Review`
- `Sentence Compression`
- `Preposition Prediction`
- `Misc.`

## Reasoning

- `Abductive Reasoning`
- `Analogical Reasoning`
- `Argument Reasoning`
- `Causal Reasoning`
- `Commonsense Reasoning`: Tasks related to activities humans do in daily life e.g. eating breakfast in the morning, sleeping during night etc.
  - `Commonsense Reasoning -> Numerical Commonsense Reasoning`: Tasks which requires numerical commonsense knowledge e.g. a car has 4 wheels.
  - `Commonsense Reasoning -> Physical Reasoning`: Tasks involving physical interactions with objects e.g. a knife (and not a paper) is used to cut objects
  - `Commonsense Reasoning -> Social Situations`
  - `Commonsense Reasoning -> Spatial Reasoning`
- `Counterfactual Reasoning`
- `Cross-document Reasoning`
- `Deductive Reasoning`
- `Discrete Reasoning`
- `Ethical Judgement`
- `Ethics`
- `Grammatical Reasoning`
- `Logical Reasoning`
  - `Logical Reasoning -> Reasoning with Symbols`: Tasks where symbols represent various things e.g. if X is the number of apples in the fridge today morning and Y is the number remaining after I ate a few apples, X-Y is the number of apples I ate.
- `Mathematics`
  - `Mathematics -> Algebra`
  - `Mathematics -> Arithmetic`
  - `Mathematics -> Combinatorics`
  - `Mathematics -> Counting`: Count an attribute of input e.g. a task to count number of vowels in a given word
  - `Mathematics -> Geometry`
  - `Mathematics -> Statistics`
- `Multihop Reasoning`
- `Numerical Reasoning`
  - `Numerical Reasoning -> Numerical Commonsense Reasoning`: Tasks which requires numerical commonsense knowledge e.g. a car has 4 wheels.
- `Planning`: Tasks which need some sort of planning e.g. how to go to Hawaii?
- `Quantitative Reasoning`
- `Reasoning on Actions`
- `Reasoning on Numbers`: When inputs are numbers, e.g. finding the maximum of a list
- `Reasoning on Objects`
- `Reasoning on Social Interactions`
- `Reasoning on Strings`
- `Reasoning with Symbols`
- `Relational Reasoning`
- `Scientific Reasoning`
- `Temporal Reasoning`
- `Textual Entailment`
  - `Textual Entailment -> Abductive Reasoning`
  - `Textual Entailment -> Analogical Reasoning`
  - `Textual Entailment -> Deductive Reasoning`
  - `Textual Entailment -> Inductive Reasoning`

## Domain

* `Accounting`
* `Animals`
* `Anthropology`
* `Architecture`
* `Art`
* `Astronomy`
* `Biology`
  * `Biology -> Anatomy`
  * `Biology -> Bioinformatics`
  * `Biology -> Clinical Knowledge`
  * `Biology -> Human Biology`
  * `Biology -> Virology`
* `Books`
* `Business Ethics`
* `Captions`
  * `Captions -> Image Captions`
  * `Captions -> Video Captions`
* `Chemistry`
* `Code`
  * `Code -> Language`
	* `Code -> Language -> Python`
	* `Code -> Language -> SQL`
  * `Code -> Repo`
	* `Code -> Repo -> Github`
	* `Code -> Repo -> Stack Overflow`
* `Commonsense`
  * `Commonsense -> Concepts and Relations`
	* `Commonsense -> Concepts and Relations -> Physical Commonsense`: a context involving two physical objects with contrasting properties, usage, locations, etc.
	* `Commonsense -> Concepts and Relations -> Social Commonsense`: a situation involving two people with contrasting attributes, emotions, social roles, etc.
	* `Commonsense -> Concepts and Relations -> Spatial Commonsense`
  * `Commonsense -> Stories`
* `Computer Science`
  * `Computer Science -> Computer Security`
  * `Computer Science -> Machine Learning`
* `Conference`
* `Countries`
* `Debatepedia`
* `Dialogue`
* `Econometrics`
* `Economics`
  * `Economics -> Macroeconomics`
  * `Economics -> Microeconomics`
* `Electrical Engineering`
* `English Exams`
* `Fiction`
* `Food`
* `Formal Fallacy`
* `Game`
  * `Game -> Card Game`
* `Geography`
* `Global Facts`
* `Government and Politics`
* `Healthcare`
* `History`
  * `History -> 9/11 Reports`
  * `History -> European History`
* `Human Race`
* `Human Sexuality`
* `International Law`
* `Jurisprudence`
* `Justice`
* `Knowledge Base`
  * `Knowledge Base -> Freebase`
  * `Knowledge Base -> Wikidata`
* `Law`
* `Linguistics`
* `Literature`
* `Logic`
  * `Logic -> Formal logic`
  * `Logic -> Propositional Logic`
* `Management`
* `Marketing`
* `Mathematics`
* `Medical Genetics`
* `Medicine`
* `Miscellaneous`
* `Moral Scenarios`
* `Movies`
* `Music`
* `Narrative`
  * `Narrative -> Everyday Events`
* `Natural Science`
  * `Natural Science -> School Science Textbooks`
* `News`
* `Nutrition`
* `Personal Narratives`
* `Philosophy`
* `Physics`
* `Pop Culture`
* `Prehistory`
* `Professions`
* `Psychology`
* `Public Places`
  * `Public Places -> Restaurants`
* `Public Relations`
* `Reviews`
  * `Reviews -> Books`
  * `Reviews -> Electronics and Grocery`
  * `Reviews -> Food`
  * `Reviews -> Movies`
  * `Reviews -> Music`
  * `Reviews -> Restaurants`
  * `Reviews -> TripAdvisor`
* `Scientific Research Papers`
* `Security: Environmental Security`
* `Security: National Security`
* `Social Media`
  * `Social Media -> Reddit`
  * `Social Media -> Text Message`
  * `Social Media -> Twitter`
* `Sociology`
* `Sports`
  * `Sports -> NFL`
* `Statistics`
* `Stereotypes`
* `Story`
* `TED Talks`
* `US Foreign Policy`
* `Web`
* `Wikipedia`
* `World Religions`

## Language

- https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes: ISO language name column
