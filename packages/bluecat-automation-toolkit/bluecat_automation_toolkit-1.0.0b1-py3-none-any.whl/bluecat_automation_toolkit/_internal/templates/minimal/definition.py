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
"""Definitions and resources for toolkit internal template "minimal"."""
# pylint: disable=line-too-long;  Let the code style tool handle it.
# pylint: disable=duplicate-code; Short line length and common dir paths trigger this easily.
# pylint: disable=fixme
import typing as t
from dataclasses import dataclass
from pathlib import Path

from bluecat_automation_toolkit._internal.cli import CopyrightDefinition
from bluecat_automation_toolkit._internal.output import (
    ToolkitTemplateDefinition,
    name_to_js_variable_name,
)
from bluecat_automation_toolkit._internal.templates import wf_def


@dataclass(init=True, frozen=True)
class Parameters:
    """User-provided parameters to toolkit workflow template "minimal"."""

    workflow_name: str
    permission_name: str
    link_title: t.Optional[str]
    link_description: t.Optional[str]
    copyright: CopyrightDefinition  # noqa: A003


class Definition(ToolkitTemplateDefinition):
    """Definition for rendering toolkit workflow template "minimal"."""

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
            "bluecat_automation_toolkit._internal.templates.minimal",
            jinja_params,
        )

        for name in (".dockerignore", ".gitignore", "Dockerfile", "Makefile"):
            self._jinja_template(Path(name), src=Path(name))

        self._dir(Path("logs"))

        self._dir(Path("workspace"))

        for name in ("config.json.sample", "config.py.sample", "permissions.json.sample"):
            self._jinja_template(Path("workspace", name), Path("workspace", name))

        self._dir(Path("workspace", "workflows"))
        self._jinja_template(
            Path("workspace", "workflows", "__init__.py"),
            Path("workspace", "workflows", "__init__.py"),
        )

        self._item(
            wf_def.Definition(
                dst=Path(dst, "workspace", "workflows"),
                params=wf_def.Parameters(
                    workflow_name=p.workflow_name,
                    permission_name=p.permission_name,
                    link_title=p.link_title,
                    link_description=p.link_description,
                    copyright=p.copyright,
                ),
            )
        )
