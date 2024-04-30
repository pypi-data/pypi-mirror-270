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

# Generates hash file for dev.in
# usage: make compile-dev-pkg dir=<venv_dir>
compile-dev-pkg:
	@$(dir)/bin/pip3 install pip-tools && \
	pip-compile --no-emit-index-url --generate-hashes $(EXTRA_INDEX_URL) requirements/dev.in

# Generates hash file for lint.in
compile-lint-pkg:
	@$(dir)/bin/pip3 install pip-tools && \
	pip-compile --generate-hashes requirements/lint.in

# Generates hash file for build.in
compile-build-pkg:
	@$(dir)/bin/pip3 install pip-tools && \
	pip-compile --generate-hashes requirements/build.in

# Generates hash file for tests.in
compile-tests-pkg:
	@$(dir)/bin/pip3 install pip-tools && \
	pip-compile --generate-hashes requirements/tests.in

# Generates hash file for copyright.in
compile-copyright-pkg:
	@$(dir)/bin/pip3 install pip-tools && \
	pip-compile --no-emit-index-url --generate-hashes $(EXTRA_INDEX_URL) requirements/copyright.in