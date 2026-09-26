import json

import allure


def _convert_to_text(data):

    if data is None:
        return ""

    try:

        if isinstance(data, (dict, list)):

            return json.dumps(
                data,
                indent=2,
                ensure_ascii=False,
            )

        return str(data)

    except Exception:

        return str(data)


def attach_request_response(
    method,
    url,
    response,
    request_body=None,
    params=None,
):


    allure.attach(
        str(method),
        name="HTTP Method",
        attachment_type=allure.attachment_type.TEXT,
    )

    allure.attach(
        str(url),
        name="Request URL",
        attachment_type=allure.attachment_type.TEXT,
    )

    if params is not None:

        allure.attach(
            _convert_to_text(params),
            name="Query Parameters",
            attachment_type=allure.attachment_type.TEXT,
        )

    if request_body is not None:

        allure.attach(
            _convert_to_text(request_body),
            name="Request Body",
            attachment_type=allure.attachment_type.TEXT,
        )

    
    try:

        allure.attach(
            str(response.status_code),
            name="Response Status Code",
            attachment_type=allure.attachment_type.TEXT,
        )

    except Exception:
        pass

    try:

        allure.attach(
            _convert_to_text(
                dict(response.headers)
            ),
            name="Response Headers",
            attachment_type=allure.attachment_type.TEXT,
        )

    except Exception:
        pass

    try:

        response_json = response.json()

        allure.attach(
            json.dumps(
                response_json,
                indent=2,
                ensure_ascii=False,
            ),
            name="Response Body",
            attachment_type=allure.attachment_type.JSON,
        )

    except Exception:

        try:

            allure.attach(
                response.text,
                name="Response Body",
                attachment_type=allure.attachment_type.TEXT,
            )

        except Exception:
            pass