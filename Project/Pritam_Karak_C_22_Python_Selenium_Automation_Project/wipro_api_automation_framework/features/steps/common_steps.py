import json
from pathlib import Path

import allure
from behave import given, when, then

from framework.response_validator import (
    assert_status,
    assert_content_type_json,
    assert_json,
    assert_field_exists,
    assert_field_equals,
    assert_schema,
    assert_response_time,
)

from utils.allure_utils import attach_request_response

from utils.data_generator import user_registration_payload


ROOT_DIR = Path(__file__).resolve().parents[2]


def _client(context, api="jsonplaceholder"):

    if api == "jsonplaceholder":
        return context.jsonplaceholder

    return context.automation


def _record_response(
    context,
    response,
    method,
    url,
    body=None,
    params=None,
):

    context.response = response

    context.response_url = url

    context.request_body = body

    context.request_params = params

    context.request_method = method

    attach_request_response(
        method,
        url,
        response.response,
        request_body=body,
        params=params,
    )



@given("the JSONPlaceholder User API is available")
def step_api_available(context):

    context.api_name = "jsonplaceholder"

    context.api = context.jsonplaceholder


@given("I have a JSONPlaceholder user payload")
def step_user_payload(context):

    context.payload = {
        "name": "Wipro Capstone User",
        "username": "wipro_automation",
        "email": "wipro.automation@example.com",
    }


@given("I have a JSONPlaceholder update payload")
def step_update_payload(context):

    context.payload = {
        "name": "Updated Wipro User",
        "username": "updated_wipro",
        "email": "updated.wipro@example.com",
    }


@given("I have a JSONPlaceholder partial update payload")
def step_partial_payload(context):

    context.payload = {
        "email": "patched.wipro@example.com"
    }


@when('I send a GET request to "{endpoint}"')
def step_get(context, endpoint):

    response = context.jsonplaceholder.get(
        endpoint
    )

    _record_response(
        context,
        response,
        "GET",
        context.jsonplaceholder._url(endpoint),
    )



@when(
    'I send a POST request to "{endpoint}" '
    'with the user payload'
)
def step_post_user(context, endpoint):

    response = context.jsonplaceholder.post(
        endpoint,
        json=context.payload,
    )

    _record_response(
        context,
        response,
        "POST",
        context.jsonplaceholder._url(endpoint),
        context.payload,
    )


@when(
    'I send a PUT request to "{endpoint}" '
    'with the update payload'
)
def step_put_user(context, endpoint):

    response = context.jsonplaceholder.put(
        endpoint,
        json=context.payload,
    )

    _record_response(
        context,
        response,
        "PUT",
        context.jsonplaceholder._url(endpoint),
        context.payload,
    )


@when(
    'I send a PATCH request to "{endpoint}" '
    'with the update payload'
)
def step_patch_user(context, endpoint):

    response = context.jsonplaceholder.patch(
        endpoint,
        json=context.payload,
    )

    _record_response(
        context,
        response,
        "PATCH",
        context.jsonplaceholder._url(endpoint),
        context.payload,
    )


@when('I send a DELETE request to "{endpoint}"')
def step_delete(context, endpoint):

    response = context.jsonplaceholder.delete(
        endpoint
    )

    _record_response(
        context,
        response,
        "DELETE",
        context.jsonplaceholder._url(endpoint),
    )


@then(
    "the response status code should be {expected:d}"
)
def step_status(context, expected):

    assert_status(
        context.response.response,
        expected,
    )


@then("the response should be JSON")
def step_json(context):

    assert_content_type_json(
        context.response.response
    )

    context.json_body = assert_json(
        context.response.response
    )


@then("the response should be a JSON list")
def step_json_list(context):

    assert_content_type_json(
        context.response.response
    )

    context.json_body = assert_json(
        context.response.response
    )

    if not isinstance(
        context.json_body,
        list
    ):

        raise AssertionError(
            "Expected a list, got "
            f"{type(context.json_body).__name__}"
        )


@then(
    "the response list should contain at least 1 user"
)
def step_list_has_user(context):

    if len(context.json_body) < 1:

        raise AssertionError(
            "Expected at least one user in response."
        )


@then(
    'the JSON field "{field}" should exist'
)
def step_field_exists(context, field):

    payload = getattr(
        context,
        "json_body",
        None
    )

    if payload is None:

        payload = assert_json(
            context.response.response
        )

    assert_field_exists(
        payload,
        field
    )


