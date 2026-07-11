from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.instrument_list_meta_segment import InstrumentListMetaSegment

T = TypeVar("T", bound="InstrumentListMeta")


@_attrs_define
class InstrumentListMeta:
    """Metadata describing the instruments listing

    Attributes:
        updated_at (datetime.datetime): When this listing was last refreshed Example: 2026-07-09T19:09:07Z.
        exchange (str): The exchange the instruments belong to Example: binance.
        segment (InstrumentListMetaSegment): The market segment served in `data` Example: spot.
    """

    updated_at: datetime.datetime
    exchange: str
    segment: InstrumentListMetaSegment
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        exchange = self.exchange

        segment = self.segment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updatedAt": updated_at,
                "exchange": exchange,
                "segment": segment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updatedAt"))

        exchange = d.pop("exchange")

        segment = InstrumentListMetaSegment(d.pop("segment"))

        instrument_list_meta = cls(
            updated_at=updated_at,
            exchange=exchange,
            segment=segment,
        )

        instrument_list_meta.additional_properties = d
        return instrument_list_meta

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
