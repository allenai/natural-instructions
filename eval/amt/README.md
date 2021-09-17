# Human Evaluation of Instructions 
 - Step1: Select a task and convert it into AMTI-friendly format:  
```terminal
> python 1.amti_create_input_data.py --file [NAME] --eval_count [COUNT]
```
For example: 
```terminal
> python 1.amti_create_input_data.py --file  task156_codah_classification_adversarial.json --eval_count 10
```
 - Step2: follow the steps in `2.run_eval.sh`
 - Step3: evaluate
