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
# pylint: disable=line-too-long;  Let the code style tool handle it.
# pylint: disable=duplicate-code; Short line length and common dir paths trigger this easily.
# pylint: disable=fixme; This is a POC.
"""Definitions of the template for rendering a single-form workflow."""
import typing as t
from dataclasses import dataclass
from pathlib import Path

from bluecat_automation_toolkit._internal.cli import CopyrightDefinition
from bluecat_automation_toolkit._internal.output import (
    ToolkitTemplateDefinition,
    name_to_js_variable_name,
)


@dataclass(init=True, frozen=True)
class Parameters:
    """User-provided parameters to toolkit workflow template "single-form"."""

    workflow_name: str
    permission_name: str
    link_title: t.Optional[str]
    link_description: t.Optional[str]
    languages: t.Iterable[str]
    copyright: CopyrightDefinition  # noqa: A003


class Definition(ToolkitTemplateDefinition):
    """Definition for rendering toolkit workflow template "single-form"."""

    def __init__(self, dst: Path, params: Parameters):  # noqa: C901
        # TODO: Validate the values in parameters, e.g.
        # assert "name" in params

        p = params  # alias for shorter access
        permission_name = p.permission_name if p.permission_name else p.workflow_name
        link_title = p.link_title if p.link_title else p.workflow_name
        ui_project_name = p.workflow_name + "_ui"
        # TODO: Limit the symbols allowed in a workflow name!
        js_workflow_name = name_to_js_variable_name(p.workflow_name)
        # The received languages are in form of a tuple, converting it to a list.
        languages = list(p.languages)
        is_localized = bool(languages)
        default_language = languages[0] if is_localized else None

        jinja_params = {
            "workflow_name": p.workflow_name,
            "permission_name": permission_name,
            "link_title": link_title,
            "link_url": f"/{p.workflow_name}",
            "link_description": p.link_description,
            "is_localized": is_localized,
            "languages": languages,
            "current_language": None,
            "default_language": default_language,
            "ui_project_name": ui_project_name,
            "js_workflow_name": js_workflow_name,
            "copyright": p.copyright,
            # TODO: Add supported gateway version
            "gateway_version": "23.2.1",
        }

        super().__init__(
            dst,
            "bluecat_automation_toolkit._internal.templates.single_form",
            jinja_params,
        )

        for name in (".dockerignore", ".gitignore", "Dockerfile", "Makefile"):
            self._jinja_template(Path(name), src=Path(name))

        # TODO: Add generating a README.rst file at the root of the output.

        self._dir(Path("logs"))

        self._dir(Path("projects"))
        self._dir(Path("projects", p.workflow_name))
        for name in ("Makefile", "README.md"):
            self._jinja_template(
                Path("projects", p.workflow_name, name),
                Path("projects", "workflow_name", name),
            )

        self._dir(Path("projects", p.workflow_name, ui_project_name))
        for name in (
            ".eslintrc.js",
            ".prettierrc",
            "babel.config.js",
            "package.json",
            "package-lock.json",
            "webpack.config.js",
        ):
            self._jinja_template(
                Path("projects", p.workflow_name, ui_project_name, name),
                Path("projects", "workflow_name", "ui_project_name", name),
            )
        self._dir(Path("projects", p.workflow_name, ui_project_name, "src"))
        self._jinja_template(
            Path("projects", p.workflow_name, ui_project_name, "src", "index.html"),
            Path("projects", "workflow_name", "ui_project_name", "src", "index.html"),
        )

        self._dir(Path("projects", p.workflow_name, ui_project_name, "src", "assets"))
        self._dir(
            Path("projects", p.workflow_name, ui_project_name, "src", "assets", "images")
        )
        self._resource(
            Path(
                "projects",
                p.workflow_name,
                ui_project_name,
                "src",
                "assets",
                "images",
                "bluecat-icon.png",
            ),
            Path(
                "projects",
                "workflow_name",
                "ui_project_name",
                "src",
                "assets",
                "images",
                "bluecat-icon.png",
            ),
        )

        self._dir(Path("projects", p.workflow_name, ui_project_name, "src", "components"))
        for name in ("FormComboBoxField.js", "FormComboBoxField.less"):
            self._jinja_template(
                Path(
                    "projects",
                    p.workflow_name,
                    ui_project_name,
                    "src",
                    "components",
                    name,
                ),
                Path(
                    "projects",
                    "workflow_name",
                    "ui_project_name",
                    "src",
                    "components",
                    name,
                ),
            )

        if is_localized:
            self._dir(
                Path("projects", p.workflow_name, ui_project_name, "src", "functions")
            )
            self._jinja_template(
                Path(
                    "projects",
                    p.workflow_name,
                    ui_project_name,
                    "src",
                    "functions",
                    "setLanguage.js",
                ),
                Path(
                    "projects",
                    "workflow_name",
                    "ui_project_name",
                    "src",
                    "functions",
                    "setLanguage.js",
                ),
            )

        self._dir(Path("projects", p.workflow_name, ui_project_name, "src", "hooks"))
        for name in ("useObjectSuggestions.js",):
            self._jinja_template(
                Path("projects", p.workflow_name, ui_project_name, "src", "hooks", name),
                Path(
                    "projects", "workflow_name", "ui_project_name", "src", "hooks", name
                ),
            )

        if is_localized:
            self._dir(Path("projects", p.workflow_name, ui_project_name, "src", "l10n"))
            self._jinja_template(
                Path(
                    "projects",
                    p.workflow_name,
                    ui_project_name,
                    "src",
                    "l10n",
                    "index.js",
                ),
                Path(
                    "projects",
                    "workflow_name",
                    "ui_project_name",
                    "src",
                    "l10n",
                    "index.js",
                ),
            )
            for language in languages:
                extra_params = {"current_language": language}

                self._jinja_template(
                    Path(
                        "projects",
                        p.workflow_name,
                        ui_project_name,
                        "src",
                        "l10n",
                        language + ".po",
                    ),
                    Path(
                        "projects",
                        "workflow_name",
                        "ui_project_name",
                        "src",
                        "l10n",
                        "language.po",
                    ),
                    extra_params,
                )

        self._dir(Path("projects", p.workflow_name, ui_project_name, "src", "pages"))
        self._dir(
            Path(
                "projects",
                p.workflow_name,
                ui_project_name,
                "src",
                "pages",
                js_workflow_name,
            )
        )
        for name in ("App.js", "App.less", "FormFields.js", "index.js"):
            self._jinja_template(
                Path(
                    "projects",
                    p.workflow_name,
                    ui_project_name,
                    "src",
                    "pages",
                    js_workflow_name,
                    name,
                ),
                Path(
                    "projects",
                    "workflow_name",
                    "ui_project_name",
                    "src",
                    "pages",
                    "js_workflow_name",
                    name,
                ),
            )

        self._dir(Path("workspace"))
        for name in ("config.json.sample", "config.py.sample", "permissions.json.sample"):
            self._jinja_template(Path("workspace", name), Path("workspace", name))

        self._dir(Path("workspace", "workflows"))
        self._jinja_template(
            Path("workspace", "workflows", "__init__.py"),
            Path("workspace", "workflows", "__init__.py"),
        )

        self._dir(Path("workspace", "workflows", p.workflow_name))
        for name in (
            "__init__.py",
            "base.py",
            "hooks.py",
            "routes.py",
            "spec.json",
        ):
            self._jinja_template(
                Path("workspace", "workflows", p.workflow_name, name),
                Path("workspace", "workflows", "workflow_name", name),
            )
