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
"""Various utilities used in tests."""
import filecmp
import os
import random
import shutil
import uuid
from pathlib import Path


def random_value() -> str:
    """
    Return a random value that is combination of lowercase letters, numbers, and dashes.
    """
    return str(uuid.uuid4())


def random_variable() -> str:
    """
    Return a random value that starts with a lowercase letter and continues with a
    combination of lowercase letters and numbers.
    """
    return "".join(
        [
            random.choice("abcdefghijklmnopqrstuvwxyz"),  # noqa: S311
            str(uuid.uuid4()).replace("-", ""),
        ]
    )


def _eval_dircmp(cmp: filecmp.dircmp) -> bool:
    """
    Evaluate whether the findings of a directory comparison done with ``dircmp`` indicate
    matching contents.

    Returns ``True`` if the contents match. Otherwise, returns ``False``.
    """
    if (
        cmp.left_only
        or cmp.right_only
        or cmp.diff_files
        or cmp.funny_files
        or cmp.common_funny
    ):
        return False
    return all(_eval_dircmp(subdir_cmp) for subdir_cmp in cmp.subdirs.values())


def cmp_snapshot(dir1: Path, dir2: Path) -> bool:
    """
    Compare two directories whether their contents match.

    .. note::
        If the environment variable ``SAVE_SNAPSHOTS`` is present and its value is `1`
        or `y`, then the snapshot will be created *before* it is compared. This can be
        used to easily create (all) snapshots through a tests run. Note that in that
        case the comparison is meaningless and the tests wouldn't fail because of it.
    """
    if str(os.environ.get("SAVE_SNAPSHOTS")).lower() in ("1", "y"):
        print("DEBUG: Saving snapshots...")
        save_snapshot(dir1, dir2)

    if not dir1.exists() or not dir2.exists():
        return False

    diff = filecmp.dircmp(dir1, dir2)
    return _eval_dircmp(diff)


def save_snapshot(src: Path, dst: Path) -> None:
    """Save the contents of the source to the destination."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
