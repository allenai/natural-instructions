# Task Hierarchy

## Guidelines / FAQs for Contributors:

- Massaging the task hierarchy categories is somewhat encouraged.
- If a subcategory (e.g. `Question Answering -> Contextual Question Answering -> Extractive`) is mentioned, don't mention its parent category (`Question Answering -> Contextual Question Answering`)
- `src/auto_add_domain.py` is helpful for adding domains for all tasks in any particular dataset
## Task Categories
- `Abuse Detection`
- `Question Answering`
  - `Question Answering -> Commonsense Question Answering`
  - `Question Answering -> Contextual Question Answering`
    - `Question Answering -> Contextual Question Answering -> Extractive`
    - `Question Answering -> Contextual Question Answering -> Abstractive` 
  - `Question Answering -> Fill in the Blank`
  - `Question Answering -> Multiple Choice Question Answering`
  - `Question Answering -> Open Question Answering`
  - `Question Answering -> Incorrect Answer Generation`
	- `Question Answering -> Incorrect Answer Generation -> Multiple Choice Incorrect Answer Generation`
	- `Question Answering -> Incorrect Answer Generation -> Comprehensive Incorrect Answer Generation`
- `Question Generation`
  - `Question Generation -> Contextual Question Generation`: Generate questions based on given context e.g. a task to create a question based on a paragraph.
  - `Question Generation -> Question Composition`: Compose questions by concating questions in the input
  - `Question Generation -> Fill in the Blank` 
- `Author Identification`
- `Classification`
  - `Classification -> Verification`: Verify whether a given descriptive attribute applies to a given text or not (binary output) e.g. if the paragraph contains offensive content or not
    - `Classification -> Verification -> Claim Verification`
    - `Classification -> Verification -> Sufficient Information Verification`: Verify whether a text contains sufficient information to answer a question
    - `Classification -> Verification -> Grammar Verification`: Verify whether a text is grammatical 
    - `Classification -> Verification -> Relevance Verification`
    - `Classification -> Verification -> Answer Verification`: Verify whether a text answers the question
- `Combinatorics`
- `Command Execution`
- `Coreference`
  - `Coreference -> Entity Coreference`
  - `Coreference -> Pronoun Disambiguation`
- `Counting`: Count an attribute of input e.g. a task to count number of vowels in a given word
- `Dialogue Understanding`
- `Document Understanding`
- `Entity Detection`
- `Ethical Judgement`
- `Fake News Detection`
- `Grammar Error`
  -  `Grammar Error -> Grammar Error Correction`
  -  `Grammar Error -> Grammar Error Detection`
- `Hallucination`: Given a context, generate imaginary content e.g. given a sentence, generate a story/poem.
- `Hate Speech Detection`
- `Hypernym Discovery`
- `Intent Detection`
- `Language Identification`
- `Mathematics`
  - `Mathematics -> Algebra`
  - `Mathematics -> Arithmetic`
  - `Mathematics -> Geometry`
- `Named Entity Recognition`
- `Order Generation`: Given a set of elements, find their order (e.g. monotonically increasing/decreasing numbers, increasing/decreasing size in case of objects)
- `Paraphrasing`
- `Parts-of-speech`
- `Question Decomposition`
- `Reasoning`
  - `Reasoning -> Abductive Reasoning`
  - `Reasoning -> Analogical Reasoning`
  - `Reasoning -> Causal Reasoning`
  - `Reasoning -> Commonsense Reasoning`: Tasks related to activities humans do in daily life e.g. eating breakfast in the morning, sleeping during night etc.
  - `Reasoning -> Deductive Reasoning`
  - `Reasoning -> Logical Reasoning`
  - `Reasoning -> Multihop Reasoning`
  - `Reasoning -> Numerical Commonsense Reasoning`: Tasks which requires numerical commonsense knowledge e.g. a car has 4 wheels.
  - `Reasoning -> Numerical Reasoning`
  - `Reasoning -> Physical Reasoning`: Tasks involving physical interactions with objects e.g. a knife (and not a paper) is used to cut objects
  - `Reasoning -> Planning`: Tasks which need some sort of planning e.g. how to go to Hawaii?
  - `Reasoning -> Qualitative Reasoning`
  - `Reasoning -> Reasoning on Actions`
  - `Reasoning -> Reasoning on Social Interactions`
  - `Reasoning -> Reasoning with Symbols`: Tasks where symbols represent various things e.g. if X is the number of apples in the freeze today morning and Y is the number remaining after I ate a few apples, X-Y is the number of apples I ate.
  - `Reasoning -> Spatial Reasoning`
  - `Reasoning -> Temporal Reasoning`
