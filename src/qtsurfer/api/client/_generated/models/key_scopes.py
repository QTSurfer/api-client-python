from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyScopes")


@_attrs_define
class KeyScopes:
    """What your API key may do, as a map from a resource to the actions allowed on it. Names are
    lower case: `{ "backtests": ["read", "write", "execute"], "exchanges": ["read"] }`. A key
    with no scopes is `{}`. `GET /account` and `POST /auth/token` return the same map for the
    same key. The API reports the scopes of a key; it does not yet refuse an operation because
    a scope is missing.

        Example:
            {'backtests': ['read', 'write', 'execute'], 'exchanges': ['read']}

    """

    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_scopes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[str], prop_dict)

            additional_properties[prop_name] = additional_property

        key_scopes.additional_properties = additional_properties
        return key_scopes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
