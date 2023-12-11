# Pseudo-Code Instructions
This repository contains the code and dataset for the paper [Prompting with Pseudo-Code Instructions](https://arxiv.org/abs/2305.11790).

Authors:
- Mayank Mishra
- Prince Kumar
- Riyaz Bhat
- Rudra Murthy V
- Danish Contractor
- Srikanth Tamilselvam

The dataset consists of human-created instructions in pseudo-code for various tasks provided in the original [Super-Natural Instructions](https://github.com/allenai/natural-instructions) dataset. Our instructions are present in [instructions/](instructions/) folder.

## Usage
```python
from code_instruct import CodeInstructionsDataset, ExampleType
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-3b")

# load dataset
dataset = CodeInstructionsDataset("all", num_shots=2, multilingual=False)

# datapoint is a class which can be converted into any of the supported ExampleType defined in code_instruct/data.py
# Supported ExampleType (s) are:
# CODE_INSTRUCTIONS
# CODE_INSTRUCTIONS_WITHOUT_DOCSTRING
# FUNCTION_DEFINITION
# NATURAL_INSTRUCTIONS
# NATURAL_INSTRUCTIONS_WITH_DOCSTRING
# NO_INSTRUCTION_CODE_EXAMPLES
# NO_INSTRUCTION_NATURAL_EXAMPLES
# NO_INSTRUCTION_GENERIC_FUNCTION_CALL
for datapoint in dataset:
    example = datapoint.get_example(ExampleType.CODE_INSTRUCTIONS, eos_token=tokenizer.eos_token)
    input, gt_outputs = example

    print(input)
    print(gt_outputs)
```

Note: For the paper, we use [code_isntruct/inference.py](code_isntruct/inference.py) which runs inference on the task examples given in [ids/sample_ids-1000.txt](ids/sample_ids-1000.txt). You can launch this using the following command:
```bash
make inference model_name=bigscience/bloom-3b model_class=AutoModelForCausalLM example_type=code_instructions num_shots=2 output_file=output.jsonl sample_ids_file=ids/sample_ids-1000.txt
```

## Contributing

To contribute tasks to this dataset, please read the following guidelines:

```python
def count_noun_verbs(sentence: str, pos_tag: str) -> int:
    """
    Count the number of nouns/verbs in the given sentence
    If the instruction is to count the number of nouns then return the number of nouns in the sentence
    If the instruction is to count the number of verbs then return the number of verbs in the sentence
    Ignore the instruction part while counting for frequency

    Parameters:
        sentence (str): An English Sentence
        pos_tag (str): the target POS category, either nouns or verbs

    Returns:
        int: Count of nouns or verbs
    """

    return count_of_pos_tags(sentence, pos_tag)


# program
{
    "method": "count_noun_verbs",
    "arguments": {"sentence": "str", "pos_tag": "str"},
    "return": "int",
    "execute": "count_noun_verbs(sentence, pos_tag)",
}

# preprocessor
def preprocess(input: str):
    sentence = input.split("Sentence: '")[1].split("'. Count")[0]
    pos_tag = input.split("Count the number of ")[1].split(" in this sentence.")[0]
    return sentence, pos_tag

```


1. The pseudocode should look mostly like python.
2. The functions should be strongly typed. If the function doesn't return anything, type = `None`. If the return type can be anything depending on what happens inside, type = `Any`. Please be careful with lowercase/uppercase.
3. Try to keep a blank line between functions.
4. Avoid declaring global variables whenever possible and pass them as arguments to a method.
5. Avoid using classes, enums etc if possible. Keep the instructions as functions as much as possible. For some tasks, this might not be possible and in such cases you can uses classes/enums sparingly.
6. Create a python file for the task with task number as the file-name
7. Please specify the comment `program` on how to execute the method. This template will be used to create 0-shot or potentially few-shot examples. There should be a singular point of entry (function) for the pseudo-code program.
8. Note, not all functions require definition. If the task is `non-atomic`, you can assume availability of basic functions and don't need to define stuff like `concat_str`, `search` etc and can simply call these funcations.
9. All function names should be descriptive. For example, in the following we prefer the first function name as opposed to the second. But keep in mind that the functions name are not too long.
```python
generate_event_duration_question_from_sentence(event, sentence)
generate_question(event, sentence)
```
10. All variables should be descriptive. For example, the first one is a better variable name in the following:
```python
duration_question = generate_event_duration_question_from_sentence(event, sentence)
question = generate_event_duration_question_from_sentence(event, sentence)
```
11. Each line of code (that is not starightforward) should have an associated comment explaining why the next line of code has been written. 
12. Programming shorthand/python tricks should not be used and each step should be as atomic as possible. For example, the use of yield/generator functionality in python, relying on intristic behavior of global/local variables, extracting multiple different lists, tuples all at once.
13. Each function should be accompanied by a descriptive docstring that explains the goal of the function as well as defines the `Parameters` and the value returned preferably with type information.
14. Secondary sub-task function should only be defined if the descriptive function name may require some additional details to be specified.
15. A preprocessor to parse the input is needed. This should be python code that works and not pseudocode. This should be a function with the name `preprocess` that takes a single input string. This function will be called on each example in the dataset for that task.
16. Once you are done and satisfied with your annotations, open a PR against this repo.

## License 
All the data here (except the instances of each task) are released under Apache-2.0 license. 
The instances of each tasks are subject to the license under which the original dataset was released. 
These license information are available unders "Instance License" field within each task file. 


## Citation

```bibtex
@inproceedings{mishra-etal-2023-prompting,
    title = "Prompting with Pseudo-Code Instructions",
    author = "Mishra, Mayank  and
      Kumar, Prince  and
      Bhat, Riyaz  and
      Murthy, Rudra  and
      Contractor, Danish  and
      Tamilselvam, Srikanth",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.939",
    pages = "15178--15197",
    abstract = "Prompting with natural language instructions has recently emerged as a popular method of harnessing the capabilities of large language models (LLM). Given the inherent ambiguity present in natural language, it is intuitive to consider the possible advantages of prompting with less ambiguous prompt styles, like pseudo-code. In this paper, we explore if prompting via pseudo-code instructions helps improve the performance of pre-trained language models. We manually create a dataset of pseudo-code prompts for 132 different tasks spanning classification, QA, and generative language tasks, sourced from the Super-NaturalInstructions dataset. Using these prompts along with their counterparts in natural language, we study their performance on two LLM families - BLOOM, CodeGen. Our experiments show that using pseudo-code instructions leads to better results, with an average increase (absolute) of 7-16 points in F1 scores for classification tasks and an improvement (relative) of 12-38{\%} in aggregate ROUGE-L scores across all tasks. We include detailed ablation studies which indicate that code comments, docstrings, and the structural clues encoded in pseudo-code all contribute towards the improvement in performance. To the best of our knowledge, our work is the first to demonstrate how pseudo-code prompts can be helpful in improving the performance of pre-trained LMs.",
}
```
