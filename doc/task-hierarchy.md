
# Task Hierarchy

## Guidelines / FAQs for Contributors:

- Massaging the task hierarchy categories is somewhat encouraged.
- If a subcategory (e.g. `Question Answering -> Contextual Question Answering -> Extractive`) is mentioned, don't mention its parent category (`Question Answering -> Contextual Question Answering`)
- `src/auto_add_domain.py` is helpful for adding domains for all tasks in any particular dataset
## Task Categories   
- `Classification`
  - `Classification -> Answer Type Classification`: Classify a text that contains a question to the type of answer that is expected (e.g., multiple choice, extractive, abstractive etc.) 
  - `Classification -> Intent Classification`: Classify a text to a pre-defined set of intent classes  
  - `Classification -> Pairwise Classification`: Classify a pair of text sequences to a target class
  - `Classification -> Topic Classification`
  - `Classification -> Verification`: Verification is a sub-category for classification and it is used for binary classifications. The task is to verify whether a given descriptive attribute applies to a given text or not (binary output) e.g. if the paragraph contains offensive content or not. In the verification tasks, the potential outputs are mentioned in the definition.
    - `Classification -> Verification -> Answer Correctness Verification`: Verify whether the answer is correct
	- `Classification -> Verification -> Answer Verification`: Verify whether a text answers the question
	- `Classification -> Verification -> Claim Verification`
	- `Classification -> Verification -> Clarification Verification`
	- `Classification -> Verification -> Entailment Verification`
	- `Classification -> Verification -> Ethical Verification`
	- `Classification -> Verification -> Grammar Verification`: Verify whether a text is grammatical
	- `Classification -> Verification -> Paraphrase Verification`: Verify whether a text sequence is a paraphrase of another text sequence
	- `Classification -> Verification -> Question Correctness Verification`
	- `Classification -> Verification -> Relevance Verification`	
	  - `Classification -> Verification -> Relevance Verification -> Category Verification`
	  - `Classification -> Verification -> Relevance Verification -> Title Verification`
	- `Classification -> Verification -> Statement Verification`: Verify whether a text statement is true or false
	- `Classification -> Verification -> Sufficient Information Verification`: Verify whether a text contains sufficient information to answer a question
	- `Classification -> Verification -> Summary Verification`
	- `Classification -> Verification -> Translation Verification`: Verify whether a text sequence is a translation of another text sequence
- `Command Execution`
- `Coreference`
  - `Coreference -> Entity Coreference`
  - `Coreference -> Pronoun Disambiguation`
- `Detection` : Detection tasks are to find something in the input. For example, detecting the entities in a review or detecting the motivation of something. Detection tasks can be text generation, classification, etc., and possible outputs are not necessarily given in the definition.
  - `Detection -> Aspect Detection`
  - `Detection -> Capability Detection`
  - `Detection -> Cause Detection`
  - `Detection -> Character Detection`
  - `Detection -> Desire Detection`
  - `Detection -> Effect Detection`
  - `Detection -> Emotion Detection`
    - `Detection -> Emotion Detection -> Classification`
  - `Detection -> Entity Detection`
	- `Detection -> Entity Detection -> Classification`: Classify the text to a pre-defined set of entities (closed set)
	- `Detection -> Entity Detection -> Extractive`: Extract the entity from the text (open set)
	- `Detection -> Entity Detection -> Sentient Entity Detection`
  - `Detection -> Event Detection`
  - `Detection -> Fake News Detection`
  - `Detection -> Intent Detection`
  - `Detection -> Location Detection`
  - `Detection -> Motivation Detection`
  - `Detection -> Need Detection`
  - `Detection -> Obstacle Detection`
  - `Detection -> Order Detection`
  - `Detection -> Reaction Detection`
	- `Detection -> Reaction Detection -> Emotional Reaction Detection`
  - `Detection -> Relation Detection`
  - `Detection -> Stance Detection`
    - `Detection -> Stance Detection -> Classification`
	  - `Detection -> Stance Detection -> Classification -> Verification`
  - `Detection -> Stereotype Detection`
  - `Detection -> Toxicity Detection`
    - `Detection -> Toxicity Detection -> Abuse Detection`
	- `Detection -> Toxicity Detection -> Abuse Detection -> Hate Speech Detection`
	- `Detection -> Toxicity Detection -> Abuse Detection -> Religious Abuse Detection`
	- `Detection -> Toxicity Detection -> Abuse Detection -> Sexism Detection`
	- `Detection -> Toxicity Detection -> Abuse Detection -> Violence Detection`
  - `Detection -> Usage Detection`
