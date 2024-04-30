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
"""Definitions and resources for toolkit internal template "wf-def"."""
# pylint: disable=fixme
import typing as t
from dataclasses import dataclass
from pathlib import Path

from bluecat_automation_toolkit._internal.cli import CopyrightDefinition
from bluecat_automation_toolkit._internal.output import (
    ToolkitTemplateDefinition,
    name_to_js_variable_name,
)
from bluecat_automation_toolkit._internal.templates import license_file


@dataclass(init=True, frozen=True)
class Parameters:
    """User-provided parameters to toolkit workflow template "wf-def"."""

    workflow_name: str
    permission_name: str
    link_title: t.Optional[str]
    link_description: t.Optional[str]
    copyright: CopyrightDefinition  # noqa: A003


class Definition(ToolkitTemplateDefinition):
    """Definition for rendering toolkit workflow template "wf-def"."""

    def __init__(self, dst: Path, params: Parameters):
        # TODO: Validate the values in parameters, e.g.
        # assert "name" in params

        p = params  # alias for shorter access
        permission_name = p.permission_name if p.permission_name else p.workflow_name
        link_title = p.link_title if p.link_title else p.workflow_name
        ui_project_name = p.workflow_name + "_ui"
        # TODO: Limit the symbols allowed in a workflow name!
        js_workflow_name = name_to_js_variable_name(p.workflow_name)

        jinja_params = {
            "workflow_name": p.workflow_name,
            "permission_name": permission_name,
            "link_title": link_title,
            "link_url": f"/{p.workflow_name}",
            "link_description": p.link_description,
            "ui_project_name": ui_project_name,
            "js_workflow_name": js_workflow_name,
            "copyright": p.copyright,
            # TODO: Add supported gateway version
            "gateway_version": "23.2.1",
        }

        super().__init__(
            dst,
            "bluecat_automation_toolkit._internal.templates.wf_def",
            jinja_params,
        )

        self._dir(Path(p.workflow_name))

        for name in (
            "__init__.py",
            "base.py",
            "hooks.py",
            "README.md",
            "routes.py",
            "spec.json",
        ):
            self._jinja_template(
                Path(p.workflow_name, name),
                Path("workflow_name", name),
            )

        self._item(
            license_file.Definition(
                Path(dst, p.workflow_name), license_file.Parameters(p.copyright)
            )
        )
