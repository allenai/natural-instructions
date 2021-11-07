# launch the experiment
export AWS_PROFILE=alexandria-mturk
amti --verbose create-batch mturk-specs/definition-likert start=600_end=850_max_size=5.jsonl . --live

# check the experiment status
export BATCH=batch-...
#export BATCH=batch-23353cc5-13c1-4af9-94c3-03eb2bacbd0a_start=600_end=850_max_size=5
amti status-batch "$BATCH" --live

# fetch the results when they're over
amti review-batch "$BATCH" --approve-all --live
amti save-batch "$BATCH" --live
amti extract tabular "$BATCH" "${BATCH}/batch-results.jsonl"