- `Dialogue Understanding`
- `Document Understanding`
- `Ethical Judgement`
- `Hallucination`: Given a context, generate imaginary content e.g. given a sentence, generate a story/poem.
- `Hypernym Discovery`
- `Identification`
  - `Identification -> Language Identification`
	- `Identification -> Language Identification -> Verification`
  - `Identification -> Object Identification`: identifying the object of a sentence
  - `Identification -> Predicate Identification`: identifying the predicate of a sentence
  - `Identification -> Subject Identification`: identifying the subject of a sentence
- `Incorrect generation`
- `Mathematics`
  - `Mathematics -> Algebra`
  - `Mathematics -> Arithmetic`
  - `Mathematics -> Combinatorics`
  - `Mathematics -> Counting`: Count an attribute of input e.g. a task to count number of vowels in a given word
  - `Mathematics -> Geometry`
  - `Mathematics -> Statistics`
- `Named Entity Recognition`
- `Parts-of-speech`
- `Proofreading`
  - `Proofreading -> Coherence Detection`
	- `Proofreading -> Coherence Detection -> Sentence Swapping`
    - `Proofreading -> Coherence Detection -> Word Replacement`
  - `Proofreading -> Grammar Error`
    - `Proofreading -> Grammar Error -> Grammar Error Correction`
    - `Proofreading -> Grammar Error -> Grammar Error Detection`
    - `Proofreading -> Grammar Error -> Grammar Error Generation`
  - `Proofreading -> Spelling Error`
    - `Proofreading -> Spelling Error -> Spelling Error Detection`
  - `Proofreading -> Word Order Error`
- `Question Answering`
  - `Question Answering -> Commonsense Question Answering`
  - `Question Answering -> Contextual Question Answering`
    - `Question Answering -> Contextual Question Answering -> Abstractive`
    - `Question Answering -> Contextual Question Answering -> Extractive`
    - `Question Answering -> Contextual Question Answering -> Missing Knowledge` : When the answer to the question is not present in the passage and reqiures extra knowledge.
  - `Question Answering -> Fill in the Blank`
  - `Question Answering -> Incorrect Answer Generation`
    - `Question Answering -> Incorrect Answer Generation -> Commonsense Question Answer Generation`
    - `Question Answering -> Incorrect Answer Generation -> Contextual Question Answer Generation`
      - `Question Answering -> Incorrect Answer Generation -> Contextual Question Answering -> Abstractive`
      - `Question Answering -> Incorrect Answer Generation -> Contextual Question Answering -> Extractive`
    - `Question Answering -> Incorrect Answer Generation -> Multiple Choice Answer Generation`
	- `Question Answering -> Incorrect Answer Generation -> Open Question Answering`
  - `Question Answering -> Multihop Question Answering`
  - `Question Answering -> Multiple Choice Question Answering`
  - `Question Answering -> Numerical Question Answering`
  - `Question Answering -> Open Question Answering`
- `Question Generation`
  - `Question Generation -> Clarifying Question`: Ask clarifying question to get more information
  - `Question Generation -> Contextual Question Generation`: Generate questions based on given context e.g. a task to create a question based on a paragraph.
      - `Question Generation -> Contextual Question Generation -> Generate from an Answer`
      - `Question Generation -> Contextual Question Generation -> Open Question Generation`
  - `Question Generation -> Fill in the Blank` 
  - `Question Generation -> Option Generation`
  - `Question Generation -> Paraphrase Question Generation`: Generate a question as a paraphrase of the original question
  - `Question Generation -> Question Composition`: Compose questions by concating questions in the input
    - `Question Generation -> Question Composition -> Generate from Answers`
  - `Question Generation -> Question Decomposition` 
  - `Question Generation -> Unanswerable Question Generation`
