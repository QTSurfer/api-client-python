from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_state import JobState
    from ..models.result_map import ResultMap


T = TypeVar("T", bound="BacktestJobResult")


@_attrs_define
class BacktestJobResult:
    """Backtest job result.

    Attributes:
        results (ResultMap): Execution result map. Always includes core fields (hostName, iops, strategyId, instrument).
            Yield metrics (pnlTotal, pnlTotalPercent, totalTrades, winRate, equityCurve, etc.) are present when the strategy
            emitted at least one trade. When signal storage is enabled, includes signal fields described below. `notices`
            carries what the run had to say about itself, and is absent when it had nothing.
        state (JobState): Information about a single job
    """

    results: ResultMap
    state: JobState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = self.results.to_dict()

        state = self.state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_state import JobState
        from ..models.result_map import ResultMap

        d = dict(src_dict)
        results = ResultMap.from_dict(d.pop("results"))

        state = JobState.from_dict(d.pop("state"))

        backtest_job_result = cls(
            results=results,
            state=state,
        )

        backtest_job_result.additional_properties = d
        return backtest_job_result

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
