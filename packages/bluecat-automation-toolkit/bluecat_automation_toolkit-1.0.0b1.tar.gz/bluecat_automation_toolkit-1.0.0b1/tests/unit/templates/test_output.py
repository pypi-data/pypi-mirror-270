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

from pathlib import Path

import pytest

from bluecat_automation_toolkit._internal.output import ToolkitTemplateDefinition
from tests import utils


@pytest.mark.usefixtures("runner")
def test_simple_remove(snapshots_path):
    cwd = Path.cwd()
    d = SimpleRemoveDefinition(cwd)
    assert d.render() == 0
    assert utils.cmp_snapshot(cwd, snapshots_path / "output" / "simple_remove")


@pytest.mark.usefixtures("runner")
def test_recursive_remove(snapshots_path):
    cwd = Path.cwd()
    d = RecursiveRemoveDefinition(cwd)
    assert d.render() == 0
    assert utils.cmp_snapshot(cwd, snapshots_path / "output" / "recursive_remove")


class SimpleRemoveDefinition(ToolkitTemplateDefinition):
    """Definition for a template that adds then removes a file."""

    def __init__(self, dst: Path):
        super().__init__(
            dst,
            "tests.unit.templates.test_template_files",
            jinja_params={},
        )

        self._jinja_template(Path(dst, "TESTFILE1.md"), Path("TESTFILE1.md"))
        self._jinja_template(Path(dst, "TESTFILE2.md"), Path("TESTFILE2.md"))

        self._remove(Path(dst, "TESTFILE1.md"))


class RecursiveRemoveDefinition(ToolkitTemplateDefinition):
    """Definition for a template that adds another template and removes a file from it."""

    def __init__(self, dst: Path):
        super().__init__(
            dst,
            "tests.unit.templates.test_template_files",
            jinja_params={},
        )

        simple_def = SimpleRemoveDefinition(dst)

        self._item(simple_def)

        self._remove(Path(dst, "TESTFILE1.md"))

        self._jinja_template(Path(dst, "TESTFILE1.md"), Path("TESTFILE3.md"))