- `Reasoning`
  - `Reasoning -> Abductive Reasoning`
  - `Reasoning -> Analogical Reasoning`
  - `Reasoning -> Argument Reasoning`
  - `Reasoning -> Causal Reasoning`
  - `Reasoning -> Commonsense Reasoning`: Tasks related to activities humans do in daily life e.g. eating breakfast in the morning, sleeping during night etc.
    - `Reasoning -> Commonsense Reasoning -> Numerical Commonsense Reasoning`: Tasks which requires numerical commonsense knowledge e.g. a car has 4 wheels.
    - `Reasoning -> Commonsense Reasoning -> Physical Reasoning`: Tasks involving physical interactions with objects e.g. a knife (and not a paper) is used to cut objects
    - `Reasoning -> Commonsense Reasoning -> Social Situations`
    - `Reasoning -> Commonsense Reasoning -> Spatial Reasoning`
  - `Reasoning -> Counterfactual Reasoning`
  - `Reasoning -> Cross-document Reasoning`
  - `Reasoning -> Deductive Reasoning`
  - `Reasoning -> Discrete Reasoning`
  - `Reasoning -> Ethics`
  - `Reasoning -> Factual Reasoning`
  - `Reasoning -> Grammatical Reasoning`
  - `Reasoning -> Logical Reasoning`
    - `Reasoning -> Logical Reasoning -> Reasoning with Symbols`: Tasks where symbols represent various things e.g. if X is the number of apples in the fridge today morning and Y is the number remaining after I ate a few apples, X-Y is the number of apples I ate.
  - `Reasoning -> Multihop Reasoning`
  - `Reasoning -> Numerical Reasoning`
    - `Reasoning -> Numerical Reasoning -> Numerical Commonsense Reasoning`: Tasks which requires numerical commonsense knowledge e.g. a car has 4 wheels.
  - `Reasoning -> Planning`: Tasks which need some sort of planning e.g. how to go to Hawaii?
  - `Reasoning -> Qualitative Reasoning`
  - `Reasoning -> Quantitative Reasoning`
  - `Reasoning -> Reasoning on Actions`
  - `Reasoning -> Reasoning on Numbers`: When inputs are numbers, e.g. finding the maximum of a list
  - `Reasoning -> Reasoning on Objects`
  - `Reasoning -> Reasoning on Social Interactions`
  - `Reasoning -> Reasoning on Strings`
  - `Reasoning -> Reasoning with Symbols`
  - `Reasoning -> Relational Reasoning`
  - `Reasoning -> Scientific Reasoning`
  - `Reasoning -> Temporal Reasoning`
  - `Reasoning -> Textual Entailment`
    - `Reasoning -> Textual Entailment -> Abductive Reasoning`
    - `Reasoning -> Textual Entailment -> Analogical Reasoning`
    - `Reasoning -> Textual Entailment -> Deductive Reasoning`
    - `Reasoning -> Textual Entailment -> Inductive Reasoning`
- `Role Labelling`
- `Semantic Parsing`
  - `Semantic Parsing -> Program Synthesis`
- `Sentiment Analysis`
  - `Sentiment Analysis -> Entity-based Classification`: Predict the sentiment towards a given entity in the text
  - `Sentiment Analysis -> Entity-based Verification`: Verify whether the predicted sentiment towards a given entity in the text is right or wrong
  - `Sentiment Analysis -> Review Analysis`
  - `Sentiment Analysis -> Sentiment Classification`
- `Story Completion`
- `Structured Text Processing`
  - `Structured Text Processing -> Code Summarization`
  - `Structured Text Processing -> Operation on Primitives`: e.g. An unambiguous transform is applied to all inputs e.g. subtract 1 from every element in the list
	- `Structured Text Processing -> Operation on Primitives -> List`
	  - `Structured Text Processing -> Operation on Primitives -> List -> Numbers`
      - `Structured Text Processing -> Operation on Primitives -> List -> String`
    - `Structured Text Processing -> Operation on Primitives -> Numbers`
      - `Structured Text Processing -> Operation on Primitives -> Numbers -> List`
	  - `Structured Text Processing -> Operation on Primitives -> Numbers -> Scalar`
      - `Structured Text Processing -> Operation on Primitives -> Numbers -> Set`
    - `Structured Text Processing -> Operation on Primitives -> String`
  - `Structured Text Processing -> Semantic Parsing`
    - `Structured Text Processing -> Semantic Parsing -> Program Synthesis`
