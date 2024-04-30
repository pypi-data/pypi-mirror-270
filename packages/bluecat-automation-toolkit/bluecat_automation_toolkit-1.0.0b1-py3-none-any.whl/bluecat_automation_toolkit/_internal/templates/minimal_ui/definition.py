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
"""Definitions and resources for toolkit internal template "minimal_ui"."""
# pylint: disable=fixme
# pylint: disable=R0801, R0914
import typing as t
from dataclasses import dataclass
from pathlib import Path

from bluecat_automation_toolkit._internal.cli import CopyrightDefinition
from bluecat_automation_toolkit._internal.output import (
    ToolkitTemplateDefinition,
    name_to_js_variable_name,
)
from bluecat_automation_toolkit._internal.templates.minimal import definition as minimal


@dataclass(init=True, frozen=True)
class Parameters:
    """User-provided parameters to toolkit workflow template "single-form"."""

    workflow_name: str
    permission_name: str
    link_title: t.Optional[str]
    link_description: t.Optional[str]
    languages: t.Iterable[str]
    copyright: CopyrightDefinition  # noqa: A003

    def to_minimal_param(self) -> minimal.Parameters:
        """Converts Parameters to minimal template Parameters."""
        return minimal.Parameters(
            workflow_name=self.workflow_name,
            permission_name=self.permission_name,
            link_title=self.link_title,
            link_description=self.link_description,
            copyright=self.copyright,
        )


class Definition(ToolkitTemplateDefinition):
    """Definition for rendering toolkit workflow template "minimal_ui"."""

    def __init__(self, dst: Path, params: Parameters):
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

        jinja_params: dict = {
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
            "bluecat_automation_toolkit._internal.templates.minimal_ui",
            jinja_params,
        )
        min_def = minimal.Definition(dst, p.to_minimal_param())
        self._item(min_def)

        ui_project_name = jinja_params["ui_project_name"]
        js_workflow_name = jinja_params["js_workflow_name"]

        self._remove(Path(dst, ".gitignore"))
        self._jinja_template(Path(".gitignore"), src=Path(".gitignore"))

        self._remove(Path(dst, "Makefile"))
        self._jinja_template(Path("Makefile"), src=Path("Makefile"))

        self._remove(Path(dst, "workspace", "workflows", p.workflow_name, "routes.py"))
        self._jinja_template(
            Path("workspace", "workflows", p.workflow_name, "routes.py"),
            src=Path("workspace", "workflows", "ui_workflow_name", "routes.py"),
        )
        # replace items from min_def

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
            self._remove(Path(dst, "workspace", "config.py.sample"))
            self._jinja_template(
                Path("workspace", "config.py.sample"),
                Path("workspace", "config.py.sample"),
            )  # TODO: test replace config.py with localized version

        self._jinja_template(
            Path("projects", p.workflow_name, ui_project_name, "src", "index.html"),
            Path(
                "projects",
                "workflow_name",
                "ui_project_name",
                "src",
                "index.html",
            ),
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
        self._dir(Path("projects", p.workflow_name, ui_project_name, "src", "hooks"))
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

        for name in ("App.js", "App.less", "index.js"):
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
