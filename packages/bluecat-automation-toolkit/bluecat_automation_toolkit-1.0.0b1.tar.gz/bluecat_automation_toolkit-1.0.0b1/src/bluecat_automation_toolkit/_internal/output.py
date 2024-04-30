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
# pylint: disable=line-too-long; Let the code style tool handle it.
"""Definitions of the template for rendering a single-form workflow."""
import copy
import errno
import importlib.resources
import string
import sys
import traceback
import typing as t
from importlib.abc import Traversable
from pathlib import Path

from jinja2 import (
    BaseLoader,
    ChoiceLoader,
    Environment,
    PackageLoader,
    StrictUndefined,
    select_autoescape,
)

from bluecat_automation_toolkit._internal.copyrights import copyright_notice


def _error(_msg: str) -> None:
    print(f"{_msg}", file=sys.stderr)


class ItemBase:
    """A base class for a filesystem item to be created."""

    def __init__(self, dst: Path):
        self.dst = dst

    def render(self) -> int:
        """Create the expected item at the destination."""
        raise NotImplementedError


class Directory(ItemBase):
    """A directory should be created."""

    def render(self) -> int:
        """Create the defined directory."""
        if self.dst.exists():
            _error(f"WARNING: {self.dst}: Directory already exists.")
            # show error, still assign exit status = 0
        self.dst.mkdir(exist_ok=True)
        return 0


class File(ItemBase):
    """A base class for when a file should be created."""

    def render(self) -> int:
        if self.dst.exists():
            _error(f"ERROR: {self.dst}: File already exists. New file not created.")
            return errno.EEXIST
        return 0


class FileFromCallable(File):
    """A file should be created from the result of a callable."""

    def __init__(
        self, dst: Path, func: t.Callable[[], t.Optional[str]], create_empty: bool = False
    ):
        super().__init__(dst)
        self.func = func
        self.create_empty = create_empty

    def render(self) -> int:
        """Create the defined file."""
        rv = super().render()
        if rv:
            return rv

        content = self.func()
        if not content and not self.create_empty:
            # _error(
            #     f"WARNING: {self.dst}: The file was not created,"
            #     " because it would have been empty."
            # )
            return 0

        self.dst.write_text(content if content else "")
        return 0


class FileFromResource(File):
    """A file should be created from a static resource, one that does not change."""

    def __init__(
        self,
        dst: Path,
        src: Path,
        res_root: importlib.abc.Traversable,
    ):
        super().__init__(dst)
        self.src = src
        self.res_root = res_root

    def render(self) -> int:
        """Create the defined file."""
        rv = super().render()
        if rv:
            return rv

        # To avoid `self.res_root / self.src` which causes a MyPy error, go through each
        # part of the relative source path one at a time to build the full source path.
        # The MyPy error was: Unsupported operand types for / ("Traversable" and "Path")
        src = self.res_root
        for part in self.src.parts:
            src = src / part

        self.dst.write_bytes(src.read_bytes())
        return 0


class FileFromTemplate(File):
    """A file should be created from a Jinja template."""

    def __init__(
        self, dst: Path, src: Path, jinja_env: Environment, jinja_params: dict[str, t.Any]
    ):
        super().__init__(dst)
        self.src = str(src)
        self.jinja_env = jinja_env
        self.jinja_params = jinja_params

    def render(self) -> int:
        """Create the defined file."""
        rv = super().render()
        if rv:
            return rv

        tmpl = self.jinja_env.get_template(
            self.src,
            globals={
                "copyright_notice": copyright_notice,
            },
        )
        text = tmpl.render(self.jinja_params)
        self.dst.write_text(text)
        return 0


