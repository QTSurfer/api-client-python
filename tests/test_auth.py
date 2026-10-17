"""Authentication keeps scope grants and distinguishes a valid key without scopes."""

import asyncio

import httpx
import respx

from qtsurfer.api.client import AuthenticatedClient
from qtsurfer.api.client.api.auth import authenticate
from qtsurfer.api.client.models import AuthTokenError, AuthTokenErrorCode, AuthTokenResponse, KeyScopes

BASE = "https://api.example/v1"


def _apikey_client() -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=BASE,
        token="test-api-key",
        prefix="",
        auth_header_name="X-API-Key",
        raise_on_unexpected_status=True,
    )


@respx.mock
def test_authentication_success_parses_resource_action_scope_map() -> None:
    scopes = {"backtests": ["read", "write", "execute"], "exchanges": ["read"]}
    payload = {
        "access_token": "test-jwt",
        "token_type": "Bearer",
        "expires_in": 3600,
        "scopes": scopes,
        "tier": "free",
    }
    route = respx.post(BASE + "/auth/token").mock(return_value=httpx.Response(200, json=payload))

    response = authenticate.sync_detailed(client=_apikey_client())

    assert response.status_code == 200
    assert isinstance(response.parsed, AuthTokenResponse)
    assert isinstance(response.parsed.scopes, KeyScopes)
    assert response.parsed.scopes["backtests"] == ["read", "write", "execute"]
    assert response.parsed.to_dict() == payload
    request = route.calls.last.request
    assert request.headers["X-API-Key"] == "test-api-key"
    assert "Authorization" not in request.headers


@respx.mock
def test_authentication_403_is_a_typed_key_without_scopes_error() -> None:
    payload = {
        "code": "apikey_without_scopes",
        "message": "This API key has no scopes. Create a key with at least one scope in the web app.",
    }
    route = respx.post(BASE + "/auth/token").mock(return_value=httpx.Response(403, json=payload))

    response = authenticate.sync_detailed(client=_apikey_client())

    assert response.status_code == 403
    assert isinstance(response.parsed, AuthTokenError)
    assert response.parsed.code is AuthTokenErrorCode.APIKEY_WITHOUT_SCOPES
    assert response.parsed.to_dict() == payload
    assert len(route.calls) == 1
    assert "access_token" not in response.parsed.to_dict()


@respx.mock
def test_async_authentication_403_is_a_typed_key_without_scopes_error() -> None:
    respx.post(BASE + "/auth/token").mock(
        return_value=httpx.Response(403, json={"code": "apikey_without_scopes", "message": "Create a key with a scope"})
    )

    response = asyncio.run(authenticate.asyncio_detailed(client=_apikey_client()))

    assert response.status_code == 403
    assert isinstance(response.parsed, AuthTokenError)
    assert response.parsed.code is AuthTokenErrorCode.APIKEY_WITHOUT_SCOPES
