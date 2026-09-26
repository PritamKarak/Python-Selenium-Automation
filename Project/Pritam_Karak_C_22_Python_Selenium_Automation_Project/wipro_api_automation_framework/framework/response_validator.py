from jsonschema import validate
from jsonschema.exceptions import ValidationError as JSONSchemaValidationError

from framework.exceptions import ResponseValidationError


def assert_status(response, expected):
    actual = response.status_code
    if actual != expected:
        raise AssertionError(
            f"Expected status {expected}, but received {actual}. "
            f"Response: {response.text[:1000]}"
        )


def assert_content_type_json(response):
    content_type = response.headers.get("Content-Type", "")
    if "application/json" not in content_type.lower():
        raise AssertionError(
            f"Expected JSON content type, got: {content_type}"
        )


def assert_json(response):
    try:
        return response.json()
    except ValueError as exc:
        raise ResponseValidationError(
            f"Response is not valid JSON: {response.text[:1000]}"
        ) from exc


def assert_field_exists(payload, field):
    if not isinstance(payload, dict):
        raise AssertionError("Expected a JSON object while checking a field.")
    if field not in payload:
        raise AssertionError(f"Required field '{field}' was not found.")


def assert_field_equals(payload, field, expected):
    assert_field_exists(payload, field)
    actual = payload[field]
    if actual != expected:
        raise AssertionError(
            f"Field '{field}': expected {expected!r}, got {actual!r}"
        )


def assert_schema(payload, schema):
    try:
        validate(instance=payload, schema=schema)
    except JSONSchemaValidationError as exc:
        raise AssertionError(f"JSON schema validation failed: {exc.message}") from exc


def assert_response_time(elapsed_seconds, max_seconds=2.0):
    if elapsed_seconds > max_seconds:
        raise AssertionError(
            f"Response took {elapsed_seconds:.3f}s; expected <= {max_seconds:.3f}s"
        )
