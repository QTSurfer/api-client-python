from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sweep_base_config_fee_leg import SweepBaseConfigFeeLeg
from ..types import UNSET, Unset

T = TypeVar("T", bound="SweepBaseConfig")


@_attrs_define
class SweepBaseConfig:
    """
    Attributes:
        initial_funding (float | Unset):  Default: 100.0.
        fee_rate (float | Unset):  Default: 0.001.
        buy_fee_rate (float | Unset):
        sell_fee_rate (float | Unset):
        fee_leg (SweepBaseConfigFeeLeg | Unset):  Default: SweepBaseConfigFeeLeg.RECEIVED.
        percent_amount_to_lock (float | Unset):
    """

    initial_funding: float | Unset = 100.0
    fee_rate: float | Unset = 0.001
    buy_fee_rate: float | Unset = UNSET
    sell_fee_rate: float | Unset = UNSET
    fee_leg: SweepBaseConfigFeeLeg | Unset = SweepBaseConfigFeeLeg.RECEIVED
    percent_amount_to_lock: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        initial_funding = self.initial_funding

        fee_rate = self.fee_rate

        buy_fee_rate = self.buy_fee_rate

        sell_fee_rate = self.sell_fee_rate

        fee_leg: str | Unset = UNSET
        if not isinstance(self.fee_leg, Unset):
            fee_leg = self.fee_leg.value

        percent_amount_to_lock = self.percent_amount_to_lock

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initial_funding is not UNSET:
            field_dict["initialFunding"] = initial_funding
        if fee_rate is not UNSET:
            field_dict["feeRate"] = fee_rate
        if buy_fee_rate is not UNSET:
            field_dict["buyFeeRate"] = buy_fee_rate
        if sell_fee_rate is not UNSET:
            field_dict["sellFeeRate"] = sell_fee_rate
        if fee_leg is not UNSET:
            field_dict["feeLeg"] = fee_leg
        if percent_amount_to_lock is not UNSET:
            field_dict["percentAmountToLock"] = percent_amount_to_lock

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        initial_funding = d.pop("initialFunding", UNSET)

        fee_rate = d.pop("feeRate", UNSET)

        buy_fee_rate = d.pop("buyFeeRate", UNSET)

        sell_fee_rate = d.pop("sellFeeRate", UNSET)

        _fee_leg = d.pop("feeLeg", UNSET)
        fee_leg: SweepBaseConfigFeeLeg | Unset
        if isinstance(_fee_leg, Unset):
            fee_leg = UNSET
        else:
            fee_leg = SweepBaseConfigFeeLeg(_fee_leg)

        percent_amount_to_lock = d.pop("percentAmountToLock", UNSET)

        sweep_base_config = cls(
            initial_funding=initial_funding,
            fee_rate=fee_rate,
            buy_fee_rate=buy_fee_rate,
            sell_fee_rate=sell_fee_rate,
            fee_leg=fee_leg,
            percent_amount_to_lock=percent_amount_to_lock,
        )

        sweep_base_config.additional_properties = d
        return sweep_base_config

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
