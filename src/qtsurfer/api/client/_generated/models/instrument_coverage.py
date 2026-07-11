from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_window import CoverageWindow


T = TypeVar("T", bound="InstrumentCoverage")


@_attrs_define
class InstrumentCoverage:
    """Time coverage of available data for this instrument, per data type

    Attributes:
        tickers (CoverageWindow | Unset): The time range of available data for a single data type
        klines (CoverageWindow | Unset): The time range of available data for a single data type
    """

    tickers: CoverageWindow | Unset = UNSET
    klines: CoverageWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tickers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tickers, Unset):
            tickers = self.tickers.to_dict()

        klines: dict[str, Any] | Unset = UNSET
        if not isinstance(self.klines, Unset):
            klines = self.klines.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tickers is not UNSET:
            field_dict["tickers"] = tickers
        if klines is not UNSET:
            field_dict["klines"] = klines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_window import CoverageWindow

        d = dict(src_dict)
        _tickers = d.pop("tickers", UNSET)
        tickers: CoverageWindow | Unset
        if isinstance(_tickers, Unset):
            tickers = UNSET
        else:
            tickers = CoverageWindow.from_dict(_tickers)

        _klines = d.pop("klines", UNSET)
        klines: CoverageWindow | Unset
        if isinstance(_klines, Unset):
            klines = UNSET
        else:
            klines = CoverageWindow.from_dict(_klines)

        instrument_coverage = cls(
            tickers=tickers,
            klines=klines,
        )

        instrument_coverage.additional_properties = d
        return instrument_coverage

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
