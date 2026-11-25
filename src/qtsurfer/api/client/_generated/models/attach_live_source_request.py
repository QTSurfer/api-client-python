from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_source_request import LiveSourceRequest


T = TypeVar("T", bound="AttachLiveSourceRequest")


@_attrs_define
class AttachLiveSourceRequest:
    """
    Attributes:
        source (LiveSourceRequest): One market-data source to start a live run on, or to attach to one. It is
            `LiveSource` as you ask for it: the only difference is that `instruments` can be left out.
        warm_from (int | Unset): Seconds of the feed before the attachment that the strategy sees first, for this source
            only. Left out, the same default as at start. See "Warming up" in the Live execution guide.
        ref (str | Unset): A string of yours. Sending the same `ref` to the same run answers the attachment it already
            made instead of making another one.
        resolve_instrument (bool | Unset): For a `dex` pool. `true`: the strategy is told of the source, with the pair
            the pool's candles carry, when the pool delivers its first candle. `false`: it is told at once, with a stand-in
            instrument made of the pool's address and `<exchange>:<segment>`. A centralized exchange's source accepts the
            field and ignores it. See "The instrument of a pool" in the Live execution guide. Default: True.
    """

    source: LiveSourceRequest
    warm_from: int | Unset = UNSET
    ref: str | Unset = UNSET
    resolve_instrument: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        source = self.source.to_dict()

        warm_from = self.warm_from

        ref = self.ref

        resolve_instrument = self.resolve_instrument

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if warm_from is not UNSET:
            field_dict["warmFrom"] = warm_from
        if ref is not UNSET:
            field_dict["ref"] = ref
        if resolve_instrument is not UNSET:
            field_dict["resolveInstrument"] = resolve_instrument

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_source_request import LiveSourceRequest

        d = dict(src_dict)
        source = LiveSourceRequest.from_dict(d.pop("source"))

        warm_from = d.pop("warmFrom", UNSET)

        ref = d.pop("ref", UNSET)

        resolve_instrument = d.pop("resolveInstrument", UNSET)

        attach_live_source_request = cls(
            source=source,
            warm_from=warm_from,
            ref=ref,
            resolve_instrument=resolve_instrument,
        )

        return attach_live_source_request
