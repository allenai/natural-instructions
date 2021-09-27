# Converting Crowdsourcing Instructions to Our Format 

Generally, this process consists of the following steps: 

### Step 1: Identify a dataset and engage with their authors
Consider a task that involves high-level language instructions. 
These could be the instructions used for crowdsourcing a dataset or otherwise.
If you decide to use crowdsourcing instructions, you can [email authors of existing datasets](emailing-authors.md) and ask for their templates. 
There are also a bunch of task suggestions in [the Github issues](https://github.com/allenai/natural-instructions-expansion/issues?q=is%3Aissue+is%3Aopen+label%3Atask-suggestion) which you can sign up to work on.


### Step 2: Go through the template and understand the task 
Create few data samples, annotate them and see if your outputs match instructions in the template and gold annotations.
Obviously, if you're the task author, this should be quite easy for you. 

### Step 3: Split the template into sub-tasks 
If the task involves multiple annotation steps, split them into several subtasks.
Almost all the crowdworking instructions include sequences of steps to guide crowdworkers to collect task instances.
For example, QASC and MCTACO include 7 and 19 steps in the data creation process, respectively. 
Dividing crowdsourcing instructions into their underlying steps would result in multiple subtasks that are minimal and standalone.  
We have some examples of these tasks in [this work](https://arxiv.org/abs/2104.08773).
This can be a non-trivial process. So, if you have any question on to this, feel free to discuss them in the issues. 

 - **Note** Let's skip any of the tasks that involve on-the-fly processing (e.g., model responses, retrieval responses).

### Step 4: Manually fill fields in schema with content from the template:
For doing this, you can create a empty json file based on the example provided in [the main readme](../README.md#task-definitions) 
and start filling out different fields.
In addition to the default schema, make sure to add the following fields too: 
 - `Contributor`: your name 
 - `Categories`: general semantic categories of the tasks. You can see some example catregories in [the task list](../tasks/README.md). 

### Step 5: Iterate over the instructions 
Iterate over the instructions to ensure their clarity while eliminating the repeated content. Fix writing and annotation issues in examples, also typos etc. 
Retain only the minimum content. Remember, maximum input token size to language models is limited.
Often, examples in the template may not have correct annotation, check and fix those.

### Step 6: Create negative examples if not present. Add the missing explanations to the examples.
Look at negative examples in [our earlier construction](https://instructions.apps.allenai.org/explore) to get a good idea of how they look like.
These examples typically define the boundaries of the task by showing undesirable examples.
Note that, all examples contain an ‘explanation’ that define the reason why an example fits the bill (for positive examples) or why it fails to meet the requirements (for negative examples).

### Step 7: Programmatically extract the input/output instances from raw crowdsourcing annotations.
Check if input output pairs associated with this task are present in the source dataset. 
If yes, this will save a lot of time. Else, extract those from the annotation csv files (the output of crowdsourcing). 
 - Remove repeated data instances. 
 - Keep the instances with high inter-annotator agreement.
 - Retain only 6500 samples, make sure to shuffle before selecting samples. Also ensure that samples corresponding to all labels are present in the selected dataset.
 - Verify a few samples to ensure that gold annotations and inputs match.

### Step 8: Double-check your generated json file 
Make sure that all the content is there. 
And make sure that your json file in [human readable](../README.md#how-to-contribute).    

### Step 8: Create a Pull Request for your task. 
If you don't know how this is done, [here](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) is a good summary.
The quick gist is that: 
 - Fork this repository. 
 - Clone the forked repository on your computer. 
 - Add your task to the cloned repo and push it to a branch on your **forked** repo. 
 - Open a pull request that refers to the branch that contains your task. 
 - Then wait for our review! :) 
