import importlib
import json
import logging
import os
import re
from typing import Callable, List, Tuple

import colorlog
import json5
from code_instruct.data import NaturalInstructionsDataset


class Logger:
    def __init__(self, name: str) -> logging.Logger:
        formatter = colorlog.ColoredFormatter(
            "%(log_color)s[%(levelname)5s]: %(message)s%(reset)s",
            # "%(log_color)s%(asctime)s - [%(levelname)s]: %(message)s (%(filename)s:%(lineno)d)%(reset)s",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            secondary_log_colors={},
            style="%",
        )

        handler = colorlog.StreamHandler()
        handler.setFormatter(formatter)

        logger = colorlog.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        self.logger = logger
        self.error_count = 0

    def error(self, message: str, fname: str) -> None:
        self.error_count += 1
        self.logger.error(f"{fname}: 😔 {message}")

    def info(self, message: str, fname: str) -> None:
        self.logger.info(f"{fname}: 🙂 {message}")


logger = Logger(__name__)


def test_filename_correctness(fname: str) -> None:
    fname_split = fname.split(".")

    if len(fname_split) < 2:
        logger.error("filename doesn't have an extension", fname)
        return

    try:
        x = int(fname_split[0])
        if x < 0:
            logger.error("filename should start with a non-negative integer", fname)
    except:
        logger.error("filename should start with a non-negative integer", fname)

    if fname_split[1] != "py":
        logger.error("filename should end with .py extension", fname)


def check_section_correctness(lines: List[str], section_name: str, fname: str) -> int:
    found = -1

    for line_number, line in enumerate(lines):
        if line.strip() == section_name:
            if found == -1:
                found = line_number
            else:
                logger.error(f"found duplicate '{section_name}'", fname)
                return

    if found == -1:
        logger.error(f"'{section_name}' not found", fname)
        return

    return found


def parse_data_into_sections(lines: List[str], fname: str) -> Tuple[List[str]]:
    program_beginning = check_section_correctness(lines, "# program", fname)
    preprocessor_beginning = check_section_correctness(lines, "# preprocessor", fname)

    if program_beginning is None or preprocessor_beginning is None:
        return

    if program_beginning is not None and preprocessor_beginning is not None:
        instruction = lines[:program_beginning]
        program = lines[program_beginning + 1 : preprocessor_beginning]
        preprocessor = lines[preprocessor_beginning + 1 :]

        return instruction, program, preprocessor


def dump_json_formatted_data(lines: List[str], fname: str) -> None:
    data = {}
    for line_number, line in enumerate(lines):
        data[line_number] = line

    json.dump(data, open(os.path.join("tmp", fname.split(".")[0] + ".json"), "w", encoding="UTF-8"), indent=4)


def parse_instruction(instruction: list) -> str:
    return "".join(instruction)


def check_and_parse_program(
    program_lines: List[str], return_variables_from_preprocessor: List[str], fname: str
) -> dict:
    program = None

    try:
        program = json5.loads("".join(program_lines))

        if "method" not in program:
            logger.error("program json doesn't have 'method'", fname)
            return
        elif type(program["method"]) != str:
            logger.error("'method' in  program json should be a string", fname)
            return

        if "arguments" not in program:
            logger.error("program json doesn't have 'arguments'", fname)
            return
        elif type(program["arguments"]) != dict:
            logger.error("'arguments' in program json should be a dict", fname)
            return

        if "return" not in program:
            logger.error("program json doesn't have 'return'", fname)
            return
        elif type(program["return"]) != str:
            logger.error("'return' in program json should be a string", fname)
            return

        if "execute" not in program:
            logger.error("program json doesn't have 'execute'", fname)
            return
        elif type(program["execute"]) != str:
            logger.error("'execute' in program json should be a string", fname)
            return

        function_signature = program["execute"]

        arguments = function_signature.split("(")[1].split(")")[0].split(",")
        arguments = [arg.strip() for arg in arguments]

        if len(arguments) != len(program["arguments"]):
            logger.error("method signature in 'execute' has different number of arguments than 'arguments'", fname)
            return

        for argument in arguments:
            if argument not in program["arguments"]:
                logger.error(
                    f"method signature in 'execute' has argument '{argument}' which is missing in 'arguments'", fname
                )
                return

        if return_variables_from_preprocessor != arguments:
            logger.error("method signature has different input order as preprocessors return variables", fname)
            return

        if program["method"] != program["execute"].split("(")[0]:
            logger.error("method name mismatch in 'execute' and 'method'", fname)
            return
    except:
        logger.error("program is not a valid json object", fname)

    return program