- `Summarization`
  - `Summarization -> Code Summarization`: Generating natural language description for a piece of code
- `Tabular Text Operation`
  - `Tabular Text Operation -> Column Matching`: Given two sets in the input, generate a mapping between them e.g. given a set of countries and their capitals in the input, generate an output that maps countries to capitals.
  - `Tabular Text Operation -> Question Answering`
- `Text Comparison`
  - `Text Comparison -> Entailment`
  - `Text Comparison -> Relevancy Comparison`
    - `Text Comparison -> Relevancy Comparison -> Irrelevant Selection`
  - `Text Comparison -> Semantic Textual Similarity`
  - `Text Comparison -> Sentiment Comparison`
  - `Text Comparison -> Style Comparison`
- `Text Generation`
  - `Text Generation -> Command Execution`
    - `Text Generation -> Command Execution -> Code Execution`
    - `Text Generation -> Command Execution -> Natural Language Instruction Execution`
  - `Text Generation -> Dialogue Generation`
  - `Text Generation -> Explanation Generation`
  - `Text Generation -> Long Text Generation`
    - `Text Generation -> Long Text Generation -> Contextual Text Generation`
      - `Text Generation -> Long Text Generation -> Contextual Text Generation -> Process Description`
	  - `Text Generation -> Long Text Generation -> Contextual Text Generation -> Story Generation`
		- `Text Generation -> Long Text Generation -> Contextual Text Generation -> Story Generation -> From Scratch`
		- `Text Generation -> Long Text Generation -> Contextual Text Generation -> Story Generation -> Story Completion`
    - `Text Generation -> Long Text Generation -> Paragraph Generation`
    - `Text Generation -> Long Text Generation -> Review Generation`
  - `Text Generation -> Number Generation`
  - `Text Generation -> Order Generation`: Given a set of elements, find their order (e.g. monotonically increasing/decreasing numbers, increasing/decreasing size in case of objects)
    - `Text Generation -> Order Generation -> Arrangement`
  - `Text Generation -> Rhyme Generation`
  - `Text Generation -> Semi-Structured Text Generation`
    - `Text Generation -> Semi-Structured Text Generation -> Named Entity Generation`
  - `Text Generation -> Sentence Generation`
    - `Text Generation -> Sentence Generation -> Code Summarization`: Generating natural language description for a piece of code
    - `Text Generation -> Sentence Generation -> Completion`
      - `Text Generation -> Sentence Generation -> Completion -> Story`
    - `Text Generation -> Sentence Generation -> Contextual Text Generation`
      - `Text Generation -> Sentence Generation -> Contextual Text Generation -> Coherent Text Generation`
    - `Text Generation -> Sentence Generation -> Explanation Generation`
    - `Text Generation -> Sentence Generation -> Summary Generation`
  - `Text Generation -> Structured Text Generation`: Generate structured text in the output e.g. a task that converts questions in natural language to SQL queries
      - `Text Generation -> Structured Text Generation -> Code`
      - `Text Generation -> Structured Text Generation -> List`
      - `Text Generation -> Structured Text Generation -> Table`
  - `Text Generation -> Summary Generation`
  - `Text Generation -> Title Generation`
  - `Text Generation -> Topic Generation`
  - `Text Generation -> Word Generation`
    - `Text Generation -> Word Generation -> Abbrevation Generation`
    - `Text Generation -> Word Generation -> Preposition Generation`
    - `Text Generation -> Word Generation -> Transition Word Generation`
- `Text Modification`
  - `Text Modification -> Paraphrasing`
  - `Text Modification -> Perturbation`
  - `Text Modification -> Structured Text Modification`
  - `Text Modification -> Style Transfer`
    - `Text Modification -> Style Transfer -> Text Simplification`
  - `Text Modification -> Text Simplification`
- `Text Span Selection`
- `Title Selection`
- `Unnatural Language Processing`
  - `Unnatural Language Processing -> Question Answering`  
- `Word Sense Disambiguation`

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
