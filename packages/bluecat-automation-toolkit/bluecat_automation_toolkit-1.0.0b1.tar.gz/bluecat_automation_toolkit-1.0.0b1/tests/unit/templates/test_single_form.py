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
import errno
from pathlib import Path

import pytest

from bluecat_automation_toolkit._internal.copyrights import (
    CopyrightDefinition,
)
from bluecat_automation_toolkit._internal.templates.single_form.definition import (
    Definition,
    Parameters,
)
from tests import utils


def render_workflow_files(  # noqa: PLR0913 pylint: disable=too-many-arguments
    path,
    workflow_name,
    cpr,
    languages=(),
    permission_name="",
    link_title=None,
    link_description=None,
):
    p = Parameters(
        workflow_name=workflow_name,
        permission_name=permission_name,
        link_title=link_title,
        link_description=link_description,
        languages=languages,
        copyright=cpr,
    )
    d = Definition(path, p)
    return d.render()


@pytest.mark.usefixtures("runner")
@pytest.mark.parametrize("nested_path", ["", "level1/level2/level3"])
def test_render_with_all_params(nested_path, snapshots_path):
    cwd = Path.cwd() / nested_path
    cpr = CopyrightDefinition("apache2", "", "3000")
    result = render_workflow_files(
        path=cwd,
        workflow_name="test_workflow",
        cpr=cpr,
        permission_name="test_permission",
        link_title="A title for an HTML link",
        link_description="A description of what to be expected",
        languages=(),
    )
    assert result == 0
    assert utils.cmp_snapshot(cwd, snapshots_path / "single_form" / "all_params")


@pytest.mark.usefixtures("runner")
def test_render_with_default_params(snapshots_path):
    cwd = Path.cwd()
    cpr = CopyrightDefinition("", "Test Tester", "3000")
    result = render_workflow_files(
        path=cwd,
        workflow_name="test_workflow",
        cpr=cpr,
    )
    assert result == 0
    assert utils.cmp_snapshot(cwd, snapshots_path / "single_form" / "default_params")


@pytest.mark.usefixtures("runner")
def test_expected_error_with_different_wfs_render(snapshots_path):
    cwd = Path.cwd()

    cpr1 = CopyrightDefinition("mit", "Tester1", "3000")
    result1 = render_workflow_files(
        path=cwd,
        workflow_name="test_name_1",
        permission_name="test_permission_1",
        link_title="Workflow title 1",
        link_description="A description of workflow 1.",
        cpr=cpr1,
    )

    cpr2 = CopyrightDefinition("apache2", "Tester2", "4000")
    result2 = render_workflow_files(
        path=cwd,
        workflow_name="test_name_2",
        permission_name="test_permission_2",
        link_title="Workflow title 2",
        link_description="A description of workflow 2.",
        cpr=cpr2,
    )

    assert result1 == 0
    assert result2 == errno.EEXIST
    assert utils.cmp_snapshot(cwd, snapshots_path / "single_form" / "two_wfs")


@pytest.mark.usefixtures("runner")
def test_render_with_l10n(snapshots_path):
    cwd = Path.cwd()
    cpr = CopyrightDefinition("", "Test Tester", "3000")
    result = render_workflow_files(
        path=cwd,
        workflow_name="test_workflow",
        languages=("fr", "gr", "en"),
        cpr=cpr,
    )
    assert result == 0
    assert utils.cmp_snapshot(cwd, snapshots_path / "single_form" / "l10n")
