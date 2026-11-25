from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.signal_subscription_run_type import SignalSubscriptionRunType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignalSubscriptionRun")


@_attrs_define
class SignalSubscriptionRun:
    """
    Attributes:
        run_id (str):
        type_ (SignalSubscriptionRunType):
        warm_from (int):
        created_at_ms (int):
        resolve_instrument (bool | Unset):
    """

    run_id: str
    type_: SignalSubscriptionRunType
    warm_from: int
    created_at_ms: int
    resolve_instrument: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        type_ = self.type_.value

        warm_from = self.warm_from

        created_at_ms = self.created_at_ms

        resolve_instrument = self.resolve_instrument

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "type": type_,
                "warmFrom": warm_from,
                "createdAtMs": created_at_ms,
            }
        )
        if resolve_instrument is not UNSET:
            field_dict["resolveInstrument"] = resolve_instrument

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        type_ = SignalSubscriptionRunType(d.pop("type"))

        warm_from = d.pop("warmFrom")

        created_at_ms = d.pop("createdAtMs")

        resolve_instrument = d.pop("resolveInstrument", UNSET)

        signal_subscription_run = cls(
            run_id=run_id,
            type_=type_,
            warm_from=warm_from,
            created_at_ms=created_at_ms,
            resolve_instrument=resolve_instrument,
        )

        signal_subscription_run.additional_properties = d
        return signal_subscription_run

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
