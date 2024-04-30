from os import PathLike
from pathlib import Path

from gradema.test import Test
from gradema.test._command import CommandTest
from gradema.test._stdio import StdioTest


# noinspection PyMethodMayBeStatic
class RustProgram:
    def __init__(self, main_location: str | PathLike[str] | Path, binary_location: str | PathLike[str] | Path):
        self.main_location = main_location if isinstance(main_location, Path) else Path(main_location)
        self.binary_location = binary_location if isinstance(binary_location, Path) else Path(binary_location)

    def create_compile_step(self) -> Test:
        return CommandTest(["cargo", "build"])

    def create_stdio_test(self, test_identifier: str, input_file: Path, goal_file: Path) -> Test:
        command = [str(self.binary_location)]
        return StdioTest(command, test_identifier, input_file, goal_file)

    def create_format_check(self) -> Test:
        """
        Creates a rustfmt check.

        Note that the resulting command will be something like ``rustfmt --check src/main.rs``.
        Even though this only includes the main file, all files referenced by main will also be format checked -- it's not necessary to list all the files here!
        https://github.com/rust-lang/rustfmt/issues/2426

        :return: A test that completes successfully when there are no formatting errors
        """
        return CommandTest(["rustfmt", "--check", str(self.main_location)])

    def create_cargo_command(self, arguments: list[str]) -> Test:
        return CommandTest(["cargo"] + arguments)
