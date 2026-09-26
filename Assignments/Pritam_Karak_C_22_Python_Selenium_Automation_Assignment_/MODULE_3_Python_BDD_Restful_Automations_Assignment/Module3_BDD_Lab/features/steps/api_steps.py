from behave import given, when, then
import requests


@given('the API endpoint is "{endpoint}"')
def step_endpoint(context, endpoint):
    context.endpoint = endpoint


@when("I send a GET request")
def step_get(context):
    context.response = requests.get(
        context.endpoint,
        timeout=10
    )


@then("the response status code should be 200")
def step_status(context):
    assert context.response.status_code == 200


@then("the response ID should be {post_id:d}")
def step_id(context, post_id):
    data = context.response.json()
    assert data["id"] == post_id