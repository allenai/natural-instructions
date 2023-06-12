import importlib
import json
import os
import random
import shutil
from enum import Enum
from functools import partial
from typing import Callable, List, Tuple, Union
from uuid import uuid4

import json5
import torch


class ExampleType(Enum):
    CODE_INSTRUCTIONS = "code_instructions"
    CODE_INSTRUCTIONS_WITHOUT_DOCSTRING = "code_instructions_without_docstring"
    FUNCTION_DEFINITION = "function_definition"
    NATURAL_INSTRUCTIONS = "natural_instructions"
    NATURAL_INSTRUCTIONS_WITH_DOCSTRING = "natural_instructions_with_docstring"
    NO_INSTRUCTION_CODE_EXAMPLES = "no_instruction_code_examples"
    NO_INSTRUCTION_NATURAL_EXAMPLES = "no_instruction_natural_examples"
    NO_INSTRUCTION_GENERIC_FUNCTION_CALL = "no_instruction_generic_function_call"


class Datapoint:
    def __init__(
        self,
        id: str,
        task: str,
        preprocessing_function: Callable,
        original_instruction: str,
        original_input: str,
        outputs: List[str],
        code_instruction: str,
        parsed_program: dict,
        few_shots: List[dict],
        num_shots: int = 0,
    ) -> None:
        self.id = id
        self.task = task
        self.preprocessing_function = preprocessing_function
        self.original_instruction = original_instruction
        self.original_input = original_input
        self.outputs = outputs
        self.code_instruction = code_instruction
        self.doc_instruction, self.code_instruction_without_doc = self.separate_docstring_and_code()
        self.function_instruction = self.get_function_instruction()
        self.parsed_program = parsed_program
        self.few_shots = few_shots
        self.num_shots = min(num_shots, len(self.few_shots))

    def separate_docstring_and_code(self) -> str:
        def get_is_doc_or_comment_line(code_instruction_lines: List[str]) -> List[Union[Tuple[int], int]]:
            result = []

            i = 0
            while i < len(code_instruction_lines):
                if code_instruction_lines[i].count('"""') == 2:
                    result.append(True)
                elif '"""' in code_instruction_lines[i]:
                    result.append(True)
                    i += 1
                    while '"""' not in code_instruction_lines[i]:
                        result.append(True)
                        i += 1
                    result.append(True)
                elif "#" in code_instruction_lines[i]:
                    result.append(True)
                else:
                    result.append(False)

                i += 1

            return result

        def get_doc_instruction(code_instruction_lines: List[str], is_doc_or_comment_line: List[int]) -> str:
            doc_instruction_lines = []
            for i, line in enumerate(code_instruction_lines):
                if is_doc_or_comment_line[i]:
                    doc_instruction_lines.append(line.strip())

            doc_instruction = "\n".join(doc_instruction_lines)

            return doc_instruction

        def get_code_instruction_without_doc(
            code_instruction_lines: List[str], is_doc_or_comment_line: List[int]
        ) -> str:
            code_instruction_without_doc_lines = []
            for i, line in enumerate(code_instruction_lines):
                if not is_doc_or_comment_line[i]:
                    code_instruction_without_doc_lines.append(line)

            code_instruction_without_doc = "\n".join(code_instruction_without_doc_lines)

            return code_instruction_without_doc

        code_instruction_lines = self.code_instruction.split("\n")
        is_doc_or_comment_line = get_is_doc_or_comment_line(code_instruction_lines)
        doc_instruction = get_doc_instruction(code_instruction_lines, is_doc_or_comment_line)
        code_instruction_without_doc = get_code_instruction_without_doc(code_instruction_lines, is_doc_or_comment_line)

        return doc_instruction, code_instruction_without_doc

    def get_function_instruction(self) -> str:
        code_lines = self.code_instruction.split("\n")
        for line_number, line in enumerate(code_lines):
            if "->" in line:
                break

        function_instruction = "\n".join(code_lines[: line_number + 1])
        return function_instruction

    def get_example(self, type: ExampleType, eos_token: str) -> Tuple[str]:
        def _get_example(
            num_shots: int, few_shots_list: List[dict], prepare_shot: Callable, original_input: str, instruction: str
        ):
            few_shots = ""
            if num_shots > 0:
                few_shot_examples = few_shots_list[: self.num_shots]
                for example in few_shot_examples:
                    example = "\n\n" + prepare_shot(input=example["input"], output=example["output"])
                    few_shots += example
            few_shots += "\n\n"

            query = prepare_shot(input=original_input)
            if instruction == "":
                few_shots = few_shots.lstrip()
            example = f"{instruction}{few_shots}{query}\n"

            return example

        if type == ExampleType.NATURAL_INSTRUCTIONS:
            prepare_shot = partial(self.prepare_natural_instructions_shot, eos_token=eos_token)
            instruction = self.original_instruction
        elif type == ExampleType.CODE_INSTRUCTIONS:
            prepare_shot = partial(self.prepare_code_shot, eos_token=eos_token)
            instruction = self.code_instruction
        elif type == ExampleType.FUNCTION_DEFINITION:
            prepare_shot = partial(self.prepare_code_shot, eos_token=eos_token)
            instruction = self.function_instruction
        elif type == ExampleType.NATURAL_INSTRUCTIONS_WITH_DOCSTRING:
            prepare_shot = partial(self.prepare_natural_instructions_shot, eos_token=eos_token)
            instruction = f"{self.original_instruction}\n{self.doc_instruction}"
        elif type == ExampleType.CODE_INSTRUCTIONS_WITHOUT_DOCSTRING:
            prepare_shot = partial(self.prepare_code_shot, eos_token=eos_token)
            instruction = self.code_instruction_without_doc
        elif type == ExampleType.NO_INSTRUCTION_CODE_EXAMPLES:
            prepare_shot = partial(self.prepare_code_shot, eos_token=eos_token)
            instruction = ""
        elif type == ExampleType.NO_INSTRUCTION_NATURAL_EXAMPLES:
            prepare_shot = partial(self.prepare_natural_instructions_shot, eos_token=eos_token)
            instruction = ""
        elif type == ExampleType.NO_INSTRUCTION_GENERIC_FUNCTION_CALL:
            prepare_shot = partial(self.prepare_code_shot, generic_function_call=True, eos_token=eos_token)
            instruction = ""
        else:
            raise Exception(f"unknown type '{type}'")

        return (
            _get_example(self.num_shots, self.few_shots, prepare_shot, self.original_input, instruction),
            self.outputs,
        )

    def prepare_natural_instructions_shot(self, input: str, eos_token: str, output: str = None) -> str:
        result = f"input: {input}\noutput:"
        if output is not None:
            result += f" {output}{eos_token}"
        return result

    def prepare_code_shot(
        self, input: str, eos_token: str, output: str = None, generic_function_call: bool = False
    ) -> str:
        function_signature = self.parsed_program["execute"]
        arguments = function_signature.split("(")[1].split(")")[0].split(",")
        input_types = [self.parsed_program["arguments"][arg.strip()] for arg in arguments]

        preprocessed_inputs = self.preprocessing_function(input)

        if not isinstance(preprocessed_inputs, tuple):
            preprocessed_inputs = [str(preprocessed_inputs)]
        else:
            preprocessed_inputs = [str(input) for input in preprocessed_inputs]

        for i, (input_type_, preprocessed_input_) in enumerate(zip(input_types, preprocessed_inputs)):
            if input_type_ == "str":
                preprocessed_inputs[i] = '"' + preprocessed_input_ + '"'

        preprocessed_inputs = ", ".join(preprocessed_inputs)
        preprocessed_inputs = f"({preprocessed_inputs})"

        if generic_function_call:
            method_name = "func"
        else:
            method_name = self.parsed_program["execute"].split("(")[0]

        result = f">>> {method_name}{preprocessed_inputs}"
        if output is not None:
            result += f"\n{output}{eos_token}"
        return result


