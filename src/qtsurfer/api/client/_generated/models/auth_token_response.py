from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_token_response_tier import AuthTokenResponseTier
from ..models.auth_token_response_token_type import AuthTokenResponseTokenType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_scopes import KeyScopes


T = TypeVar("T", bound="AuthTokenResponse")


@_attrs_define
class AuthTokenResponse:
    """
    Attributes:
        access_token (str): Short-lived HS256 JWT. Send as `Authorization: Bearer <token>` on all other endpoints.
        token_type (AuthTokenResponseTokenType): Always `Bearer`.
        expires_in (int): Seconds until the JWT expires (typically 3600). Example: 3600.
        tier (AuthTokenResponseTier): Subscription tier this token was issued for. Drives rate limits and feature flags
            on downstream endpoints. Example: free.
        scopes (KeyScopes | Unset): What your API key may do, as a map from a resource to the actions allowed on it.
            Names are
            lower case: `{ "backtests": ["read", "write", "execute"], "exchanges": ["read"] }`. A scope
            is a resource and an action: a resource is listed only with at least one action, and a key
            with no scope is `{}`. `GET /account` and `POST /auth/token` return the same map for the
            same key. The API reports the scopes of a key; it does not yet refuse an operation because
            a scope is missing.
             Example: {'backtests': ['read', 'write', 'execute'], 'exchanges': ['read']}.
    """

    access_token: str
    token_type: AuthTokenResponseTokenType
    expires_in: int
    tier: AuthTokenResponseTier
    scopes: KeyScopes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        token_type = self.token_type.value

        expires_in = self.expires_in

        tier = self.tier.value

        scopes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "token_type": token_type,
                "expires_in": expires_in,
                "tier": tier,
            }
        )
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_scopes import KeyScopes

        d = dict(src_dict)
        access_token = d.pop("access_token")

        token_type = AuthTokenResponseTokenType(d.pop("token_type"))

        expires_in = d.pop("expires_in")

        tier = AuthTokenResponseTier(d.pop("tier"))

        _scopes = d.pop("scopes", UNSET)
        scopes: KeyScopes | Unset
        if isinstance(_scopes, Unset):
            scopes = UNSET
        else:
            scopes = KeyScopes.from_dict(_scopes)

        auth_token_response = cls(
            access_token=access_token,
            token_type=token_type,
            expires_in=expires_in,
            tier=tier,
            scopes=scopes,
        )

        auth_token_response.additional_properties = d
        return auth_token_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
