# launch the experiment
export AWS_PROFILE=alexandria-mturk
amti --verbose create-batch mturk-specs/definition-likert start=1200_end=1536_max_size=5.jsonl . --live

# check the experiment status
export BATCH=batch-...
#export BATCH=batch-13abedb3-9788-4118-8a23-89978a941638_start=1540_end=1800_max_size=5
amti status-batch "$BATCH" --live

# fetch the results when they're over
amti review-batch "$BATCH" --approve-all --live
amti save-batch "$BATCH" --live
amti extract tabular "$BATCH" "${BATCH}/batch-results.jsonl"
