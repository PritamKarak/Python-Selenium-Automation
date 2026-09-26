from requests.auth import HTTPBasicAuth


class AuthManager:
    """Reusable authentication helper for APIs that need common auth schemes."""

    @staticmethod
    def no_auth():
        return {}

    @staticmethod
    def bearer(token):
        return {"Authorization": f"Bearer {token}"}

    @staticmethod
    def api_key(key, header_name="X-API-Key"):
        return {header_name: key}

    @staticmethod
    def basic(username, password):
        return HTTPBasicAuth(username, password)
