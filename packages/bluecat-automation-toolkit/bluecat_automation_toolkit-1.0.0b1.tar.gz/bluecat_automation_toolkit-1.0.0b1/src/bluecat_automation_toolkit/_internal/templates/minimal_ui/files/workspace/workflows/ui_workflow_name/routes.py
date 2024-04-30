{#
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
-#}
{{ copyright_notice(copyright, "py") | safe -}}
"""Routes and back-end implementation of workflow "{{workflow_name}}"."""

from bluecat.gateway.decorators import (
    api_exc_handler,
    page_exc_handler,
    require_permission,
)
from bluecat.util import no_cache

from .base import bp

from flask import send_from_directory
from pathlib import Path


@bp.route("/")
@page_exc_handler(default_message='Failed to load page "{{link_title}}".')
@require_permission("{{permission_name}}")
def page():
    """
    Render page "{{link_title}}".

    :return: Response with the page's HTML.
    """
    return send_from_directory(
        Path(__file__).parent, "html/{{js_workflow_name}}/index.html"
    )



@bp.route("/", methods=["POST"])
@no_cache
@api_exc_handler(default_message="Failed to perform the action.")
@require_permission("{{permission_name}}")
def api_post_{{workflow_name}}():
    """
    Perform an action based on the provided parameters.
    """
    # Validate the parameters.

    # Perform the action.

    # Respond with success.
    return {
        "message": "Operation successfully completed.",
    }

@bp.route("/data")
@page_exc_handler(default_message='Failed to load page "{{link_title}}" data.')
@require_permission("{{permission_name}}")
def data():
    """
    Return data for page "{{link_title}}".

    :return: Response with data
    """
    # return form data

    return {
        #"field_1": initial_field1_value,
    }

