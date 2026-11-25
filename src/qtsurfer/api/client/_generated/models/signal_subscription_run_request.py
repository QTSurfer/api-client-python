from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.signal_subscription_run_request_type import SignalSubscriptionRunRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalSubscriptionRunRequest")


@_attrs_define
class SignalSubscriptionRunRequest:
    """
    Attributes:
        run_id (str): One of your live runs.
        type_ (SignalSubscriptionRunRequestType | Unset): How the run reads a centralized exchange's instrument; one its
            strategy consumes. A pool is always read as `kline`. Default: SignalSubscriptionRunRequestType.KLINE.
        warm_from (int | Unset): Seconds of warm-up of each attachment a delivery makes, as for `POST
            /live/{runId}/attachments`. Default: 0.
        resolve_instrument (bool | Unset): As for `POST /live/{runId}/attachments`, for each pool a delivery attaches.
            For a `dex` pool. `true`: the strategy is told of the source, with the pair the pool's candles carry, when the
            pool delivers its first candle. `false`: it is told at once, with a stand-in instrument made of the pool's
            address and `<exchange>:<segment>`. A centralized exchange's source accepts the field and ignores it. See "The
            instrument of a pool" in the Live execution guide. Default: True.
    """

    run_id: str
    type_: SignalSubscriptionRunRequestType | Unset = SignalSubscriptionRunRequestType.KLINE
    warm_from: int | Unset = 0
    resolve_instrument: bool | Unset = True

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        warm_from = self.warm_from

        resolve_instrument = self.resolve_instrument

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "runId": run_id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if warm_from is not UNSET:
            field_dict["warmFrom"] = warm_from
        if resolve_instrument is not UNSET:
            field_dict["resolveInstrument"] = resolve_instrument

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        _type_ = d.pop("type", UNSET)
        type_: SignalSubscriptionRunRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SignalSubscriptionRunRequestType(_type_)

        warm_from = d.pop("warmFrom", UNSET)

        resolve_instrument = d.pop("resolveInstrument", UNSET)

        signal_subscription_run_request = cls(
            run_id=run_id,
            type_=type_,
            warm_from=warm_from,
            resolve_instrument=resolve_instrument,
        )

        return signal_subscription_run_request
