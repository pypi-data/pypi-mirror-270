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

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
parentdir := $(shell dirname $(mkfile_path))

ui-req:
	cd $(parentdir)/{{ui_project_name}} && npm install

ui-build:
	cd $(parentdir)/{{ui_project_name}} \
		&& export NODE_ENV=production \
		&& npm run build

clean:
	rm -rf \
		$(parentdir)/../../workspace/workflows/{{workflow_name}}/fonts \
		$(parentdir)/../../workspace/workflows/{{workflow_name}}/html \
		$(parentdir)/../../workspace/workflows/{{workflow_name}}/img \
		$(parentdir)/../../workspace/workflows/{{workflow_name}}/js

purge: clean
	rm -rf $(parentdir)/{{ui_project_name}}/node_modules

