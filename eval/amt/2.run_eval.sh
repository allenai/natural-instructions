# launch the experiment
export AWS_PROFILE=alexandria-mturk
amti --verbose create-batch mturk-specs/definition-likert start=400_end=600_max_size=5.jsonl . --live

# check the experiment status
export BATCH=batch-...
#export BATCH=batch-4739062e-2141-4f97-9a37-41197abf9a93_start=400_end=600_max_size=5
amti status-batch "$BATCH" --live

# fetch the results when they're over
amti review-batch "$BATCH" --approve-all --live
amti save-batch "$BATCH" --live
amti extract tabular "$BATCH" "${BATCH}/batch-results.jsonl"
