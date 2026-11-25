from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CexImportInstrumentUsage")


@_attrs_define
class CexImportInstrumentUsage:
    """
    Attributes:
        exchange (str):  Example: binance.
        segment (str):  Example: spot.
        used (int):  Example: 3.
    """

    exchange: str
    segment: str
    used: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exchange = self.exchange

        segment = self.segment

        used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exchange": exchange,
                "segment": segment,
                "used": used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exchange = d.pop("exchange")

        segment = d.pop("segment")

        used = d.pop("used")

        cex_import_instrument_usage = cls(
            exchange=exchange,
            segment=segment,
            used=used,
        )

        cex_import_instrument_usage.additional_properties = d
        return cex_import_instrument_usage

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
