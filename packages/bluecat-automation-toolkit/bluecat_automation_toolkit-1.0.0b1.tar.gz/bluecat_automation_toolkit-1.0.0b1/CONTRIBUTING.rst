..
    Copyright 2023 BlueCat Networks Inc.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

BlueCat Automation Toolkit Developer instructions
#################################################

There are many ``make`` targets available to facilitate the development and building of
the ``bluecat-automation-toolkit`` package. The ``make`` targets are divided into different files
with respect to their uses.


Setting up DEV environment
**************************

Setting up the development environment is facilitated by make targets in
``infrastructure/venv.mk`` file.

1. Creating virtual environment: This is needed so that the consistent
development environment and package versions can be maintained for particular
repository. Command to create it inside ``./venv`` directory is

    .. code-block:: bash

        make venv-create dir=venv

2. Install python packages that are needed in the final build of the package.
This installs the python packages from ``requirements/build.in`` file.

    .. code-block:: bash

        make venv-install-build-pkg dir=venv

3. Install python packages that are needed for the development, but are not needed in
the final build. This installs the python packages from ``requirements/dev.in`` file.
Before running make command, make sure you are connected to the VPN.

    .. code-block:: bash

        make venv-install-dev-pkg dir=venv


Compile Requirement files
*************************

This step is required only when there is some change in any for the requirement files.
i.e. ``dev.in``, ``build.in``, ``tests.in``, ``lint.in``.
After changes the corresponding hash file needs to be updated.

    * For generating hash file for ``dev.in``:

        .. code-block:: bash

            make compile-dev-pkg dir=venv

    * For generating hash file for ``lint.in``:

        .. code-block:: bash

            pip install pip-tools
            pip-compile --generate-hashes requirements/lint.in

    * For generating hash file for ``build.in``:

        .. code-block:: bash

            pip install pip-tools
            pip-compile --generate-hashes requirements/build.in

    * For generating hash file for ``tests.in``:

        .. code-block:: bash

            pip install pip-tools
            pip-compile --generate-hashes requirements/tests.in


Running tests locally
*********************

To run the tests we have make targets in ``infrastructure/tests.mk`` file

    .. code-block:: bash

        make unit-tests

When writing or updating a toolkit template, or when functionality related to the
rendering of such a template changes, the developer should have to create or update
tests for the rendering result og that template. There is a utility function -
``tests.utils.cmp_snapshot`` - for comparing a snapshot of such rendering result with the
actual one. As a convenient way to create or update snapshots, the function checks for
environment variable ``SAVE_SNAPSHOTS``. If it is present and its value is `1` or `y`,
then the snapshot will be created *before* it is compared. This can be used to easily
create (all) snapshots through a tests run. Note that in that case the comparison is
meaningless and the tests wouldn't fail because of it.


Running lint targets locally
****************************

1. Run ``pylint`` checks

    .. code-block:: bash

        make pylint-check

2. Run ``ruff`` checks

    .. code-block:: bash

        make ruff-check

2. Run ``black`` checks

    .. code-block:: bash

        make black-check


Build package
*************

For building the final package, we have ``infrastructure/build_py_pkg.mk`` file.
Following make targets are available:

1. Build the package. The command clears the previous build and creates a new package
from the source code. This is used in ``post-merge`` pipeline in gitlab-ci

    .. code-block:: bash

        make build

2. Publish the package. This command publishes the built package to
`artifactory <https://gitlab.bluecatlabs.net/dns-integrity/stargate/
automation-toolkit/-/packages>`_ available on gitlab. It uses python module
`twine <https://pypi.org/project/twine/>`_ for achieving this.
This command is used in gitlab-ci pipeline as part of ``release`` make target,
but can be run locally as well, given the appropriate environment variables are set.

    .. code-block:: bash

        make publish

Design Summary
*************

The Click library is utilized to integrate the command line for the toolkit (`src/bluecat_automation_toolkit/cli.py`).

Each workflow incorporates Jinja templates to formulate desired workflows. Within
`src/bluecat_automation_toolkit/internal/templates/`, there are directories for each available workflow that can be
created by the tool. The `wf_dev` directory contains the most basic files and the definition file,
`src/bluecat_automation_toolkit/_internal/templates/wf_def/__init__.py`, required to create a basic workflow.

Other workflows have a `definition.py` file with their own required structure to generate the workflow from the command.
Each template folder has its own template files, which are modified by their respective definition files to
achieve the desired outcome (minimal, minimal-ui, single-form) with or without localization.
