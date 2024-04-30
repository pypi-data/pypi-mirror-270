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

# pylint: disable=redefined-builtin
# pylint: disable=import-outside-toplevel
# pylint: disable=duplicate-code; Common parameters' handling across commands.
# pylint: disable=R0913; CLI commands have many options.
# ruff: noqa: PLR0913; CLI commands have many options.
# mypy: disable-error-code="return"
"""CLI commands of the BlueCat Automation Toolkit."""
from __future__ import annotations

import platform
import typing as t
from pathlib import Path

import click

from . import __version__
from ._internal.cli import (
    copyright_options,
    l10n_options,
    process_copyright_options,
    workflow_new_common_options,
)


@click.group
@click.version_option(
    __version__,
    message=f"Python {platform.python_version()}\nbluecat-automation-toolkit %(version)s",
)
def cli() -> t.Optional[t.Any]:
    """
    The BlueCat Automation Toolkit lets users effortlessly generate workflows
    for BlueCat Gateway. You can easily customize these workflows to align with your
    specific design requirements. Workflows you can build with this toolkit range from
    simple, fundamental workflows, to more advanced ones with a UI that seamlessly
    integrates with BAM.
    """


@click.group
def workflow() -> t.Optional[t.Any]:
    """Operate with a workflow."""


cli.add_command(workflow)


@click.group(name="new")
def new() -> t.Optional[t.Any]:
    """Create a new workflow."""


workflow.add_command(new)


@click.command(name="minimal")
@workflow_new_common_options
@copyright_options
@click.pass_context
def minimal(
    ctx: click.core.Context,
    name: str,
    output: str,
    permission: str,
    link_title: str,
    link_description: str,
    copyright_license: str,
    copyright_name: str,
    copyright_year: str,
) -> t.Optional[t.Any]:
    """
    Create a new basic workflow with no user interface.
    Generate a dedicated workspace for running the Gateway workflow.
    Create files in output root that help run workflow from this workspace.
    """
    if output is None:
        output = Path.cwd()
        click.echo("Using the current working directory for output.")
    dst_path = Path(output)

    # NOTE: For temporary debugging purposes only.
    click.echo(f"DEBUG: output: {dst_path!r}")
    click.echo(f"DEBUG: name: {name!r}")
    click.echo(f"DEBUG: permission: {permission!r}")
    click.echo(f"DEBUG: link_title: {link_title!r}")
    click.echo(f"DEBUG: link_description: {link_description!r}")
    click.echo(f"DEBUG: copyright_license: {copyright_license!r}")
    click.echo(f"DEBUG: copyright_name: {copyright_name!r}")
    click.echo(f"DEBUG: copyright_year: {copyright_year!r}")
    click.echo("Creating a new workflow from the 'minimal' template.")

    from bluecat_automation_toolkit._internal.templates.minimal.definition import (
        Definition,
        Parameters,
    )

    params = Parameters(
        workflow_name=name,
        permission_name=permission,
        link_title=link_title,
        link_description=link_description,
        copyright=process_copyright_options(
            copyright_license, copyright_name, copyright_year
        ),
    )
    d = Definition(dst_path, params)
    ctx.exit(d.render())


new.add_command(minimal)


@click.command(name="minimal-ui")
@workflow_new_common_options
@copyright_options
@l10n_options
@click.pass_context
def minimal_ui(  # pylint: disable=R0913;
    ctx: click.core.Context,
    name: str,
    output: str,
    permission: str,
    link_title: str,
    link_description: str,
    language: list,
    copyright_license: str,
    copyright_name: str,
    copyright_year: str,
) -> t.Optional[t.Any]:
    """
    Create a new basic workflow with a user interface.
    Generate a dedicated workspace for running the Gateway workflow with
    basic UI elements with localization options.
    Create files in output root that help run workflow from this workspace.
    """
    if output is None:
        output = Path.cwd()
        click.echo("Using the current working directory for output.")
    dst_path = Path(output)

    # NOTE: For temporary debugging purposes only.
    click.echo(f"DEBUG: output: {dst_path!r}")
    click.echo(f"DEBUG: name: {name!r}")
    click.echo(f"DEBUG: permission: {permission!r}")
    click.echo(f"DEBUG: link_title: {link_title!r}")
    click.echo(f"DEBUG: link_description: {link_description!r}")
    click.echo(f"DEBUG: languages: {language!r}")
    click.echo(f"DEBUG: copyright_license: {copyright_license!r}")
    click.echo(f"DEBUG: copyright_name: {copyright_name!r}")
    click.echo(f"DEBUG: copyright_year: {copyright_year!r}")
    click.echo("Creating a new workflow from the 'minimal-ui' template.")

    from bluecat_automation_toolkit._internal.templates.minimal_ui.definition import (
        Definition,
        Parameters,
    )

    params = Parameters(
        workflow_name=name,
        permission_name=permission,
        link_title=link_title,
        link_description=link_description,
        languages=language,
        copyright=process_copyright_options(
            copyright_license, copyright_name, copyright_year
        ),
    )

    d = Definition(dst_path, params)
    ctx.exit(d.render())


new.add_command(minimal_ui)


@click.command("single-form")
@workflow_new_common_options
@copyright_options
@l10n_options
@click.pass_context
def single_form(
    ctx: click.core.Context,
    name: str,
    output: str,
    permission: str,
    link_title: str,
    link_description: str,
    language: list,
    copyright_license: str,
    copyright_name: str,
    copyright_year: str,
) -> t.Optional[t.Any]:
    """
    Create a new  workflow with a single form user interface.
    Generate a dedicated workspace for running the Gateway workflow
    with example workflow UI with localization options.
    Enable user to be able to add text resource record to BAM using this UI.
    Create files in output root that help run workflow from this workspace.
    """
    click.echo("Creating a new workflow from the 'single-form' template.")
    if output is None:
        output = Path.cwd()
        click.echo("Using the current working directory for output.")
    dst_path = Path(output)

    # NOTE: For temporary debugging purposes only.
    click.echo(f"DEBUG: output: {dst_path!r}")
    click.echo(f"DEBUG: name: {name!r}")
    click.echo(f"DEBUG: permission: {permission!r}")
    click.echo(f"DEBUG: link_title: {link_title!r}")
    click.echo(f"DEBUG: languages: {language!r}")
    click.echo(f"DEBUG: link_description: {link_description!r}")
    click.echo(f"DEBUG: copyright_license: {copyright_license!r}")
    click.echo(f"DEBUG: copyright_name: {copyright_name!r}")
    click.echo(f"DEBUG: copyright_year: {copyright_year!r}")

    from bluecat_automation_toolkit._internal.templates.single_form.definition import (
        Definition,
        Parameters,
    )

    params = Parameters(
        workflow_name=name,
        permission_name=permission,
        link_title=link_title,
        link_description=link_description,
        languages=language,
        copyright=process_copyright_options(
            copyright_license, copyright_name, copyright_year
        ),
    )
    d = Definition(dst_path, params)
    ctx.exit(d.render())


new.add_command(single_form)
