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

# pylint: disable=redefined-outer-name; Definition and use of a pytest fixture in same file.
"""Fixtures and utilities for tests."""
from pathlib import Path

import pytest
from click.testing import CliRunner


@pytest.fixture(scope="session")
def rootpath(pytestconfig) -> Path:
    """
    The path to the root of the repository. Resolving it relies on the location of file
    ``pyproject.toml``.
    """
    return pytestconfig.rootpath


@pytest.fixture(scope="session")
def snapshots_path(rootpath) -> Path:
    """The path to the directory with snapshots that tests can compare with."""
    return rootpath / "tests" / "__snapshots__"


@pytest.fixture(scope="session", autouse=True)
def adjust_snapshots_contents(snapshots_path) -> None:  # noqa: PT004
    """
    Some of the output of the tool is empty directories. However, we cannot track
    (recreate) empty directories via Git. If we place a dummy `.keep` file in them,
    then the output of the tool will not match.
    Thus, adjusting the contents of the snapshots directory before running any tests.
    """
    for relpath in (
        ("minimal", "all_params", "logs"),
        ("minimal", "default_params", "logs"),
        ("minimal_ui", "all_params", "logs"),
        ("minimal_ui", "default_params", "logs"),
        ("minimal_ui", "l10n_params", "logs"),
        (
            "minimal_ui",
            "all_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "assets",
        ),
        (
            "minimal_ui",
            "all_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "components",
        ),
        (
            "minimal_ui",
            "all_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "hooks",
        ),
        (
            "minimal_ui",
            "default_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "assets",
        ),
        (
            "minimal_ui",
            "default_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "components",
        ),
        (
            "minimal_ui",
            "default_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "hooks",
        ),
        (
            "minimal_ui",
            "l10n_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "components",
        ),
        (
            "minimal_ui",
            "l10n_params",
            "projects",
            "tester_workflow",
            "tester_workflow_ui",
            "src",
            "hooks",
        ),
        ("single_form", "all_params", "logs"),
        ("single_form", "default_params", "logs"),
        ("single_form", "l10n", "logs"),
        ("single_form", "two_wfs", "logs"),
    ):
        Path(snapshots_path, *relpath).mkdir(exist_ok=True)


@pytest.fixture
def example_fixture():  # noqa: PT004
    """Example fixture."""
    print("This is the setup in the example fixture.")
    yield
    print("This is teardown in the example fixture.")


@pytest.fixture
def runner():
    """A runner of click-built CLI with the CWD set to a temporary directory."""
    r = CliRunner()
    with r.isolated_filesystem():
        yield r
