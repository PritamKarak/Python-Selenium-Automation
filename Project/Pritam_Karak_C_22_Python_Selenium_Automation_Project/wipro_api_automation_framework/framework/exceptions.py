class APIAutomationError(Exception):
    """Base exception for the API automation framework."""


class APIRequestError(APIAutomationError):
    """Raised when an HTTP request cannot be completed."""


class ResponseValidationError(APIAutomationError):
    """Raised when an API response does not satisfy an expected contract."""
