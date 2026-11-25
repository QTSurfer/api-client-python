from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.signal_notice_request_data import SignalNoticeRequestData
    from ..models.signal_notice_source import SignalNoticeSource


T = TypeVar("T", bound="SignalNoticeRequest")


@_attrs_define
class SignalNoticeRequest:
    """
    Attributes:
        source (SignalNoticeSource): The instrument a notice is about: `LiveSourceRequest` without `type`, which is the
            subscription's to say, and with the instruments named one by one.
        ref (str | Unset): A string of yours. Sending the same `ref` to the same channel answers the notice it already
            made.
        expires_in (int | Unset): Seconds the notice is worth acting on. A delivery not made by then is `EXPIRED`.
            Default: 300.
        data (SignalNoticeRequestData | Unset): Anything else you want subscribers to read with the notice, as text: up
            to 16 entries, each key lower case (letters, digits, `_`, parts separated by `.`, up to 64 characters) and each
            value 1 to 256 characters with no control characters. It is shown with the delivery; it does not reach the
            strategy.
    """

    source: SignalNoticeSource
    ref: str | Unset = UNSET
    expires_in: int | Unset = 300
    data: SignalNoticeRequestData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source.to_dict()

        ref = self.ref

        expires_in = self.expires_in

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if expires_in is not UNSET:
            field_dict["expiresIn"] = expires_in
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.signal_notice_request_data import SignalNoticeRequestData
        from ..models.signal_notice_source import SignalNoticeSource

        d = dict(src_dict)
        source = SignalNoticeSource.from_dict(d.pop("source"))

        ref = d.pop("ref", UNSET)

        expires_in = d.pop("expiresIn", UNSET)

        _data = d.pop("data", UNSET)
        data: SignalNoticeRequestData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SignalNoticeRequestData.from_dict(_data)

        signal_notice_request = cls(
            source=source,
            ref=ref,
            expires_in=expires_in,
            data=data,
        )

        return signal_notice_request
