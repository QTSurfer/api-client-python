from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.instrument_coverage import InstrumentCoverage


T = TypeVar("T", bound="InstrumentDetail")


@_attrs_define
class InstrumentDetail:
    """Exchange instrument with per-data-type coverage and market info

    Attributes:
        id (str): Instrument identifier (e.g. currency pair) Example: BTC/USDT.
        base (str): Base currency Example: BTC.
        quote (str): Quote currency Example: USDT.
        coverage (InstrumentCoverage | Unset): Time coverage of available data for this instrument, per data type
        last_price (float | Unset): Last traded price Example: 84250.5.
        volume24h (float | Unset): Trading volume in the last 24 hours (in quote currency) Example: 1234567.89.
    """

    id: str
    base: str
    quote: str
    coverage: InstrumentCoverage | Unset = UNSET
    last_price: float | Unset = UNSET
    volume24h: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        base = self.base

        quote = self.quote

        coverage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = self.coverage.to_dict()

        last_price = self.last_price

        volume24h = self.volume24h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "base": base,
                "quote": quote,
            }
        )
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if last_price is not UNSET:
            field_dict["lastPrice"] = last_price
        if volume24h is not UNSET:
            field_dict["volume24h"] = volume24h

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instrument_coverage import InstrumentCoverage

        d = dict(src_dict)
        id = d.pop("id")

        base = d.pop("base")

        quote = d.pop("quote")

        _coverage = d.pop("coverage", UNSET)
        coverage: InstrumentCoverage | Unset
        if isinstance(_coverage, Unset):
            coverage = UNSET
        else:
            coverage = InstrumentCoverage.from_dict(_coverage)

        last_price = d.pop("lastPrice", UNSET)

        volume24h = d.pop("volume24h", UNSET)

        instrument_detail = cls(
            id=id,
            base=base,
            quote=quote,
            coverage=coverage,
            last_price=last_price,
            volume24h=volume24h,
        )

        instrument_detail.additional_properties = d
        return instrument_detail

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
