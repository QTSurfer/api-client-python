from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_signal import LiveSignal
    from ..models.public_live_list_links import PublicLiveListLinks


T = TypeVar("T", bound="LiveSignalPage")


@_attrs_define
class LiveSignalPage:
    """One page of a run's recorded signals, oldest first.

    Attributes:
        signals (list[LiveSignal]):
        available_since_ms (int | Unset): The oldest moment this run's signals can still be read from. Absent when the
            run has produced nothing yet. It moves forward over time as older signals are discarded, so a `sinceMs` earlier
            than this is served from here instead.
        field_links (PublicLiveListLinks | Unset): Present only when another page exists.
    """

    signals: list[LiveSignal]
    available_since_ms: int | Unset = UNSET
    field_links: PublicLiveListLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.to_dict()
            signals.append(signals_item)

        available_since_ms = self.available_since_ms

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signals": signals,
            }
        )
        if available_since_ms is not UNSET:
            field_dict["availableSinceMs"] = available_since_ms
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_signal import LiveSignal
        from ..models.public_live_list_links import PublicLiveListLinks

        d = dict(src_dict)
        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = LiveSignal.from_dict(signals_item_data)

            signals.append(signals_item)

        available_since_ms = d.pop("availableSinceMs", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: PublicLiveListLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PublicLiveListLinks.from_dict(_field_links)

        live_signal_page = cls(
            signals=signals,
            available_since_ms=available_since_ms,
            field_links=field_links,
        )

        live_signal_page.additional_properties = d
        return live_signal_page

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
