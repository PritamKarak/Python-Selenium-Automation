from behave import given, when, then

from utils.data_generator import user_registration_payload
from utils.allure_utils import attach_request_response

from framework.response_validator import (
    assert_status,
    assert_json,
)


def _record(
    context,
    response,
    method,
    url,
    body=None,
    params=None,
):
    """
    Store API response in Behave context
    and attach request/response information to Allure.
    """

    context.response = response
    context.response_url = url
    context.request_body = body
    context.request_params = params

    attach_request_response(
        method,
        url,
        response.response,
        request_body=body,
        params=params,
    )


@given("I register a new Automation Exercise user")
def register_user(context):

    payload = user_registration_payload()

    response = context.automation.post(
        "/api/createAccount",
        data=payload,
    )

    _record(
        context,
        response,
        "POST",
        context.automation._url(
            "/api/createAccount"
        ),
        body=payload,
    )

    # Automation Exercise returns HTTP 200
    # and uses responseCode inside JSON.

    assert_status(
        response.response,
        200,
    )

    body = assert_json(
        response.response
    )

    if body.get("responseCode") != 201:
        raise AssertionError(
            f"Expected API responseCode 201, "
            f"got {body.get('responseCode')}. "
            f"Response: {body}"
        )

    context.registered_user = payload

    # Keep compatibility with common_steps.py
    context.created_user = payload


@when(
    "I verify login using the registered user's credentials"
)
def verify_registered_login(context):

    data = {
        "email": context.registered_user["email"],
        "password": context.registered_user["password"],
    }

    response = context.automation.post(
        "/api/verifyLogin",
        data=data,
    )

    _record(
        context,
        response,
        "POST",
        context.automation._url(
            "/api/verifyLogin"
        ),
        body=data,
    )


@when(
    'I verify login using email "{email}" and password "{password}"'
)
def verify_invalid_login(
    context,
    email,
    password,
):

    data = {
        "email": email,
        "password": password,
    }

    response = context.automation.post(
        "/api/verifyLogin",
        data=data,
    )

    _record(
        context,
        response,
        "POST",
        context.automation._url(
            "/api/verifyLogin"
        ),
        body=data,
    )


@when(
    'I verify login without an email using password "{password}"'
)
def verify_without_email(
    context,
    password,
):

    data = {
        "password": password,
    }

    response = context.automation.post(
        "/api/verifyLogin",
        data=data,
    )

    _record(
        context,
        response,
        "POST",
        context.automation._url(
            "/api/verifyLogin"
        ),
        body=data,
    )


@when(
    "I get the Automation Exercise user details by email"
)
def get_user_details(context):

    email = context.registered_user["email"]

    params = {
        "email": email,
    }

    response = context.automation.get(
        "/api/getUserDetailByEmail",
        params=params,
    )

    _record(
        context,
        response,
        "GET",
        context.automation._url(
            "/api/getUserDetailByEmail"
        ),
        params=params,
    )


@when(
    'I send a DELETE request to "/api/verifyLogin" on the Automation Exercise API'
)
def delete_verify_login(context):

    response = context.automation.delete(
        "/api/verifyLogin"
    )

    _record(
        context,
        response,
        "DELETE",
        context.automation._url(
            "/api/verifyLogin"
        ),
    )


@then(
    "I delete the registered Automation Exercise user"
)
def delete_registered_user(context):

    if not hasattr(
        context,
        "registered_user",
    ):
        return

    data = {
        "email": context.registered_user["email"],
        "password": context.registered_user["password"],
    }

    response = context.automation.delete(
        "/api/deleteAccount",
        data=data,
    )

    _record(
        context,
        response,
        "DELETE",
        context.automation._url(
            "/api/deleteAccount"
        ),
        body=data,
    )

    assert_status(
        response.response,
        200,
    )

    body = assert_json(
        response.response
    )

    if body.get("responseCode") != 200:
        raise AssertionError(
            f"Account deletion failed: {body}"
        )


@when(
    "I update the registered user's account"
)
def update_registered_user(context):

    payload = dict(
        context.registered_user
    )

    payload["name"] = (
        "Updated Wipro Capstone User"
    )

    payload["company"] = (
        "Wipro Updated Capstone"
    )

    payload["mobile_number"] = (
        "9111111111"
    )

    response = context.automation.put(
        "/api/updateAccount",
        data=payload,
    )

    _record(
        context,
        response,
        "PUT",
        context.automation._url(
            "/api/updateAccount"
        ),
        body=payload,
    )