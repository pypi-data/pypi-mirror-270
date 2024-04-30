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
import os

import pytest

from bluecat_automation_toolkit.cli import cli


def filter_debug_messages(output: str):
    # get output after the debugging messages
    # change this when "temporary debugging messages" are removed
    return [line for line in output.split("\n") if not line.startswith("DEBUG") and line]


def test_no_overwrite(runner):
    workflow_name = "test_workflow_name"
    args = ["workflow", "new", "single-form", "--name", workflow_name, "-o", "temp"]

    result = runner.invoke(cli, args)
    assert not filter_debug_messages(result.output)[1:]
    assert result.exit_code == 0  # for no overwrite warnings


def test_with_overwrite_all(runner):
    file_error = "File already exists. New file not created."
    folder_warning = "Directory already exists"

    workflow_name = "test_workflow_name"
    args = ["workflow", "new", "single-form", "--name", workflow_name, "-o", "temp"]
    runner.invoke(cli, args)
    result = runner.invoke(cli, args)

    for msg in filter_debug_messages(result.output)[1:]:
        assert (msg.startswith("ERROR") and file_error in msg) or (
            msg.startswith("WARNING") and folder_warning in msg
        )
    assert result.exit_code == errno.EEXIST  # file already exists exit code


@pytest.mark.parametrize(
    ("obj_type", "error_msg", "target", "exit_code"),
    [
        (
            "File",
            "ERROR: temp/.gitignore: File already exists. New file not created.",
            "temp/.gitignore",
            errno.EEXIST,
        ),
        (
            "Directory",
            "WARNING: temp/projects: Directory already exists.",
            "temp/projects",
            0,
        ),
    ],
)
def test_overwrite_single_object(runner, obj_type, error_msg, target, exit_code):
    workflow_name = "test_workflow_name"
    args = ["workflow", "new", "single-form", "--name", workflow_name, "-o", "temp"]

    os.mkdir("temp")
    if obj_type == "File":
        # pylint: disable=unspecified-encoding
        with open(target, "a"):
            pass  # create new file
    elif obj_type == "Directory":
        os.mkdir(target)

    # ensure file/folder was created successfully
    assert os.path.exists(target)

    result = runner.invoke(cli, args)

    assert filter_debug_messages(result.output)[1:][0] == error_msg

    assert result.exit_code == exit_code  # file already exists exit code
