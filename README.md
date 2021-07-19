# A Repository of Community-Driven Natural Instructions 

**TLDR;** this repository maintains a community effort to create a large collection of tasks and their natural language definitions/instructions. 
We're looking for more contributions to make this data bigger! 🙌 
We invite submission of new tasks to this benchmark by way of [GitHub pull request](https://github.com/allenai/natural-instructions-expansion/pulls), through **September 15, 2021**.
The contributors with meaningful contribution to our tasks will be included as co-authors on a paper that will announce the benchmark as well as analysis/results on it. 

## Background 
### Why define tasks in natural language?
While the current dominant paradigm (supervised learning with labeled examples) has been successful in building task-specific models. 
Such models can't generalize to unseen tasks; for example, a model that is supervised to solve questions cannot solve a classification task. 
We hypothesize that a model equipped with understanding and reasoning with natural language instructions should be able to generalize to any task that can be defined in terms of natural language.

### Any empirical evidence that this might be true?
In our [earlier effort](https://arxiv.org/abs/2104.08773), we built a smaller data (61 tasks) and 
observed that language models benefit from language instructions, i.e., their generalization to unseen tasks when they were provided with more instructions.  
Also, generalization to unseen tasks improves as the model is trained on more tasks.

### Why build this dataset?  
We believe that [our earlier work](https://arxiv.org/abs/2104.08773) is just scratching the surface and there is probably so much that be studied in this setup.
We hope to put together a much larger dataset that cover a wider range of reasoning abilities. 
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
    * Make sure that your json is human readable (use proper indentation; e.g., in Python: `json.dumps(your_json_string, indent=4)`)   
    * Make sure that you json file is not bigger than 50MB. 
    * Make sure your task has no more 6.5k instances (input/output pairs).
    * Make sure to number your task json correctly (Look at the task number in the latest pull request, task number in your submission should be the next number).
    * Make sure to create a pull request after creating all possible tasks from a dataset. You should have one pull request per dataset.
    * If you're building your tasks based existing datasets and their crowdsourcing templates, see these [guidelines](doc/crowdsourcing.md). 
 * Add your task to [our list of tasks](tasks/README.md).
 * To make sure that your addition is formatted correctly, run the tests: `> python src/test_all.py`
  
 
If you have any questions or suggestions, please use [the issues](https://github.com/allenai/natural-instructions-expansion/issues) feature.  


## Frequently Asked Questions
### Can I submit non-English tasks?
Yes! We welcome submission from any of the languages. 

### Can I create tasks without using crowdsourcing templates?
Yes! just make sure that the quality of instructions is good enough for a human to understand the task just based on instructions. You can take a different route than the [guidelines](doc/crowdsourcing.md).

### What is the minimun number of instances I can have in my task? 

Anything north of 100 is a safe number. The more, the merrier! Also, you should not have more than 6500 instances.

### What do you mean by "meaningful contribution"? 
If you're among top `k` [contributors](https://github.com/allenai/natural-instructions-expansion/graphs/contributors) (say, `k=25`), or if you have contributed at least `l` tasks (say, `l=10`). Depending on the overall contributions, we will adjust these constants so that the number of authors don't exeed `m` (say, `m=35`). 
 
### My commits are not tied to my Github profie; Github does not show all my contributions. 

Make sure that your email is set in your git environment and it is also mentioned in your github profile. See [this](https://stackoverflow.com/questions/26004587/git-commits-are-not-getting-linked-with-my-github-account) and [this](https://docs.github.com/en/github/committing-changes-to-your-project/troubleshooting-commits/why-are-my-commits-linked-to-the-wrong-user). 
 
