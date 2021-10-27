# launch the experiment
export AWS_PROFILE=alexandria-mturk
amti --verbose create-batch mturk-specs/definition-likert start=301_end=400_max_size=5.jsonl . --live

# check the experiment status
export BATCH=batch-...
#export BATCH=batch-fc02d066-1e35-4184-b4ea-ba7eca1abcc1_start=301_end=400_max_size=5
amti status-batch "$BATCH" --live

# fetch the results when they're over
amti review-batch "$BATCH" --approve-all --live
amti save-batch "$BATCH" --live
amti extract tabular "$BATCH" "${BATCH}/batch-results.jsonl"
