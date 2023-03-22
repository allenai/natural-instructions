# Set up the evaluation script

We use the [`rouge-score`](https://github.com/google-research/google-research/tree/master/rouge) library to compute the ROUGE-L score.

Rouge scores are computed after tokenization. For English tasks, we use the default tokenizer implemented in the libary. For cross-lingual tasks, since the output text are in different languages and the default tokenizer cannot handle non-English text very well, we use the [`GPT2 tokenizer`](https://huggingface.co/docs/transformers/model_doc/gpt2#transformers.GPT2Tokenizer) instead, which is based on Byte-level BPE. Space (`Ġ`) prefix will be removed from the GPT2 tokenization output.

As of 06/10/2022, the pip released `rouge-score` library doesn't support a user-defined tokenizer. You need to clone it from its latest codebase and put it into `eval/automic/`.

```bash
cd eval/automatic/
svn export https://github.com/google-research/google-research/trunk/rouge rouge
```

Then, you can evaluate your prediction output as follows:

```bash
python evaluation.py --prediction_file=predictions.jsonl --reference_file=references.jsonl
```

Each line of `predictions.jsonl` should correspond to a json object that contains `id` and `prediction` fields. `reference.jsonl` should have `id`, `references`, `task_id`, `task_category` and `track` in each line. To produce the reference file of our official test set, you can run the script in [`eval/automatic/leaderboard/create_reference_file.py`](eval/automatic/leaderboard/create_reference_file.py) as follows:

```bash
python eval/automatic/leaderboard/create_reference_file.py
