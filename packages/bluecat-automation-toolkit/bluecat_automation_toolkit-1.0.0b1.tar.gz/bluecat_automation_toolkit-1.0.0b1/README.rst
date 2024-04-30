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


***************************
BlueCat Automation Toolkit
***************************

.. contents:: Table of Contents


Requirements
=================

- Gateway 24.2.0+
- Address Manager 9.5.0+


Description
=================

The BlueCat Automation Toolkit lets you generate BlueCat Gateway workflows quickly and easily.
You can then customize these workflows to fit your specific design requirements.
With this toolkit, you can build both simple, basic workflows and advanced workflows
with a UI that seamlessly integrate with BlueCat Address Manager (BAM).

**Note:** This is an early beta version of the toolkit. BlueCat does not provide support for this software package.



Available commands
===================

Commands that are available on this tookit are shown below.

Create a minimal workflow
---------------------------------------------

.. code-block:: bash

    atk workflow new minimal --name minimal_wf

This command creates a baseline workflow to kickstart your project. It gives you the freedom to
choose any framework to render your workflow's UI. It creates essential files and directories in the primary
output directory, including the `Makefile`, `Dockerfile`, `workspace` directory, and gateway `logs` directory.
Commands in the Makefile build a Docker image and configure the workflow to run on a Gateway Docker
Container. The Dockerfile copies needed files into the workflow, running them using the specified Gateway
image from Quay. The workspace directory contains the new workflow's directory, workflow permissions,
configuration files, and other fundamental components for the new workflow. It also contains route files for
UI rendering and API requests.

To run the workflow right after you create it, follow the instructions below:

1. In the output directory, modify ``workspace/config.py.sample`` to reflect your BAM.
    - Rename this file as `config.py` when you're done.
2. Run the following commands:-
    .. code-block:: bash

        make build
        make run

This runs a docker containerized instance of Gateway with your workflow. Depending on your system needs,
you might have to modify the `run` portion of the Makefile.


Create a minimal user-interface workflow
---------------------------------------------
.. code-block:: bash

    atk workflow new minimal-ui --name minimal_ui_wf

This command creates a new baseline workflow to kickstart your project, also including essential front-end UI files in
the `projects` directory. This command uses React UI to demonstrate workflows with UIs. The projects directory
includes Babel for transpiling Javascript, and Webpack for bundling front-end files. The projects directory also
contains a `Makefile` that runs npm to build and install all packages needed for the UI front-end. You can isolate
the npm action to run from the projects directory, or run them from the Makefile from within the main output
directory. Since this workflow contains front-end ui files, you will be able to navigate to the page to view the
default rendering of the contents of the `App.js` file.

To run the workflow right after you create it, follow the instructions below:

1. In the output directory, modify ``workspace/config.py.sample`` to reflect your BAM.
    - Rename this file as `config.py` when you're done.
2. Run the following commands:-
    .. code-block:: bash

        make ui-req
        make build
        make run

This runs a docker containerized instance of Gateway with your workflow. Depending on your system needs,
you might have to modify the `run` portion of the Makefile.


Create a single form workflow
---------------------------------------------
.. code-block:: bash

    atk workflow new single-form --name single_form_ui

This command creates a new baseline workflow to kickstart your project, including a single, full workflow that
interacts with BAM. This sample workflow uses the `Add Text Record` feature to add a Text Resource Record, using
React UI. This feature (and therefore the workflow itself) requires the REST v2 client to function. Unlike the
minimal_ui_wf sample workflow, this sample workflow's version of `App.js` defines additional UI elements that show
how to use form components to create buttons for Add and Cancel requests. It presents a simple but complete
workflow process, illustrating how a workflow can allow interactions with a Gateway Workflow UI, sending requests
to BAM and receiving a response.

To run the workflow right after you create it, follow the instructions below:

1. In the output directory, modify ``workspace/config.py.sample`` to reflect your BAM.
    - Rename this file as `config.py` when you're done.
2. Run the following commands:-
    .. code-block:: bash

        make ui-req
        make build
        make run

This should run a docker containerized gateway with your workflow. Please look into the `run` portion of
the Makefile to modify according to your needs.



Workflow Localization
---------------------------------------------

To create localized versions of the `minimal-ui` and `single-form` workflows,
use the `--language` parameter. Multiple languages are supported,
with the first parameter serving as the default language.

Example command to generate localizations for a single form workflow with a single language:

.. code-block:: bash

    atk workflow new single-form --name single_form_ui_localization --language en

Example command to generate localizations for a single form workflow with multiple languages. The first language will be the default:

.. code-block:: bash

    atk workflow new single-form --name single_form_ui_localization --language en --language fr

These commands generate translation files that you will modify with translations for
your project. Store translated and localized content in the po (portable object) files.
In the above example, translations should be stored in the files `en.po` (English) and `fr.po` (French).

The above example workflows contain t macros around all text to be localized. If the `po` file is
updated or new text with a t macro added, run `npx @bluecateng/l10n-cli` from your project root directory.

Common Workflow Parameters
---------------------------------------------

The following are common parameters that can be coupled with all available workflow commands from above.
This same output is also seen from the command below:

.. code-block:: bash

    atk workflow new single-form --help

.. code-block:: text

    --link-description TEXT         Description for the link to the workflow's
                                    page.
    --link-title TEXT               Text to display for the link to the
                                    workflow's page.
    -p, --permission TEXT           Name of the permission to be required by the
                                    workflow.
    -o, --output PATH               Path to the directory to place the output
                                    in.
    -n, --name TEXT                 Name of the created workflow. [required]
    --no-copyright                  An alternative way to specify to not include
                                    any copyright notice. Equivalent to
                                    '--copyright-license none'.
    --copyright-year, --cy TEXT     The year to use in the copyright notice.
                                    Defaults to the current year.
    --copyright-name, --cn TEXT     The name of the copyright owner.
    --copyright-license, --cl       The license to put in the copyright notice
    [proprietary|apache2|mit|none]  in the created files.
    -l, --language TEXT             Languages to be supported by the workflow.

This command shows the use case of all parameters at once. The only required parameter is '--name` as described above.

.. code-block:: bash

    atk workflow new single-form --name single_form_all --permission single_form_permission --link-title 'My Single Form'  --link-description 'View my single form' --output test_wf/single_ui_wf/  --cy 2023 --cn single_ui_property --cl mit --language fr


As specified in the parameters, this command will generate single-form workflow with the following characteristics:
 - Name: `single_form_all`
 - Permission Name: `single_form_permission`
 - Title: `My Single Form`
 - Title Description: `View my single form`
 - Output Location: `/test_wf/single_ui_wf/`
 - Copyright Year: `2023`
 - Copyright Name: `single_ui_property`
 - Copyright License: `mit`
 - Localization: `en`

 Copyright can be avoided all together by using the parameter  `--no-copyright`