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
import { useEffect, useState } from 'react';
import {
    doGet,
    doPost,
    FormButtons,
    FormLayout,
    processErrorMessages,
    replaceKeys,
    {% if is_localized -%}
    PageToolkit,
    PageBody,
    PageContent,
    {%- else %}SimplePage,{%- endif %}
    usePageError,
    usePageMessages,
    usePageModalSpinner,
    useTrigger,
} from '@bluecateng/limani';
import { Form, validateNotEmpty } from '@bluecateng/auto-forms';
import { FormFields } from './FormFields';
{% if is_localized -%}
import { t } from '@bluecateng/l10n.macro';
import setLanguage from '../../functions/setLanguage';
{% endif -%}
import './App.less';

const BE_FE = new Map([
    ['configuration', 'configuration'],
    ['view', 'view'],
    ['zone', 'zone'],
    ['name', 'name'],
    ['text', 'text'],
]);

const Content = () => {
    const { addMessages, addSuccessMessage } = usePageMessages();
    const { setBusy } = usePageModalSpinner();
    const { setError } = usePageError();
    const [triggerLoad, toggleTriggerLoad] = useTrigger();
    const [initialFormData, setInitialFormData] = useState(null);

    useEffect(() => {
        doGet('/{{workflow_name}}/configurations')
            .then((data) => {
                setInitialFormData({
                    configurations: data.configurations,
                    configuration: '',
                    view: '',
                    zone: '',
                    name: '',
                    text: '',
                });
            })
            .catch((error) => {
                setError(error);
            });
    }, [triggerLoad]);

    const extraValidation = (errors, { configuration, view, zone }) => ({
        ...errors,
        configuration: validateNotEmpty({{ localize('Please select a configuration.') }})(configuration?.name),
        view: validateNotEmpty({{ localize('Please select a view.') }})(view?.name),
        zone: validateNotEmpty({{ localize('Please select a zone.') }})(zone?.name),
    });


    const handleSubmit = (values, { setErrors }) => {
        setBusy(true);
        const payload = new FormData();
        payload.append('zone_name', values.zone.name);
        payload.append('zone_id', values.zone.id);
        payload.append('name', values.name);
        payload.append('text', values.text);

        doPost('/{{workflow_name}}', payload)
            .then((data) => {
                addSuccessMessage(data.message);
                toggleTriggerLoad();
            })
            .catch((error) => {
                const { page: pageErrors, fields: fieldsErrors } = processErrorMessages(
                    error,
                    Array.from(BE_FE.keys()),
                    true,
                );
                setErrors(replaceKeys(fieldsErrors, BE_FE));
                addMessages(pageErrors.map((text) => ({ type: 'error', text: text })));
            })
            .finally(() => setBusy(false));
    };

    return (
        <>
            {initialFormData && (
                {% if is_localized -%}
                <PageBody>
                    <PageContent pageTitle={t`{{link_title}}`}>
                        <FormLayout>
                            <Form
                                className='WorkflowForm'
                                initialValues={initialFormData}
                                rules={{ '{{}}' }}
                                extraValidation={extraValidation}
                                onSubmit={handleSubmit}>
                                <FormFields initialFormData={initialFormData} />
                                <FormButtons />
                            </Form>
                        </FormLayout>
                    </PageContent>
                </PageBody>{% else -%}
                <FormLayout>
                    <Form
                        className='WorkflowForm'
                        initialValues={initialFormData}
                        rules={{ '{{}}' }}
                        extraValidation={extraValidation}
                        onSubmit={handleSubmit}>
                        <FormFields initialFormData={initialFormData} />
                        <FormButtons />
                    </Form>
                </FormLayout>{%- endif %}
            )}
        </>
    );
};

export default function App() {
    return (
        {% if is_localized -%}
        <PageToolkit onLanguageChange={setLanguage}>
            <Content />
        </PageToolkit>{% else -%}<SimplePage pageTitle='{{link_title}}'>
            <Content />
        </SimplePage>
        {%- endif %}
    );
}

