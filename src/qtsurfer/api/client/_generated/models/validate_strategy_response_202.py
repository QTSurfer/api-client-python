from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_strategy_response_202_validation import ValidateStrategyResponse202Validation

T = TypeVar("T", bound="ValidateStrategyResponse202")


@_attrs_define
class ValidateStrategyResponse202:
    """
    Attributes:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
            always yields the same id, for every caller, whatever its formatting. See
            `POST /strategy` for exactly which rewrites preserve it and which do not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        validation (ValidateStrategyResponse202Validation):
    """

    strategy_id: str
    validation: ValidateStrategyResponse202Validation
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        validation = self.validation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
                "validation": validation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        validation = ValidateStrategyResponse202Validation(d.pop("validation"))

        validate_strategy_response_202 = cls(
            strategy_id=strategy_id,
            validation=validation,
        )

        validate_strategy_response_202.additional_properties = d
        return validate_strategy_response_202

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
