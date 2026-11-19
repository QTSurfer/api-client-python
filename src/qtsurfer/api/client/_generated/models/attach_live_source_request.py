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
    """

    source: LiveSourceRequest
    warm_from: int | Unset = UNSET
    ref: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source.to_dict()

        warm_from = self.warm_from

        ref = self.ref

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_source_request import LiveSourceRequest

        d = dict(src_dict)
        source = LiveSourceRequest.from_dict(d.pop("source"))

        warm_from = d.pop("warmFrom", UNSET)

        ref = d.pop("ref", UNSET)

        attach_live_source_request = cls(
            source=source,
            warm_from=warm_from,
            ref=ref,
        )

        return attach_live_source_request
