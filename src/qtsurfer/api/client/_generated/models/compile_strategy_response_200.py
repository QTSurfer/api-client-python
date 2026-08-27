from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.declared_property import DeclaredProperty


T = TypeVar("T", bound="CompileStrategyResponse200")


@_attrs_define
class CompileStrategyResponse200:
    """
    Attributes:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        declared_properties (list[DeclaredProperty] | Unset): What could be established about this strategy's sweep-key
            vocabulary without
            constructing it. See `DeclaredProperty` — best-effort, not exhaustive.
    """

    strategy_id: str
    declared_properties: list[DeclaredProperty] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        declared_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.declared_properties, Unset):
            declared_properties = []
            for declared_properties_item_data in self.declared_properties:
                declared_properties_item = declared_properties_item_data.to_dict()
                declared_properties.append(declared_properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
            }
        )
        if declared_properties is not UNSET:
            field_dict["declaredProperties"] = declared_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.declared_property import DeclaredProperty

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        _declared_properties = d.pop("declaredProperties", UNSET)
        declared_properties: list[DeclaredProperty] | Unset = UNSET
        if _declared_properties is not UNSET:
            declared_properties = []
            for declared_properties_item_data in _declared_properties:
                declared_properties_item = DeclaredProperty.from_dict(declared_properties_item_data)

                declared_properties.append(declared_properties_item)

        compile_strategy_response_200 = cls(
            strategy_id=strategy_id,
            declared_properties=declared_properties,
        )

        compile_strategy_response_200.additional_properties = d
        return compile_strategy_response_200

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
