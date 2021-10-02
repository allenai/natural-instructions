# A Community-Driven Repository of Natural Language Instructions 

**TLDR;** this repository maintains a community effort to create a large collection of tasks and their natural language definitions/instructions. 
We're looking for more contributions to make this data bigger! 🙌 
We invite submission of new tasks to this benchmark by way of [GitHub pull request](https://github.com/allenai/natural-instructions-expansion/pulls), through **October 15, 2021**.
The contributors with [meaningful contributions](https://github.com/allenai/natural-instructions-expansion/#what-do-you-mean-by-meaningful-contribution) to our tasks will be included as co-authors on a paper that will announce the benchmark as well as analysis/results on it. 


## Background 
### Why define tasks in natural language?
While the current dominant paradigm (supervised learning with task-specific labeled examples) has been successful in building task-specific models, such models can't generalize to unseen tasks; for example, a model that is supervised to solve questions cannot solve a classification task. 
We hypothesize that a model equipped with understanding and reasoning with natural language instructions should be able to generalize to any task that can be defined in terms of natural language.

### Any empirical evidence that this might be true?
In our [earlier effort](https://arxiv.org/abs/2104.08773), we built a smaller data (61 tasks) and 
observed that language models benefit from language instructions, i.e., their generalization to unseen tasks when they were provided with more instructions.  
Also, generalization to unseen tasks improves as the model is trained on more tasks.

### Why build this dataset?  
We believe that [our earlier work](https://arxiv.org/abs/2104.08773) is just scratching the surface and there is probably so much that be studied in this setup.
We hope to put together a much larger dataset that covers a wider range of reasoning abilities. 
We believe that this expanded dataset will serve as a useful playground for the community to study and build the next generation of AI/NLP models.


## Task definitions 
Each consists of input/output. For example, think of the task of sentiment classification:  
 - **Input:** `I thought the Spiderman animation was good, but the movie disappointed me.`
 - **Output:** `Mixed` 

Here is another example from the same task: 
 - **Input:** `The pumpkin was one of the worst that I've had in my life.` 
 - **Output:**  `Negative`  

Additionally, each ask contains a task *definition*: 
```
Given a tweet, classify it into one of 4 categories: Positive, Negative, Neutral, or Mixed.
``` 

Overall, each tasks follows this schema:
 
![](doc/schema-simplified.svg ) 

Or if you're comfortable with json files, here is how it would look like: 
```json 
{
  "Contributors": [""],
  "Source": [""],
  "Categories": [""],
  "Definition": "",
  "Positive Examples": [ { "input": "", "output": "",  "explanation": ""} ], 
  "Negative Examples": [ { "input": "", "output": "",  "explanation": ""} ],
  "Instances": [ { "input": "", "output": [""]} ],
}
```

## How to contribute 
We would appreciate any external contributions! 🙏

 * All submissions must be submitted via [Github pull requests](https://github.com/allenai/natural-instructions-expansion/pulls). These submissions will undergo a review before being merged. 
 * Each task must contain contain a `.json` file that contains the task content. You can look inside the [`tasks/`](tasks) directory for several examples.  
    * Make sure that your json is human readable (use proper indentation; e.g., in Python: `json.dumps(your_json_string, indent=4, ensure_ascii=False)`)   
    * Make sure that you json file is not bigger than 50MB. 
    * Make sure your task has no more 6.5k instances (input/output pairs).
    * Make sure to number your task json correctly (Look at the task number in the latest pull request, task number in your submission should be the next number). Make sure to include the source dataset name and the task category name while creating the json file name. You can use this format: taskabc_<source dataset>_<task category>.json E.g. in task001_quoref_question_generation.json, the source dataset is 'quoref' and the task category is 'question generation. Note that, source need not necessarily be a dataset and can be a website e.g. leetcode. Finally, if you have created the json without any reference, use 'synthetic' in place of source.
    * Make sure to create a pull request after creating all possible tasks from a dataset. You should have one pull request per dataset. Name your pull request as Task <start_task_number>-<end_task_number>: <Task Summary> e.g. Task 101-107: SQuAD Dataset.
    * If you're building your tasks based existing datasets and their crowdsourcing templates, see these [guidelines](doc/crowdsourcing.md). 
 * Add your task to [our list of tasks](tasks/README.md).
 * To make sure that your addition is formatted correctly, run the tests: `> python src/test_all.py`
  
## Summary of Diversity in the Accepted Tasks:
Task Type:
* Contextual Question Generation
* Answer Generation: Reading Comprehension
* Answer Generation: Contextual Question Answering
* Answer Generation: Open book/Domain-specific Question Answering
* Answer Generation: Commonsense Question Answering
* Answer Generation: Fill in the Blank
* Natural Language Inference
* Incorrect Answer Generation
* Sentence Generation
* Text Modification
* Classification
* Long Text Generation
* Verification
* Translation
* Multiple Choice Question Answering
* Structured Text Generation
* Arithmetic
* Algebra
* Mathematics
* Question Decomposition
* Counting
* Entity Detection
* Role Labelling
* Combinatorics
* Grammar Correction
* Summarization
* Sentiment Analysis
* Hate Speech Detection
* Logic
* Fake News Detection
* Explanation Generation
* Ethical Judgement
* Style Transfer
* Text Comparison
* Geometry
* Question Composition
* Review Generation
* Column Matching
* Handling Commands
* Author Identification
* Order Generation
* Language Identification
* Prompt Generation
* Text Span Selection
* Hallucination
* Title Generation
* Document Classification
* Relevancy Estimation
* NER
* Program Synthesis
* Dialogue Prediction
* Abuse Detection
* Weblink Generation
* Text Simplification
* Reasoning: Numerical Reasoning
* Reasoning: Entity Coreference
* Reasoning: Reasoning on Actions
* Reasoning: General Commonsense Reasoning
* Reasoning: Abductive Reasoning
* Reasoning: Pronoun Disambiguation
* Reasoning: Temporal Reasoning
* Reasoning: Multihop Reasoning
* Reasoning: Reasoning on Social Interactions
* Reasoning: Contextual Commonsense Reasoning
* Reasoning: Numerical Commonsense Reasoning
* Reasoning: Physical Reasoning
* Reasoning: Logical Reasoning
* Reasoning: Planning
* Reasoning: Qualitative Reasoning
* Reasoning: Deductive Reasoning
* Reasoning: Causal Reasoning
* Reasoning: Inverse-Causal Reasoning
* Reasoning: Reasoning with Symbols

Language
* English
* Hindi
* Gujarati
* Spanish
* Farsi
* Italian
* Japanese
* Polish
* Oriya
* Bengali
* Malayalam
* Persian
* Kannada
* Arabic
* Finnish
* Turkish
* Chinese
* German
* Bulgarian
* Swedish
* Vietnamese
* Thai
* Burmese
* Malay
* Laotian
* Khmer
* Bahasa
* Filipino
* French
* Somali
* Tagalog
* Igbo
* Korean
* Marathi
* Punjabi
* Telugu
* Tamil

Domain:
* Movies
* Art
* Architecture
* Geography
* History 
* Music
* News
* Society 
* Law
* Justice 
* Anthropology
* 9/11 reports
* School science textbooks
* Fiction
* Personal narratives
* National Football League (NFL) game summaries
* Abstract algebra
* Anatomy
* Astronomy
* Business ethics
* Clinical knowledge
* College biology
* College chemistry
* College computer science
* College mathematics
* College medicine
* College physics
* Computer security
* Conceptual physics
* Econometrics
* Electrical engineering
* Elementary mathematics
* Formal logic
* Global facts
* High school biology
* High school chemistry
* High school computer science
* High school european history
* High school geography
* High school government and politics
* High school macroeconomics
* High school mathematics
* High school microeconomics
* High school physics
* High school psychology
* High school statistics
* High school us history
* High school world history
* Human aging
* Human sexuality
* International law
* jurisprudence
* Logical fallacies
* Machine learning
* Management
* Marketing
* Medical genetics
* Miscellaneous
* Moral disputes
* Moral scenarios
* Nutrition
* Philosophy
* Prehistory
* Accounting
* Law
* Medicine
* Psychology
* Public relations
* Security  studies
* Sociology
* Us foreign policy
* Virology
* World religions
* Social Media

 
If you have any questions or suggestions, please use [the issues](https://github.com/allenai/natural-instructions-expansion/issues) feature.  


## Frequently Asked Questions
### I want to contribute but I am not sure what tasks I can contribute. 
There are also a bunch of task suggestions in [the Github issues](https://github.com/allenai/natural-instructions-expansion/issues?q=is%3Aissue+is%3Aopen+label%3Atask-suggestion) which you can sign up to work on. If you have any other suggested tasks but you're not sure if they're good fit, bring them up in the [issues](https://github.com/allenai/natural-instructions-expansion/issues).  

 ### I have suggestion to improve your benchmark. Where can I discuss it? 
We would love to hear your suggestions! Please bring it up as an [issue](https://github.com/allenai/natural-instructions-expansion/issues) and let's discuss it. 

### What do you mean by "meaningful contribution"? 
If you have contributed at least 25 tasks to the repository or if you're among top 20 [contributors](https://github.com/allenai/natural-instructions-expansion/graphs/contributors), we view that as meaningful contribution. This also involves some lightweight responsibilities such as reviewing pull requests.
 
### Can I create tasks without using crowdsourcing templates?
Yes! just make sure that the quality of instructions is good enough for a human to understand the task just based on instructions. You can take a different route than the [guidelines](doc/crowdsourcing.md).

### What is the minimum number of instances I can have in my task? 

Anything north of 100 is a safe number. The more, the merrier! Also, you should not have more than 6500 instances. Make sure to shuffle instances before selecting 6500 of those. In case of classifcation tasks, make sure that the instances and positive examples are not skewed towards a class.
 
### Can I submit non-English tasks?
Yes! We welcome submission from any of the languages. 
 
### My commits are not tied to my Github profie; Github does not show all my contributions. 

Make sure that your email is set in your git environment and it is also mentioned in your github profile. See [this](https://stackoverflow.com/questions/26004587/git-commits-are-not-getting-linked-with-my-github-account) and [this](https://docs.github.com/en/github/committing-changes-to-your-project/troubleshooting-commits/why-are-my-commits-linked-to-the-wrong-user). 
 
