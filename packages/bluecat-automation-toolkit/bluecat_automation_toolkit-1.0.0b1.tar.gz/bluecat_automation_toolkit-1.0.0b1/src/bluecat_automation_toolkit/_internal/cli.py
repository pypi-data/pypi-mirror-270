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
"""CLI commands of the workflow toolkit."""
from __future__ import annotations

import datetime
import os
import re
import typing as t

import click

from .copyrights import CopyrightDefinition

# region Copyright


def validate_copyright_name(param: click.Parameter, value: str) -> str:
    """
    Ensure copyright_name parameter does not contain a newline.
    """
    if value and "\n" in value:
        msg = "Copyright name cannot contain newline."
        raise click.BadParameter(message=msg, param=param)
    return value


def validate_copyright_year(param: click.Parameter, value: str) -> str:
    """
    Ensure copyright_year parameter does not contain a newline.
    """
    if value and "\n" in value:
        msg = "Copyright year cannot contain newline."
        raise click.BadParameter(message=msg, param=param)
    return value


def copyright_options(_func: t.Optional[t.Callable] = None) -> t.Callable:
    """
    Add the standard copyright-related options to a command.

    .. note::

        Can be used as both ``@copyright_options`` and ``@copyright_options()``.

    .. versionadded:: 24.2.0
    """

    def decorator(func: t.Callable) -> t.Callable:
        for o in (
            click.Option(
                ["--copyright-license", "--cl"],
                help="The license to put in the copyright notice in the created files.",
                type=click.Choice(["proprietary", "apache2", "mit", "none"]),
                default="none",
            ),
            click.Option(
                ["--copyright-name", "--cn"],
                help="The name of the copyright owner.",
                callback=lambda _, param, value: validate_copyright_name(param, value),
            ),
            click.Option(
                ["--copyright-year", "--cy"],
                help=(
                    "The year to use in the copyright notice."
                    " Defaults to the current year."
                ),
                callback=lambda _, param, value: validate_copyright_year(param, value),
            ),
            click.Option(
                ["--no-copyright", "copyright_license"],
                help=(
                    "An alternative way to specify to not include any copyright notice."
                    " Equivalent to '--copyright-license none'."
                ),
                flag_value="none",
            ),
        ):
            # NOTE: Using `click`'s internals to achieve fluid use of decorator.
            # pylint: disable=protected-access
            click.decorators._param_memo(func, o)  # noqa: SLF001

        return func

    if _func is None:
        return decorator

    return decorator(_func)


def process_copyright_options(
    copyright_license: str, copyright_name: str, copyright_year: str
) -> CopyrightDefinition:
    """
    Process the values for copyright-related options passed via the CLI before they
    are used by a command.
    """
    if copyright_license == "none":
        return CopyrightDefinition("", "", "")  # no copyright

    if not copyright_name:
        copyright_name = ""
    if not copyright_year:
        copyright_year = str(datetime.datetime.now().year)  # noqa: DTZ005

    return CopyrightDefinition(
        license=copyright_license,
        owner_name=copyright_name,
        year=copyright_year,
    )


# endregion Copyright
# region Common "workflow new" options


def validate_name(param: click.Parameter, value: str) -> str:
    """
    Ensure workflow name is of proper format.
    - Must start with a letter or an underscore.
    - Must consist only of letters, underscores, and numbers.
    - Must not be left blank.
    - Must not contain newline.
    """
    if value:
        if not re.fullmatch("[a-zA-Z_][a-zA-Z0-9_]*", value):
            msg = (
                "Workflow name must start with a letter or _. "
                "Workflow name must consist only of letters, _, and numbers."
            )
            raise click.BadParameter(
                message=msg,
                param=param,
            )
    else:
        msg = "Workflow name cannot be blank."
        raise click.BadParameter(message=msg, param=param)
    return value


def validate_output(param: click.Parameter, value: str) -> str:
    """
    Ensure output path of workflow is valid.
    If path provided already exists, ensure it is a directory.
    """
    if value and os.path.exists(value) and not os.path.isdir(value):
        msg = "Output path must be a directory."
        raise click.BadParameter(message=msg, param=param)
    return value


def validate_permission(param: click.Parameter, value: str) -> str:
    """
    Ensure permission name does not contain a newline.
    """
    if value and "\n" in value:
        msg = "Permission name cannot contain newline."
        raise click.BadParameter(message=msg, param=param)
    return value


def validate_link_title(param: click.Parameter, value: str) -> str:
    """
    Ensure link title does not contain a newline.
    """
    if value and "\n" in value:
        msg = "Link title cannot contain newline."
        raise click.BadParameter(message=msg, param=param)
    return value


def workflow_new_common_options(_func: t.Optional[t.Callable] = None) -> t.Callable:
    """
    Add the common options to a "workflow new" template command.

    .. note::

        Can be used as both ``@workflow_new_common_options`` and
        ``@workflow_new_common_options()``.

    .. versionadded:: 24.2.0
    """

    def decorator(func: t.Callable) -> t.Callable:
        for o in (
            click.Option(
                ["--name", "-n"],
                required=True,
                help="Name of the created workflow.",
                callback=lambda _, param, value: validate_name(param, value),
            ),
            click.Option(
                ["--output", "-o"],
                type=click.Path(),
                help="Path to the directory to place the output in.",
                callback=lambda _, param, value: validate_output(param, value),
            ),
            click.Option(
                ["--permission", "-p"],
                help="Name of the permission to be required by the workflow.",
                callback=lambda _, param, value: validate_permission(param, value),
            ),
            click.Option(
                ["--link-title"],
                help="Text to display for the link to the workflow's page.",
                callback=lambda _, param, value: validate_link_title(param, value),
            ),
            click.Option(
                ["--link-description"],
                help="Description for the link to the workflow's page.",
            ),
        ):
            # NOTE: Using `click`'s internals to achieve fluid use of decorator.
            # pylint: disable=protected-access
            click.decorators._param_memo(func, o)  # noqa: SLF001

        return func

    if _func is None:
        return decorator

    return decorator(_func)


# endregion Common "workflow new" options
# region "l10n" options


def validate_language(param: click.Parameter, value: str) -> str:
    """
    Ensure language does not contain a newline.
    """
    if value and "\n" in value:
        msg = "Language cannot contain newline."
        raise click.BadParameter(message=msg, param=param)
    return value


def l10n_options(_func: t.Optional[t.Callable] = None) -> t.Callable:
    """
    Add the localization options to a "workflow new" template command.

    .. note::

        Can be used as both ``@l10n_options`` and
        ``@l10n_options()``.

    .. versionadded:: 24.2.0
    """

    def decorator(func: t.Callable) -> t.Callable:
        for o in (
            click.Option(
                ["--language", "-l"],
                multiple=True,
                default=[],
                help="Languages to be supported by the workflow.",
                callback=lambda _, param, value: validate_language(param, value),
            ),
        ):
            # NOTE: Using `click`'s internals to achieve fluid use of decorator.
            # pylint: disable=protected-access
            click.decorators._param_memo(func, o)  # noqa: SLF001

        return func

    if _func is None:
        return decorator

    return decorator(_func)


# endregion "l10n"
