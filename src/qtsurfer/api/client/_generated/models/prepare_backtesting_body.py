from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prepare_backtesting_body_cadence import PrepareBacktestingBodyCadence
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrepareBacktestingBody")


@_attrs_define
class PrepareBacktestingBody:
    """
    Attributes:
        instrument (str): Exchange instrument identifier (e.g. a currency pair) Example: BTC/USDT.
        from_ (str): Start date for the preparation process. Supports the following formats:
            - ISO-8601 (e.g. 2024-12-14T23:59:59Z)
            - ISO DATE (e.g. 2024-12-14)
            - BASIC ISO DATE (e.g., 20241214)
             Example: 2024-12-13T00:00:00Z.
        to (str): End date for the preparation process. Supports the following formats:
            - ISO-8601 (e.g. 2024-12-14T23:59:59Z)
            - ISO DATE (e.g. 2024-12-14)
            - BASIC ISO DATE (e.g., 20241214)
             Example: 2024-12-14.
        cadence (PrepareBacktestingBodyCadence | Unset): Output bar cadence for the prepared range. Defaults to the
            publisher's
            native cadence (`1s`); coarser cadences are produced on demand via
            resampling and stored alongside the native blob in cache. Coarser-than-
            source values must be exact multiples of the source cadence — invalid
            labels return `400`.
             Default: PrepareBacktestingBodyCadence.VALUE_0.
    """

    instrument: str
    from_: str
    to: str
    cadence: PrepareBacktestingBodyCadence | Unset = PrepareBacktestingBodyCadence.VALUE_0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instrument = self.instrument

        from_ = self.from_

        to = self.to

        cadence: str | Unset = UNSET
        if not isinstance(self.cadence, Unset):
            cadence = self.cadence.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instrument": instrument,
                "from": from_,
                "to": to,
            }
        )
        if cadence is not UNSET:
            field_dict["cadence"] = cadence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instrument = d.pop("instrument")

        from_ = d.pop("from")

        to = d.pop("to")

        _cadence = d.pop("cadence", UNSET)
        cadence: PrepareBacktestingBodyCadence | Unset
        if isinstance(_cadence, Unset):
            cadence = UNSET
        else:
            cadence = PrepareBacktestingBodyCadence(_cadence)

        prepare_backtesting_body = cls(
            instrument=instrument,
            from_=from_,
            to=to,
            cadence=cadence,
        )

        prepare_backtesting_body.additional_properties = d
        return prepare_backtesting_body

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
