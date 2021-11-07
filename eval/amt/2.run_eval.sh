# launch the experiment
export AWS_PROFILE=alexandria-mturk
amti --verbose create-batch mturk-specs/definition-likert start=850_end=1200_max_size=5.jsonl . --live

# check the experiment status
export BATCH=batch-...
#export BATCH=batch-4ee23f3d-2900-4fef-a0ae-d05bc7d519e8_start=850_end=1200_max_size=5
amti status-batch "$BATCH" --live

# fetch the results when they're over
amti review-batch "$BATCH" --approve-all --live
amti save-batch "$BATCH" --live
amti extract tabular "$BATCH" "${BATCH}/batch-results.jsonl"
