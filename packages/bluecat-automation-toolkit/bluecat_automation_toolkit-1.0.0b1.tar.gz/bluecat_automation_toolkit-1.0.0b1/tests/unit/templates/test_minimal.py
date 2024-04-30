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

from bluecat_automation_toolkit._internal.copyrights import (
    CopyrightDefinition,
)
from bluecat_automation_toolkit._internal.templates.minimal.definition import (
    Definition,
    Parameters,
)
from tests import utils


@pytest.mark.usefixtures("runner")
@pytest.mark.parametrize("nested_path", ["", "level1/level2/level3"])
def test_render_with_all_params(nested_path, snapshots_path):
    cwd = Path.cwd() / nested_path
    cpr = CopyrightDefinition("apache2", "Test Tester", "3000")
    p = Parameters(
        workflow_name="tester_workflow",
        copyright=cpr,
        permission_name="test_permission",
        link_title="A title for an HTML link",
        link_description="A description of what to be expected",
    )
    d = Definition(cwd, p)
    assert d.render() == 0

    assert utils.cmp_snapshot(cwd, snapshots_path / "minimal" / "all_params")


@pytest.mark.usefixtures("runner")
def test_render_with_default_params(snapshots_path):
    cwd = Path.cwd()
    cpr = CopyrightDefinition("proprietary", "Test Tester", "3000")
    p = Parameters(
        workflow_name="tester_workflow",
        copyright=cpr,
        permission_name="",
        link_title=None,
        link_description=None,
    )
    d = Definition(Path.cwd(), p)
    assert d.render() == 0

    assert utils.cmp_snapshot(cwd, snapshots_path / "minimal" / "default_params")
