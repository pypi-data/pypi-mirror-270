import importlib
from pathlib import Path

import editorconfig  # type: ignore

from gradema.test import Test
from gradema.test._command import CommandTest
from gradema.test._stdio import StdioTest


def create_python_test(module_name: str) -> Test:
    try:
        # TODO importing the module could run student code in the autograder's process. Maybe we shouldn't do this
        importlib.import_module(module_name)
    except ModuleNotFoundError:
        raise ValueError(f"Module {module_name} not found")

    return CommandTest(["python3", "-m", module_name], ["pudb", "-m", module_name])


def create_python_stdio_test(module_name: str, test_identifier: str, input_file: Path, goal_file: Path) -> Test:
    """
    Creates a traditional stdio test

    :param module_name:
    :param test_identifier:
    :param input_file:
    :param goal_file:
    :return:
    """
    command = ["python3", "-m", module_name]
    return StdioTest(command, test_identifier, input_file, goal_file)


def create_python_arg_test(module_name: str, test_identifier: str, args: list[str], goal_file: Path) -> Test:
    command = ["python3", "-m", module_name] + args
    return StdioTest(command, test_identifier, None, goal_file)


def create_python_format_check_from_path(path: str) -> Test:
    line_length = editorconfig.get_properties(str((Path(path) / "some_random_file.py").absolute())).get("max_line_length")
    command = ["black", "--check"]
    if line_length is not None:
        command.append(f"--line-length={line_length}")
    command.append(path)
    return CommandTest(command)


def create_python_format_check() -> Test:
    return create_python_format_check_from_path(".")


def create_python_type_check() -> Test:
    return CommandTest(["mypy", "--strict", "--disallow-any-explicit", "."])
