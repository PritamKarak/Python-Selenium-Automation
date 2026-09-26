class RequestBuilder:
    """Small fluent helper for building reusable request components."""

    def __init__(self):
        self._headers = {}
        self._params = {}
        self._json = None
        self._data = None

    def headers(self, **headers):
        self._headers.update(headers)
        return self

    def params(self, **params):
        self._params.update(params)
        return self

    def json(self, payload):
        self._json = payload
        return self

    def data(self, payload):
        self._data = payload
        return self

    def build(self):
        request = {}
        if self._headers:
            request["headers"] = self._headers
        if self._params:
            request["params"] = self._params
        if self._json is not None:
            request["json"] = self._json
        if self._data is not None:
            request["data"] = self._data
        return request
