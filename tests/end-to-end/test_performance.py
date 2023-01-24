from __future__ import annotations

import os
import subprocess
import sys
import zipfile
from pathlib import Path
from timeit import Timer
from typing import Any, Callable


def get_project_dir() -> Path:
    for parent in Path(__file__).parents:
        if (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError("pyproject.toml")


class RelativeBenchmark:
    def __init__(self) -> None:
        self._baseline = self._benchmark(self._baseline_operation)

    def _benchmark(self, function: Callable[..., Any]) -> float:
        # We run the function in setup as well, to 'prime' relevant caches
        runs = 5
        return int(Timer(stmt=function, setup=function).timeit(runs) / runs * 1000)

    def _baseline_operation(self) -> None:
        files = (get_project_dir() / "lib" / "binarylane").glob("**/*.py")

        with zipfile.ZipFile(os.devnull, "w", compression=zipfile.ZIP_DEFLATED) as zip:
            for file in files:
                zip.write(file)

    def get_relative_performance(self, function: Callable[..., Any]) -> float:
        """Provides a performance score for function, relative to a baseline task (lower = faster).

        Since every device that runs performance tests will go at different speeds, we cannot just say
        that a given task must complete in a specific time. Instead, we perform a baseline operation (read and
        compress the python files from our API lib/ directory) and use that to provide a relative performance number.

        For reference on the computer this was developed on, typical value of _baseline is about 0.23sec

        return: Time taken to execute function, divided by time taken to perform baseline operation.
        - 1.00 means function took the same amount of time as the baseline operation
        - 2.00 means function took twice as long as the baseline operation
        - 0.50 means function took half as long as the baseline operation
        """

        benchmark = self._benchmark(function)
        relative = benchmark / self._baseline
        print(f"baseline={self._baseline}ms benchmark={benchmark}ms relative={relative:.2f}x")
        return relative

    def get_bl_performance(self, *args: str) -> float:
        return self.get_relative_performance(
            lambda: subprocess.check_call(
                [sys.executable, "-m", "binarylane.console"] + list(args), stdout=subprocess.DEVNULL
            )
        )


def test_account_help() -> None:
    assert RelativeBenchmark().get_bl_performance("account", "--help") < 2.0


def test_account_get_help() -> None:
    assert RelativeBenchmark().get_bl_performance("account", "get", "--help") < 6.0
