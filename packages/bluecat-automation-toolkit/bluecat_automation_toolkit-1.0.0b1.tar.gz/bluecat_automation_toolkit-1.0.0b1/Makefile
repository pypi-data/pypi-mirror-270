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

BASE_DIR := $(shell pwd)
export BASE_DIR

# Choose pytest command depending on whether or not coverage is required.
ifdef cov
PYTEST_CMD = python3 -m coverage run --append -m pytest -k "${CUSTOM_TEST_SELECTION}"
else
PYTEST_CMD = pytest -k "${CUSTOM_TEST_SELECTION}"
endif

EXTRA_INDEX_URL = --extra-index-url='https://gitlab.bluecatlabs.net/api/v4/projects/3569/packages/pypi/simple'

include $(BASE_DIR)/infrastructure/build_py_pkg.mk
include $(BASE_DIR)/infrastructure/gen_req_hash.mk
include $(BASE_DIR)/infrastructure/pylint.mk
include $(BASE_DIR)/infrastructure/ruff.mk
include $(BASE_DIR)/infrastructure/tests.mk
include $(BASE_DIR)/infrastructure/venv.mk

.PHONY: black black-check
black:
	@black .

black-check:
	@tox -e black-check

copyright-check:
	@tox -e copyright-check
