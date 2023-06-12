import argparse
from typing import List

import torch
from deepspeed import init_inference
from transformers import AutoConfig, AutoTokenizer


def pad(arrays: list, padding: int, max_length: int = None, side: str = "left"):
    if max_length is None:
        max_length = max(list(map(len, arrays)))

    if side == "left":
        inputs = [[padding] * (max_length - len(array)) + array for array in arrays]
        masks = [[0] * (max_length - len(array)) + [1] * len(array) for array in arrays]
    else:
        inputs = [array + [padding] * (max_length - len(array)) for array in arrays]
        masks = [[1] * len(array) + [0] * (max_length - len(array)) for array in arrays]

    return {"input_ids": torch.tensor(inputs), "attention_mask": torch.tensor(masks)}


class Model:
    def __init__(self, args: argparse.Namespace) -> None:
        self.tokenizer = load_tokenizer(args.model_name)
        self.model = args.model_class.from_pretrained(args.model_name, torch_dtype=args.dtype)
        self.is_encoder_decoder = AutoConfig.from_pretrained(args.model_name).is_encoder_decoder
        self.input_device = "cuda:0" if torch.cuda.is_available() else "cpu"

        self.max_input_length = args.max_input_length
        if args.ds_inference:
            self.model = init_inference(self.model, mp_size=1, dtype=args.dtype, replace_with_kernel_inject=True)
        else:
            self.model.to(self.input_device)

    def generate(self, input_ids: List[int], **generate_kwargs) -> List[str]:
        input_tokens = pad(input_ids, self.tokenizer.pad_token_id)

        for t in input_tokens:
            if torch.is_tensor(input_tokens[t]):
                input_tokens[t] = input_tokens[t].to(self.input_device)

        num_input_tokens = input_tokens["input_ids"].shape[1]

        output = self.model.generate(return_dict_in_generate=True, **input_tokens, **generate_kwargs)
        output_tokens = output.sequences

        if not self.is_encoder_decoder:
            output_tokens = output_tokens[:, num_input_tokens:]

        generated_text = self.tokenizer.batch_decode(output_tokens, skip_special_tokens=True)
        return generated_text


def load_tokenizer(model_name: str) -> AutoTokenizer:
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

    return tokenizer