- `Relation Prediction`
- `Relevancy Estimation`
- `Role Labelling`
- `Semantic Parsing`
- `Sentiment Analysis`
- `Sorting`
- `Stance Detection`
- `Structured Text Generation`: Generate structured text in the output e.g. a task that converts questions in natural language to SQL queries
- `Style Transfer`
- `Summarization`
- `Tabular Text Operation`
  - `Tabular Text Operation -> Column Matching`: Given two sets in the input, generate a mapping between them e.g. given a set of countries and their capitals in the input, generate an output that maps countries to capitals.
  - `Tabular Text Operation -> Question Answering`
- `Text Comparison`
- `Text Generation`
	- `Text Generation -> Explanation Generation`
	- `Text Generation -> Paragraph Generation`
	- `Text Generation -> Review Generation`
	- `Text Generation -> Sentence Generation`
	- `Text Generation -> Story Ending Generation`
	- `Text Generation -> Title Generation`
	- `Text Generation -> Topic Generation`
- `Text Modification`
- `Text Simplification`
- `Text Span Selection`
- `Textual Entailment`
- `Translation`
- `Weblink Generation`
- `Word Sense Disambiguation`
- `Wrong Order Detection`

## Domain
* `Accounting`
* `Anthropology`
* `Architecture`
* `Art`
* `Astronomy`
* `Biology`
  * `Biology -> Anatomy`
  * `Biology -> Clinical Knowledge`
  * `Biology -> Human Biology`
  * `Biology -> Virology`
* `Business Ethics`
* `Chemistry`
* `Computer Science`
* `Computer Science -> Machine Learning`
* `Computer Security`
* `Debatepedia`
* `Dialogue`
* `Econometrics`
* `Electrical Engineering`
* `English`
* `Fiction`
* `Formal Fallacy`
* `Formal logic`
* `Geography`
* `Global Facts`
* `Government and Politics`
* `Pop Culture`
* `History`
  * `History -> European History`
  * `History -> 9/11 Reports`
* `Human Sexuality`
* `International Law`
* `Jurisprudence`
* `Justice`
* `Law`
* `Logic`
* `Macroeconomics`
* `Management`
* `Marketing`
* `Mathematics`
* `Medical Genetics`
* `Medicine`
* `Microeconomics`
* `Moral Scenarios`
* `Movies`
* `Music`
* `Narrative`
* `News`
* `Nutrition`
* `Personal Narratives`
* `Philosophy`
* `Physics`
* `Prehistory`
* `Psychology`
* `Public Relations`
* `Qualitative Relations`
* `School Science Textbooks`
* `Natural Science`
* `Security: Environmental Security`
* `Security: National Security`
* `Social Media`
* `Sociology`
* `Sports`
  * `Sports -> NFL`
* `Statistics`
* `Stack Overflow`
* `Story`
* `US Foreign Policy`
* `Wikipedia`
* `World Religions`
* `Commonsense`
  * `Commonsense -> Social Commonsense`: a situation involving two same gender people
with contrasting attributes, emotions, social roles, etc.
  * `Commonsense -> Physical Commonsense`: a context involving two physical
objects with contrasting properties, usage, locations, etc.

## Language
- https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes: ISO language name column
