test:
	black instructions
	python -m code_instruct.test

get-ids:
	python -m code_instruct.get_ids --output_file $(output_file)

sample-ids:
	python -m code_instruct.sample_ids --all_ids_file $(all_ids_file) --sample_ids_file $(sample_ids_file) --num_samples $(num_samples)

inference:
	python -m code_instruct.inference --model_name $(model_name) --model_class $(model_class) --example_type $(example_type) --num_shots $(num_shots) --dtype float16 --output_file $(output_file) --sample_ids_file $(sample_ids_file) --ds_inference

# needed if training
split-tasks:
	python -m code_instruct.split_tasks --output_dir splits/default