def parse_preprocessor(preprocessor: List[str], fname: str) -> Callable:
    returns = preprocessor[-1].split("return")[1].split(",")
    returns = [r.strip() for r in returns]

    with open(os.path.join("tmp", f"_{fname}"), "w", encoding="UTF-8") as file:
        file.writelines(preprocessor)

    try:
        module = importlib.import_module(f"tmp._{fname.split('.')[0]}")
        return returns, module.preprocess
    except:
        logger.error("function is not a valid python function", fname)
        return


def check_function_signatures(instruction: List[str], fname: str) -> dict:
    for line in instruction:
        match = re.search("def [\w]+\(.*", line)
        if match is None:
            continue

        match = match.span()
        function_signature = line[match[0] : match[1]]

        try:
            function_signature.split("->")[1].strip()
        except:
            logger.error(f"return type is not specified in function signature {function_signature}", fname)

        arguments = function_signature.split("(")[1].split(")")[0].split(",")
        arguments = [arg.strip() for arg in arguments]

        try:
            for arg in arguments:
                arg.split(":")[1].strip()
        except:
            logger.error(
                f"function arguments don't have a specified type in function signature {function_signature}", fname
            )


def load_file_data(fname: str) -> dict:
    with open(os.path.join("instructions", fname), "r", encoding="UTF-8") as file:
        lines = file.readlines()

        # dump_json_formatted_data(lines, fname)

        sections = parse_data_into_sections(lines, fname)
        if sections is None:
            return

        instruction, program, preprocessor = sections

        preprocessing_program = parse_preprocessor(preprocessor, fname)
        if preprocessing_program is None:
            return

        return_variables_from_preprocessor, preprocessing_function = preprocessing_program

        parsed_program = check_and_parse_program(program, return_variables_from_preprocessor, fname)

        check_function_signatures(instruction, fname)

        parsed_instruction = parse_instruction(instruction)

        return parsed_instruction, parsed_program, preprocessing_function


def check_preprocessing_function(preprocessing_function: Callable, dataset_map: str, fname: str) -> None:
    data_fname = dataset_map[fname.split(".")[0]]
    dataset = json.load(open(os.path.join("tasks", data_fname), "r", encoding="UTF-8"))

    for example in dataset["Positive Examples"]:
        try:
            preprocessing_function(example["input"])
        except:
            logger.error(f"preprocessing function crashed for example {example}", fname)

    for example in dataset["Instances"]:
        try:
            preprocessing_function(example["input"])
        except:
            logger.error(f"preprocessing function crashed for example {example}", fname)


def main() -> None:
    fnames = os.listdir("instructions")
    os.makedirs("tmp", exist_ok=True)

    dataset_mapping = NaturalInstructionsDataset.get_dataset_map()

    open(os.path.join("tmp", "__init__.py"), "w", encoding="UTF-8")

    for fname in fnames:
        logger.info(
            "====================================================================================================",
            fname,
        )

        test_filename_correctness(fname)

        parsed_annotations = load_file_data(fname)

        if parsed_annotations is not None:
            _, _, preprocessing_function = parsed_annotations
            check_preprocessing_function(preprocessing_function, dataset_mapping, fname)

        logger.info(
            "====================================================================================================",
            fname,
        )


if __name__ == "__main__":
    main()
