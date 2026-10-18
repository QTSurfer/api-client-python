from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_live_params_request_params import UpdateLiveParamsRequestParams


T = TypeVar("T", bound="UpdateLiveParamsRequest")


@_attrs_define
class UpdateLiveParamsRequest:
    """
    Attributes:
        params (UpdateLiveParamsRequestParams): Must be non-empty; every key must be a property your strategy declares.
    """

    params: UpdateLiveParamsRequestParams
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_live_params_request_params import UpdateLiveParamsRequestParams

        d = dict(src_dict)
        params = UpdateLiveParamsRequestParams.from_dict(d.pop("params"))

        update_live_params_request = cls(
            params=params,
        )

        update_live_params_request.additional_properties = d
        return update_live_params_request

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
