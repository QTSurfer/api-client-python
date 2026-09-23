from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_run_summary_desired import LiveRunSummaryDesired
from ..models.live_run_summary_stage import LiveRunSummaryStage
from ..models.live_run_summary_visibility import LiveRunSummaryVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_source import LiveSource


T = TypeVar("T", bound="LiveRunSummary")


@_attrs_define
class LiveRunSummary:
    """A run as it appears in `GET /live` — one of your own, narrower than `LiveRun` (no `params`, `paramsVersion`,
    `relay`, or `gate`), since listing stays cheap regardless of how many runs you have. Check a specific run's full
    state with `GET /strategy/{strategyId}/live`.

        Attributes:
            strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
                always yields the same id, for every caller. How much formatting the id ignores depends on
                the language — see `POST /strategy` for exactly which rewrites preserve it and which do
                not.
                 Example: 6bsh31ikwkuivhtgcoa6s4.
            run_id (str): This run's own id — its canonical identity for `PATCH`/`PUT .../params` and for `GET
                /live/public`.
            visibility (LiveRunSummaryVisibility):
            stage (LiveRunSummaryStage): A new run always starts `SANDBOX` — a trial run compared against a second execution
                for agreement — and moves to `LIVE` once it passes.
            state (str): `STARTING` until first observed running; otherwise the runner's own reported state (e.g.
                `RUNNING`).
            desired (LiveRunSummaryDesired): What you last asked for. `state` can lag this briefly after `DELETE`.
            sources (list[LiveSource]):
            created_at_ms (int): Epoch milliseconds this run was started.
            started_at_ms (int): Epoch milliseconds.
            name (str | Unset):
            description (str | Unset):
    """

    strategy_id: str
    run_id: str
    visibility: LiveRunSummaryVisibility
    stage: LiveRunSummaryStage
    state: str
    desired: LiveRunSummaryDesired
    sources: list[LiveSource]
    created_at_ms: int
    started_at_ms: int
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy_id = self.strategy_id

        run_id = self.run_id

        visibility = self.visibility.value

        stage = self.stage.value

        state = self.state

        desired = self.desired.value

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        created_at_ms = self.created_at_ms

        started_at_ms = self.started_at_ms

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategyId": strategy_id,
                "runId": run_id,
                "visibility": visibility,
                "stage": stage,
                "state": state,
                "desired": desired,
                "sources": sources,
                "createdAtMs": created_at_ms,
                "startedAtMs": started_at_ms,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_source import LiveSource

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        run_id = d.pop("runId")

        visibility = LiveRunSummaryVisibility(d.pop("visibility"))

        stage = LiveRunSummaryStage(d.pop("stage"))

        state = d.pop("state")

        desired = LiveRunSummaryDesired(d.pop("desired"))

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = LiveSource.from_dict(sources_item_data)

            sources.append(sources_item)

        created_at_ms = d.pop("createdAtMs")

        started_at_ms = d.pop("startedAtMs")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        live_run_summary = cls(
            strategy_id=strategy_id,
            run_id=run_id,
            visibility=visibility,
            stage=stage,
            state=state,
            desired=desired,
            sources=sources,
            created_at_ms=created_at_ms,
            started_at_ms=started_at_ms,
            name=name,
            description=description,
        )

        live_run_summary.additional_properties = d
        return live_run_summary

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
