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
{{ copyright_notice(copyright, "js") | safe -}}
import { useEffect } from 'react';
import {
    doGet,
    doPost,
    {% if is_localized -%}
    PageToolkit,
    PageBody,
    PageContent,
    {%- else -%}
    SimplePage,
    {%- endif %}
    usePageError,
    usePageMessages,
    usePageModalSpinner,
    useTrigger,
} from '@bluecateng/limani';
import './App.less';

{% if is_localized -%}
import { t } from '@bluecateng/l10n.macro';
import setLanguage from '../../functions/setLanguage';
{% endif -%}

const Content = () => {
    const { addMessages, addSuccessMessage } = usePageMessages();
    const { setBusy } = usePageModalSpinner();
    const { setError } = usePageError();
    const [triggerLoad, toggleTriggerLoad] = useTrigger();

    useEffect(() => {
        doGet('/{{workflow_name}}/data')
            .then((data) => {

            })
            .catch((error) => {
                setError(error);
            });
    }, [triggerLoad]);



    return (
        <>
            {% if is_localized -%}
                <PageBody>
                    <PageContent pageTitle={t`{{link_title}}`}>
                    </PageContent>
                </PageBody>
            {% else -%}
                <></>
            {% endif -%}
        </>
    );
};

export default function App() {
    return (
        {% if is_localized -%}
        <PageToolkit onLanguageChange={setLanguage}>
            <Content />
        </PageToolkit>
        {%- else -%}
        <SimplePage pageTitle='{{link_title}}'>
            <Content />
        </SimplePage>
        {%- endif %}
    );
}

