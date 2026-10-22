from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyScopes")


@_attrs_define
class KeyScopes:
    """What your API key may do, as a map from a resource to the actions allowed on it. Names are
    lower case: `{ "backtests": ["read", "write", "execute"], "exchanges": ["read"] }`. A scope
    is a resource and an action: a resource is listed only with at least one action, and a key
    with no scope is `{}`. `GET /account` and `POST /auth/token` return the same map for the
    same key. An operation that needs a scope the key does not carry is answered `403` with the
    code `insufficient_scope`, and says which scope it needed.

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
