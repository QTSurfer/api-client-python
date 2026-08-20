from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.strategy_summary import StrategySummary


T = TypeVar("T", bound="ListStrategiesResponse200")


@_attrs_define
class ListStrategiesResponse200:
    """
    Attributes:
        strategies (list[StrategySummary]):
    """

    strategies: list[StrategySummary]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategies = []
        for strategies_item_data in self.strategies:
            strategies_item = strategies_item_data.to_dict()
            strategies.append(strategies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategies": strategies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.strategy_summary import StrategySummary

        d = dict(src_dict)
        strategies = []
        _strategies = d.pop("strategies")
        for strategies_item_data in _strategies:
            strategies_item = StrategySummary.from_dict(strategies_item_data)

            strategies.append(strategies_item)

        list_strategies_response_200 = cls(
            strategies=strategies,
        )

        list_strategies_response_200.additional_properties = d
        return list_strategies_response_200

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
