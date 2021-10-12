# launch the experiment
export AWS_PROFILE=alexandria-mturk
amti --verbose create-batch mturk-specs/definition-likert file_name.jsonl . --live
# for example,
# amti --verbose create-batch mturk-specs/definition-likert start=1_end=2_max_size=2.jsonl .

# check the experiment status
export BATCH=batch-...
amti status-batch "$BATCH" --live

# fetch the results when they're over
amti review-batch "$BATCH" --approve-all --live
amti save-batch "$BATCH" --live
amti extract tabular "$BATCH" "${BATCH}/batch-results.jsonl"
