# Copyright 2023 BlueCat Networks Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# pylint: disable=missing-module-docstring,missing-function-docstring ; Not required for tests.
# pylint: disable=line-too-long; Let the code style tool handle it.
import datetime
from pathlib import Path

import pytest

from bluecat_automation_toolkit._internal.copyrights import (
    CopyrightDefinition,
    copyright_notice,
)
from bluecat_automation_toolkit.cli import cli


def is_for_special_bluecat_notice(line: str) -> bool:
    return (
        "Portions which reproduce template contents from BATK are Copyright 2023 BlueCat Networks Inc."
        in line
    )


def starts_with_lines(file, lines: list[str]) -> None:
    i = 0
    while True:
        if i >= len(lines):
            return True
        expected = lines[i]
        actual = file.readline()
        if actual != expected:
            return False
        i += 1

    return False


def paths_for_different_formats(
    root_path: Path, workflow_name: str
) -> tuple[tuple[Path, str]]:
    return (
        (root_path / "Makefile", "py"),
        (
            root_path
            / "projects"
            / workflow_name
            / f"{workflow_name}_ui"
            / ".eslintrc.js",
            "js",
        ),
        (
            root_path
            / "projects"
            / workflow_name
            / f"{workflow_name}_ui"
            / "src"
            / "index.html",
            "html",
        ),
    )


@pytest.mark.parametrize(
    "opts",
    [
        [],  # the defaults
        ["--copyright-license", "none"],
        ["--copyright-license", "mit", "--no-copyright"],
    ],
)
def test_no_copyright(runner, opts):
    workflow_name = "test_workflow_name"
    args = ["workflow", "new", "single-form", "--name", workflow_name, *opts]

    root_path = Path.cwd()  # The CWD will be the destination path by default.

    result = runner.invoke(cli, args)
    assert result.exit_code == 0

    for path, _ in paths_for_different_formats(root_path, workflow_name):
        assert path.exists(), f"File not created as expected: {path}"
        with path.open() as f:
            for line in f.readlines():
                if is_for_special_bluecat_notice(line):
                    continue  # Ignore lines with this addendum.
                assert (
                    "Copyright" not in line
                ), f"File contains unexpected copyright notice: {path}"


@pytest.mark.parametrize("license", ["apache2", "mit", "proprietary"])
def test_licenses(runner, license):  # noqa: A002 pylint: disable=W0622
    workflow_name = "test_workflow_name"
    owner_name = "test owner name"
    copyright_year = str(datetime.datetime.now().year)  # noqa: DTZ005
    opts = ["--copyright-license", license, "--copyright-name", owner_name]
    args = ["workflow", "new", "single-form", "--name", workflow_name, *opts]
    cr = CopyrightDefinition(license, owner_name, copyright_year)

    root_path = Path.cwd()  # The CWD will be the destination path by default.

    result = runner.invoke(cli, args)
    assert result.exit_code == 0

    for (
        path,
        fmt,
    ) in paths_for_different_formats(root_path, workflow_name):
        assert path.exists(), f"File not created as expected: {path}"

        notice = copyright_notice(cr, fmt).splitlines(keepends=True)
        with path.open() as f:
            assert starts_with_lines(
                f, notice
            ), f"File does not contain expected copyright notice: {path}"