class NaturalInstructionsDataset(torch.utils.data.Dataset):
    def __init__(
        self,
        split: str = "all",
        num_shots: int = 0,
        ignore_tasks: List[Union[str, int]] = [],
        multilingual: bool = True,
        allowed_list_file: str = None,
    ) -> None:
        fnames = os.listdir("instructions")
        dataset_map = self.get_dataset_map()

        fnames = self.prune_tasks(fnames, dataset_map, ignore_tasks, multilingual)
        fnames = self.filter_tasks_by_split(fnames, dataset_map, split)
        fnames.sort(key=lambda x: int(x.split(".py")[0]))

        self.tmp = f"tmp_{'_'.join(str(uuid4()).split('-'))}"

        os.makedirs(self.tmp, exist_ok=True)
        open(os.path.join(self.tmp, "__init__.py"), "w")

        self.num_shots = num_shots
        self.allowed_list = (
            None if allowed_list_file is None else set([i.strip() for i in open(allowed_list_file, "r").readlines()])
        )

        self.examples = []
        num_tasks = 0
        for fname in fnames:
            examples = self.create_examples(fname, dataset_map)
            self.examples.extend(examples)

            if len(examples) != 0:
                num_tasks += 1
                print(f"task {fname} has {len(examples)} examples")

        print("total examples =", len(self))
        print("total tasks with examples =", num_tasks)
        print("total tasks with 0 examples =", len(fnames) - num_tasks)

        shutil.rmtree(self.tmp)

    @classmethod
    def is_task_multilingual(cls, instruction_language: str, input_language: str, output_language: str) -> bool:
        return not (
            instruction_language.lower() == "english"
            and input_language.lower() == "english"
            and output_language.lower() == "english"
        )

    @classmethod
    def prune_tasks(
        cls, fnames: List[str], dataset_map: dict, ignore_tasks: List[Union[str, int]] = [], multilingual: bool = True
    ) -> List[str]:
        for i, task in enumerate(ignore_tasks):
            task = str(task).split(".")[0] + ".py"
            ignore_tasks[i] = task

        fnames = list(filter(lambda i: str(i) not in ignore_tasks, fnames))

        if multilingual:
            return fnames
        else:
            result_fnames = []

            for fname in fnames:
                json_data = json.load(open(os.path.join("tasks", dataset_map[fname.split(".")[0]]), "r"))

                if not cls.is_task_multilingual(
                    json_data["Instruction_language"][0],
                    json_data["Input_language"][0],
                    json_data["Output_language"][0],
                ):
                    result_fnames.append(fname)

            return result_fnames

    @classmethod
    def filter_tasks_by_split(cls, fnames: List[str], dataset_map: dict, split: str = "all") -> List[str]:
        if split == "all":
            return fnames

        allowed_tasks = open(os.path.join("splits/default", f"{split}_tasks.txt"), "r").readlines()
        allowed_tasks = [task.strip() for task in allowed_tasks]

        result_fnames = []
        for fname in fnames:
            if dataset_map[fname.split(".py")[0]].split(".json")[0] in allowed_tasks:
                result_fnames.append(fname)
        return result_fnames

    def get_few_shots(self, positive_examples: List[dict], is_classification_task: bool) -> List[dict]:
        if is_classification_task:
            classes = set()
            few_shots_indices = set()
            few_shots = []

            for i, example in enumerate(positive_examples):
                if example["output"] not in classes:
                    classes.add(example["output"])

                    few_shots_indices.add(i)
                    few_shots.append(example)

            for i, example in enumerate(positive_examples):
                if i not in few_shots_indices:
                    few_shots.append(example)

            few_shots = few_shots[: self.num_shots]
        else:
            random.seed(42)
            few_shots = random.sample(positive_examples, self.num_shots)

        return few_shots

    def create_examples(self, fname: str, dataset_map: dict) -> List[Datapoint]:
        parsed_instruction, parsed_program, preprocessing_function = self.load_file_data(fname)
        json_data = json.load(open(os.path.join("tasks", dataset_map[fname.split(".")[0]]), "r"))

        original_instruction = json_data["Definition"][0]

        is_classification_task = False
        for category in json_data["Categories"]:
            if "classification" in category.lower():
                is_classification_task = True
                break

        few_shots = self.get_few_shots(json_data["Positive Examples"], is_classification_task)

        examples = []

        for example in json_data["Instances"]:
            example = Datapoint(
                id=example["id"],
                task=dataset_map[fname.split(".")[0]],
                preprocessing_function=preprocessing_function,
                original_instruction=original_instruction,
                original_input=example["input"],
                outputs=example["output"],
                code_instruction=parsed_instruction,
                parsed_program=parsed_program,
                few_shots=few_shots,
                num_shots=self.num_shots,
            )

            if self.allowed_list is None or example.id in self.allowed_list:
                examples.append(example)

        return examples

    @classmethod
    def get_dataset_map(cls) -> dict:
        dataset_map = {}

        data_fnames = os.listdir("tasks")
        for fname in data_fnames:
            if not fname.endswith(".json"):
                continue

            task = str(int(fname.split("task")[1].split("_")[0]))
            dataset_map[task] = fname

        return dataset_map

    def load_file_data(self, fname: str) -> dict:
        with open(os.path.join("instructions", fname), "r") as file:
            lines = file.readlines()
            instruction, program, preprocessor = self.parse_data_into_sections(lines)

            preprocessing_function = self.parse_preprocessor(preprocessor, fname)
            parsed_program = self.parse_program(program)
            parsed_instruction = self.parse_instruction(instruction)

            return parsed_instruction, parsed_program, preprocessing_function

    @classmethod
    def get_starting_line_for_section(cls, lines: List[str], section_name: str) -> int:
        for line_number, line in enumerate(lines):
            if line.strip() == section_name:
                return line_number

    @classmethod
    def parse_data_into_sections(cls, lines: List[str]) -> Tuple[List[str]]:
        program_beginning = cls.get_starting_line_for_section(lines, "# program")
        preprocessor_beginning = cls.get_starting_line_for_section(lines, "# preprocessor")

        instruction = lines[:program_beginning]
        program = lines[program_beginning + 1 : preprocessor_beginning]
        preprocessor = lines[preprocessor_beginning + 1 :]

        return instruction, program, preprocessor

    def parse_preprocessor(self, preprocessor: List[str], fname: str) -> Callable:
        with open(os.path.join(self.tmp, f"_{fname}"), "w") as file:
            file.writelines(preprocessor)

        module = importlib.import_module(f"{self.tmp}._{fname.split('.')[0]}")
        return module.preprocess

    @classmethod
    def parse_program(cls, program_lines: List[str]) -> dict:
        return json5.loads("".join(program_lines))

    @classmethod
    def parse_instruction(cls, instruction: list) -> str:
        return "".join(instruction).strip()

    def __getitem__(self, index: int) -> Datapoint:
        return self.examples[index]

    def __len__(self) -> Datapoint:
        return len(self.examples)