class ToolkitTemplateDefinition(ItemBase):
    """
    A collection of directories and files to be created, considered as a single template.
    """

    _resources_root: t.Optional[Traversable]
    _jinja_env: t.Optional[Environment]
    _jinja_params: t.Optional[dict[str, t.Any]]

    def __init__(
        self,
        dst: Path,
        tk_template_pkg: t.Optional[str] = None,
        jinja_params: t.Optional[dict[str, t.Any]] = None,
    ) -> None:
        super().__init__(dst)
        self._items: list[ItemBase] = []
        if tk_template_pkg:
            self._resources_root = get_pkg_resources_root(tk_template_pkg)
            self._jinja_env = get_jinja_environment(tk_template_pkg)
            self._jinja_params = jinja_params

    def _callable(
        self, dst: Path, func: t.Callable[[], t.Optional[str]], create_empty: bool = False
    ) -> None:
        """Add a file to be generated."""
        self._items.append(
            FileFromCallable(dst=self.dst / dst, func=func, create_empty=create_empty)
        )

    def _dir(self, dst: Path) -> None:
        """Add a directory to be created."""
        self._items.append(Directory(dst=self.dst / dst))

    def _item(self, item: ItemBase) -> None:
        """
        Add an item to the list of things to render. No adjustments are made to the
        item's destination path, in contrast to how it is done for other specific ones.
        """
        self._items.append(item)

    def _remove(self, dst: Path) -> None:
        """
        removes a file previously added by the automation-toolkit from the list of things to render.
        item is selected by target file path, that is, the location the file was to be written to.
        """
        for item in self._items:
            if isinstance(item, ToolkitTemplateDefinition):
                item._remove(dst)  # noqa: SLF001; # pylint: disable=W0212
                continue  # recursively remove the path, but do not remove any ToolkitTemplateDefinition items
            if item.dst == dst:
                self._items.remove(item)

    def _jinja_template(
        self, dst: Path, src: Path, extra_params: t.Optional[dict] = None
    ) -> None:
        """Add a Jinja template to be rendered."""
        if self._jinja_env is None:
            raise Exception(
                "Cannot add a Jinja template when the template package is not specified."
            )
        if self._jinja_params is None:
            raise Exception(
                "Cannot add a Jinja template when the Jinja parameters are not specified."
            )
        if extra_params is None:
            jinja_params = self._jinja_params
        else:
            jinja_params = copy.deepcopy(self._jinja_params)
            jinja_params.update(extra_params)
        self._items.append(
            FileFromTemplate(
                dst=self.dst / dst,
                src=src,
                jinja_env=self._jinja_env,
                jinja_params=jinja_params,
            )
        )

    def _resource(self, dst: Path, src: Path) -> None:
        """Add a resource file to be copied."""
        if self._resources_root is None:
            raise Exception(
                "Cannot add a resource when the template package is not specified."
            )
        self._items.append(
            FileFromResource(
                dst=self.dst / dst,
                src=src,
                res_root=self._resources_root,
            )
        )

    def render(self) -> int:
        """Create the defined directories and files."""
        self.dst.mkdir(parents=True, exist_ok=True)
        exit_codes = []
        for item in self._items:
            try:
                exit_codes.append(item.render())
            except Exception as exc:  # noqa: PERF203
                _error(f"ERROR: {item.dst}: Item failed to render: {exc}")
                traceback.print_exc()
                exit_codes.append(1)
        exit_codes = [abs(code) for code in exit_codes if code]
        return min(exit_codes) if exit_codes else 0


class PrependTemplateLoader(BaseLoader):
    """
    Loader that will attach a specified template's source at the beginning of every
    each requested template.
    """

    def __init__(self, actual_loader: BaseLoader, template_name: str):
        self._actual_loader = actual_loader
        self._template_name = template_name

    def get_source(
        self, environment: Environment, template: str
    ) -> tuple[str, t.Optional[str], t.Optional[t.Callable[[], bool]]]:
        """Get the source of a template."""
        prepend_source, _, prepend_uptodate = self._actual_loader.get_source(
            environment, self._template_name
        )
        if prepend_uptodate is None:
            # pylint: disable=unnecessary-lambda-assignment; Keep it simple.
            prepend_uptodate = lambda: False  # noqa: E731

        source, filename, uptodate = self._actual_loader.get_source(environment, template)
        if uptodate is None:
            # pylint: disable=unnecessary-lambda-assignment; Keep it simple.
            uptodate = lambda: False  # noqa: E731

        def _uptodate() -> bool:
            return prepend_uptodate() and uptodate()

        return prepend_source.strip() + source, filename, _uptodate

    def list_templates(self) -> list[str]:
        """Return a list of available templates."""
        return self._actual_loader.list_templates()


def get_jinja_environment(tk_template_pkg: str) -> Environment:
    """Return a Jinja environment that can be used to render Jinja templates."""
    return Environment(
        loader=PrependTemplateLoader(
            ChoiceLoader(
                [
                    PackageLoader(
                        "bluecat_automation_toolkit._internal", "jinja_templates"
                    ),
                    PackageLoader(tk_template_pkg, "files"),
                ]
            ),
            "_autoloaded.html",
        ),
        autoescape=select_autoescape(),
        undefined=StrictUndefined,
    )


def get_pkg_resources_root(tk_template_pkg: str) -> Traversable:
    """Return a traversable root for locating package resources."""
    return importlib.resources.files(tk_template_pkg) / "files"


def name_to_js_class_name(value: str) -> str:
    """Convert a value to the PascalCase of a JS class name."""
    value = value.replace("_", " ").replace("-", " ")
    return string.capwords(value).replace(" ", "")


def name_to_js_variable_name(value: str) -> str:
    """Convert a value to the camelCase of a JS variable name."""
    value = value.replace("_", " ").replace("-", " ")
    value = string.capwords(value).replace(" ", "")
    if not value:
        return value
    # Make the first character lowercase.
    return value[0].lower() + value[1:]


def name_to_link_text(value: str) -> str:
    """Convert a value to sentence case as expected for a link's text."""
    return value.replace("_", " ").replace("-", " ").capitalize()
