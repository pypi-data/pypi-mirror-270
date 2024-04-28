import filecmp
import subprocess
from pathlib import Path
from typing import Optional, TextIO

from gradema.test import Test, TestReporter, TestResult, FractionalTestResult


class StdioTest(Test):
    """
    A Standard Input/Output Test

    Traditionally, a stdio test would have no arguments passed to the command, it would have an input file, and a goal file.
    Output is piped to some output file that is not committed to version control.

    This new stdio test is very similar, but it can also do what a traditional arg test could do:
    take no input, and have custom arguments passed to the command.
    If you don't want anything directed into the command's stdin, then just assign None to input_file.
    If you want custom arguments passed to the command, give those custom arguments to the command argument (you may have to do that manually).
    """

    def __init__(self, command: list[str], test_identifier: str, input_file: Optional[Path], goal_file: Path):
        self.command = command
        self.test_identifier = test_identifier
        self.input_file = input_file
        self.goal_file = goal_file

    def run(self, reporter: TestReporter) -> TestResult:
        data = reporter.report_stdio_command(self.command, self.test_identifier, self.input_file)
        output_file = data.stdout_file
        stdin: Optional[TextIO] = None
        try:
            if self.input_file is not None:
                stdin = self.input_file.open("r")
            with output_file.open("w") as stdout:
                completed = subprocess.run(
                    self.command,
                    stdin=stdin if stdin is not None else subprocess.DEVNULL,
                    stdout=stdout,
                    stderr=data.stderr,
                )
        finally:
            if stdin is not None:
                stdin.close()
        if completed.returncode != 0:
            reporter.log(f"Process had non-zero exit code: {completed.returncode}. Not going to execute a diff until the program can complete successfully.")
            return FractionalTestResult(0, 1)

        exactly_the_same = filecmp.cmp(self.goal_file, output_file)
        # TODO fuzzy diff stuff here
        reporter.report_diff_result(self.test_identifier, self.goal_file, output_file, 1.0 if exactly_the_same else 0.0, fuzzy=False)
        if exactly_the_same:
            return FractionalTestResult(1, 1)

        return FractionalTestResult(0, 1)
