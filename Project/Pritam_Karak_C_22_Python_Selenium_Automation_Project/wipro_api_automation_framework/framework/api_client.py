import json
import time
from dataclasses import dataclass
from typing import Any, Optional

import requests

from framework.config_reader import get_timeout, verify_ssl
from framework.exceptions import APIRequestError
from framework.logger import logger


@dataclass
class APIResponse:
    response: requests.Response
    elapsed_seconds: float

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def headers(self):
        return self.response.headers

    @property
    def text(self):
        return self.response.text

    def json(self):
        return self.response.json()


class APIClient:
    """Reusable HTTP client built on top of Python Requests."""

    def __init__(self, base_url: str, default_headers: Optional[dict] = None):
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {
            "Accept": "application/json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.default_headers)

    def _url(self, endpoint):
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            return endpoint
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def request(self, method, endpoint, **kwargs):
        url = self._url(endpoint)
        headers = kwargs.pop("headers", None)
        merged_headers = dict(self.default_headers)
        if headers:
            merged_headers.update(headers)

        timeout = kwargs.pop("timeout", get_timeout())
        verify = kwargs.pop("verify", verify_ssl())

        logger.info("REQUEST | %s %s", method.upper(), url)
        if kwargs.get("params"):
            logger.info("QUERY PARAMS | %s", kwargs["params"])
        if kwargs.get("json") is not None:
            logger.info("JSON BODY | %s", json.dumps(kwargs["json"], ensure_ascii=False))
        if kwargs.get("data") is not None:
            logger.info("FORM BODY | %s", kwargs["data"])

        start = time.perf_counter()
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                headers=merged_headers,
                timeout=timeout,
                verify=verify,
                **kwargs,
            )
        except requests.RequestException as exc:
            logger.exception("REQUEST FAILED | %s %s | %s", method.upper(), url, exc)
            raise APIRequestError(f"Request failed for {method.upper()} {url}: {exc}") from exc

        elapsed = time.perf_counter() - start
        logger.info(
            "RESPONSE | %s %s | status=%s | time=%.3fs",
            method.upper(), url, response.status_code, elapsed
        )
        logger.info("RESPONSE BODY | %s", response.text[:5000])

        return APIResponse(response, elapsed)

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)