@then(
    'the JSON field "{field}" should equal {expected:d}'
)
def step_field_equals_int(
    context,
    field,
    expected,
):

    payload = getattr(
        context,
        "json_body",
        None
    )

    if payload is None:

        payload = assert_json(
            context.response.response
        )

    assert_field_equals(
        payload,
        field,
        expected,
    )


@then(
    "the user list response should match the schema"
)
def step_list_schema(context):

    schema_path = (
        ROOT_DIR
        / "schemas"
        / "user_list_schema.json"
    )

    schema = json.loads(
        schema_path.read_text(
            encoding="utf-8"
        )
    )

    assert_schema(
        context.json_body,
        schema,
    )


@then(
    "the single user response should match the schema"
)
def step_single_schema(context):

    payload = getattr(
        context,
        "json_body",
        None
    )

    if payload is None:

        payload = assert_json(
            context.response.response
        )

    schema_path = (
        ROOT_DIR
        / "schemas"
        / "user_schema.json"
    )

    schema = json.loads(
        schema_path.read_text(
            encoding="utf-8"
        )
    )

    assert_schema(
        payload,
        schema,
    )


@then(
    "the response time should be less than 2 seconds"
)
def step_response_time(context):

    assert_response_time(
        context.response.elapsed_seconds,
        2.0,
    )


# =========================================================
# CREATED USER
# =========================================================

@then(
    "the created response should contain "
    "the submitted user data"
)
def step_created_data(context):

    payload = assert_json(
        context.response.response
    )

    for field in (
        "name",
        "username",
        "email",
    ):

        assert_field_equals(
            payload,
            field,
            context.payload[field],
        )


@then(
    "the created response should contain "
    "a generated id"
)
def step_created_id(context):

    payload = assert_json(
        context.response.response
    )

    assert_field_exists(
        payload,
        "id",
    )

    if not isinstance(
        payload["id"],
        int
    ):

        raise AssertionError(
            "Created user id should be an integer."
        )



@then(
    "the updated response should contain "
    "the submitted fields"
)
def step_updated_data(context):

    payload = assert_json(
        context.response.response
    )

    for field, expected in context.payload.items():

        assert_field_equals(
            payload,
            field,
            expected,
        )


@when(
    'I send a POST request to "{endpoint}" '
    'on the Automation Exercise API'
)
def step_automation_post(context, endpoint):

    response = context.automation.post(
        endpoint
    )

    _record_response(
        context,
        response,
        "POST",
        context.automation._url(endpoint),
    )


@when(
    'I send a PUT request to "{endpoint}" '
    'on the Automation Exercise API'
)
def step_automation_put(context, endpoint):

    response = context.automation.put(
        endpoint
    )

    _record_response(
        context,
        response,
        "PUT",
        context.automation._url(endpoint),
    )


@when(
    'I send a DELETE request to "{endpoint}" '
    'on the Automation Exercise API'
)
def step_automation_delete(context, endpoint):

    response = context.automation.delete(
        endpoint
    )

    _record_response(
        context,
        response,
        "DELETE",
        context.automation._url(endpoint),
    )


@when(
    'I send a POST request to "{endpoint}" '
    'on the Automation Exercise API '
    'without a search_product parameter'
)
def step_search_without_parameter(
    context,
    endpoint,
):

    response = context.automation.post(
        endpoint,
        data={},
    )

    _record_response(
        context,
        response,
        "POST",
        context.automation._url(endpoint),
        body={},
    )


@then(
    'the response message should be "{expected}"'
)
def step_message(context, expected):

    payload = assert_json(
        context.response.response
    )

    message = payload.get(
        "message"
    )

    if message != expected:

        raise AssertionError(
            f"Expected message {expected!r}, "
            f"got {message!r}"
        )


@then(
    "the response should contain the registered user's email"
)
def step_registered_email(context):

    payload = assert_json(
        context.response.response
    )

    expected_email = (
        context.registered_user["email"]
    )

    user = payload.get("user", payload)

    actual_email = user.get("email")

    if actual_email != expected_email:
        raise AssertionError(
            f"Expected email {expected_email!r}, "
            f"got {actual_email!r}"
        )

@then(
    "the API responseCode should be {expected:d}"
)
def step_api_response_code(
    context,
    expected,
):

    payload = assert_json(
        context.response.response
    )

    actual = payload.get(
        "responseCode"
    )

    if actual != expected:
        raise AssertionError(
            f"Expected API responseCode "
            f"{expected}, got {actual}. "
            f"Response: {payload}"
        )