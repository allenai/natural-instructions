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


To disqualify a certain user, add them to `genie_disqualification/blocklist.txt` and then:

    amti associate-qual  --file genie_disqualification/blocklist.txt --qual  3090SA10WM5MIHCWNTON1VROMP4CN3 --live 

Or disqualify a particular user: 

    amti associate-qual  WorkerId --qual   3090SA10WM5MIHCWNTON1VROMP4CN3   --live

To list workers that are disqualified:

    amti  associated --qual  3090SA10WM5MIHCWNTON1VROMP4CN3 --status Granted  --live 
