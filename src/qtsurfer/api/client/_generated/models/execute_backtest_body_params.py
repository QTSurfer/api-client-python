from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExecuteBacktestBodyParams")


@_attrs_define
class ExecuteBacktestBodyParams:
    """Strategy properties to apply to this run. Omit to run the strategy's declared
    defaults, which is exactly what a request without this field has always done.

    Each key is the `name` declared on the strategy's `@StrategyProperty`, which
    need NOT match the Java field it annotates — `GET`/`POST /strategy` returns
    `declaredProperties` for precisely this. A key naming no declared property is
    rejected: the job fails with the list of names the strategy does declare,
    rather than completing at the defaults and handing back a plausible result for
    parameters nobody chose.

    Scalars only — number, string or boolean. Ranges and lists belong to
    `executeSweep`; one request here is one run. `null` is not a value: leave the
    key out to keep a property at its default. Keys are made of letters, digits,
    `_`, `-` and dots, and may not be `strategyId`, `storeSignals`, `equityCurve`,
    `backtestEnabled` or `backtestFakeExecution` — those configure the job rather
    than the strategy.

        Example:
            {'ema.fast.period': 9, 'ema.slow.period': 21, 'risk.pct': 0.5}

    """

    additional_properties: dict[str, bool | float | str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        execute_backtest_body_params = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> bool | float | str:
                return cast(bool | float | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        execute_backtest_body_params.additional_properties = additional_properties
        return execute_backtest_body_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool | float | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool | float | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
