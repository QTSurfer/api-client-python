from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeclaredProperty")


@_attrs_define
class DeclaredProperty:
    """One property name `POST /strategy` could establish without constructing the strategy —
    either declared with `@StrategyProperty` on the compiled source, or one of the small set of
    base properties every strategy carries (`amnt`, `enabled`, `multiEntry`, ...).

    **Best-effort, not exhaustive.** A property registered through an attached risk/backtest
    config needs a live instance to discover and is not listed here. Use this to catch a typo'd
    sweep key before submitting, not as the definitive list of what a sweep will accept — a
    name absent from this list may still be valid.

        Attributes:
            name (str): The key a sweep or execute param map uses for this property. Example: rsi.period.
            description (str | Unset): Human-readable label, as declared. Example: RSI period.
            default_value (str | Unset): The declared default, as a string, if one was given. Absent, not null, when none
                was
                declared.
                 Example: 14.
            reflected (bool | Unset): Whether a value for this key is injected into the strategy's field (`true`) or only
                available through the property map (`false`).
                 Example: True.
            min_ (float | Unset): Suggested sweep/range minimum, if declared. Advisory only, never validated. Example: 2.
            max_ (float | Unset): Suggested sweep/range maximum, if declared. Advisory only, never validated. Example: 50.
            step (float | Unset): Suggested sweep/range step, if declared. Advisory only, never validated. Example: 1.
    """

    name: str
    description: str | Unset = UNSET
    default_value: str | Unset = UNSET
    reflected: bool | Unset = UNSET
    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    step: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        default_value = self.default_value

        reflected = self.reflected

        min_ = self.min_

        max_ = self.max_

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if reflected is not UNSET:
            field_dict["reflected"] = reflected
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        reflected = d.pop("reflected", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        step = d.pop("step", UNSET)

        declared_property = cls(
            name=name,
            description=description,
            default_value=default_value,
            reflected=reflected,
            min_=min_,
            max_=max_,
            step=step,
        )

        declared_property.additional_properties = d
        return declared_property

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
