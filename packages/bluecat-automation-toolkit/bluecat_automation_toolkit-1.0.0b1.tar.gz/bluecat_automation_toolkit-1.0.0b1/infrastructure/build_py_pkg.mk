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

clean-build:
	cd $(BASE_DIR) && rm -rf build dist src/*.egg-info

# Build the package
.PHONY: build
build: clean-build
	python -m build

# Publish the built package to GitLab registry
.PHONY: publish
publish:
	@TWINE_USERNAME=$(CI_REGISTRY_USER) \
	TWINE_PASSWORD=$(CI_REGISTRY_PASSWORD) \
	TWINE_REPOSITORY_URL=https://gitlab.bluecatlabs.net/api/v4/projects/$(CI_PROJECT_ID)/packages/pypi \
	python3 -m twine upload -r local $(BASE_DIR)/dist/*

.PHONY: pull
pull:
	@pip3 install \
		bluecat-automation-toolkit==$(version) \
		--extra-index-url https://$(CI_REGISTRY_USER):$(CI_JOB_TOKEN)@gitlab.bluecatlabs.net/api/v4/projects/$(CI_PROJECT_ID)/packages/pypi/simple

.PHONY: release
release: build publish
