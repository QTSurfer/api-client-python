from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_run_desired import LiveRunDesired
from ..models.live_run_stage import LiveRunStage
from ..models.live_run_visibility import LiveRunVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_paper_config import LivePaperConfig
    from ..models.live_run_gate import LiveRunGate
    from ..models.live_run_params import LiveRunParams
    from ..models.live_source import LiveSource


T = TypeVar("T", bound="LiveRun")


@_attrs_define
class LiveRun:
    """A live run's full state, as returned by starting, reading, or stopping it through its strategy.

    Attributes:
        strategy_id (str): Unique identifier for a compiled strategy, derived from the source itself: the same code
            always yields the same id, for every caller. How much formatting the id ignores depends on
            the language — see `POST /strategy` for exactly which rewrites preserve it and which do
            not.
             Example: 6bsh31ikwkuivhtgcoa6s4.
        run_id (str): This run's own id — its canonical identity for `PATCH`/`PUT .../params` and for `GET
            /live/public`.
        visibility (LiveRunVisibility):
        stage (LiveRunStage): A new run always starts `SANDBOX`, a 24-hour trial in which it is compared against a
            second execution and checked for resource use and stability. A run that passes moves to `LIVE` automatically
            when the 24 hours are up.
        state (str): The run's health right now: `STARTING` (no runner has reported on it yet), `RUNNING`, `LAGGING`
            (behind the market data, usually while catching up; clears by itself), `HUNG` (stuck inside one strategy call
            for longer than allowed; clears when it returns), `DEGRADED` (its independent executions produced different
            signals), `FAILED` (refused, could not start or failed while running; `reason` says why) or `STOPPED`.
            `LAGGING`, `HUNG` and `DEGRADED` come and go on a running run. The set may grow: read an unknown value as a
            running run with something to look at. See the Live execution guide.
        desired (LiveRunDesired): What you last asked for. `state` can lag this briefly after `DELETE`.
        sources (list[LiveSource]):
        params (LiveRunParams):
        params_version (int): Increments on every accepted `PUT .../params` call, including one that resends the current
            values.
        relay (bool): Whether this run's signals are relayed over the WebSocket channel described in the "Live
            execution" guide. It is the value requested at start, in either stage.
        started_at_ms (int): Epoch milliseconds.
        name (str | Unset):
        description (str | Unset):
        reason (str | Unset): Why the run stopped or failed, when there is something to say; absent otherwise. It is
            never a
            stack trace or an internal message. Either `resource: ...` (the platform stopped the run for
            exceeding its resource allowance; the text says which limit) or one of a fixed set of sentences for
            a `FAILED` run: the strategy cannot consume the source type the run was started with, the run's
            definition was refused, the run could not start after several attempts, the strategy failed while
            processing data, the run lost its data feed, or the generic `The run failed.`. The set may grow:
            read an unrecognised sentence as a failure and do not parse it. A `FAILED` run usually stays
            `desired: RUNNING` until you stop it, and counts as active (`409` on a new start, and toward your
            live-run limit) until then; one that can never run because its strategy cannot consume its source
            type is stopped by the platform itself (`desired: STOPPED`), so it holds no place.
        gate (LiveRunGate | Unset): The sandbox trial's promotion verdict. Absent for the whole 24-hour trial and
            present once it ends, so an absent `gate` means the trial has not finished. `passed` is the verdict; the rest is
            diagnostic detail whose shape is not yet stabilized as public API: treat it as opaque.
        paper (LivePaperConfig | Unset): Paper trading for this run: the same economics as a backtest's `baseConfig`
            (same fields,
            defaults and limits), plus `output`. An empty object takes every default. Each quote
            currency the run trades gets its own simulated account, opened with `initialFunding` in
            that currency; accounts are never added together. As returned on a run, the block is
            normalised: `feeRate` is resolved into `buyFeeRate`/`sellFeeRate` and defaults are filled
            in.
    """

    strategy_id: str
    run_id: str
    visibility: LiveRunVisibility
    stage: LiveRunStage
    state: str
    desired: LiveRunDesired
    sources: list[LiveSource]
    params: LiveRunParams
    params_version: int
    relay: bool
    started_at_ms: int
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    reason: str | Unset = UNSET
    gate: LiveRunGate | Unset = UNSET
    paper: LivePaperConfig | Unset = UNSET
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

        params = self.params.to_dict()

        params_version = self.params_version

        relay = self.relay

        started_at_ms = self.started_at_ms

        name = self.name

        description = self.description

        reason = self.reason

        gate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gate, Unset):
            gate = self.gate.to_dict()

        paper: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paper, Unset):
            paper = self.paper.to_dict()

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
                "params": params,
                "paramsVersion": params_version,
                "relay": relay,
                "startedAtMs": started_at_ms,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if reason is not UNSET:
            field_dict["reason"] = reason
        if gate is not UNSET:
            field_dict["gate"] = gate
        if paper is not UNSET:
            field_dict["paper"] = paper

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_paper_config import LivePaperConfig
        from ..models.live_run_gate import LiveRunGate
        from ..models.live_run_params import LiveRunParams
        from ..models.live_source import LiveSource

        d = dict(src_dict)
        strategy_id = d.pop("strategyId")

        run_id = d.pop("runId")

        visibility = LiveRunVisibility(d.pop("visibility"))

        stage = LiveRunStage(d.pop("stage"))

        state = d.pop("state")

        desired = LiveRunDesired(d.pop("desired"))

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = LiveSource.from_dict(sources_item_data)

            sources.append(sources_item)

        params = LiveRunParams.from_dict(d.pop("params"))

        params_version = d.pop("paramsVersion")

        relay = d.pop("relay")

        started_at_ms = d.pop("startedAtMs")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        reason = d.pop("reason", UNSET)

        _gate = d.pop("gate", UNSET)
        gate: LiveRunGate | Unset
        if isinstance(_gate, Unset):
            gate = UNSET
        else:
            gate = LiveRunGate.from_dict(_gate)

        _paper = d.pop("paper", UNSET)
        paper: LivePaperConfig | Unset
        if isinstance(_paper, Unset):
            paper = UNSET
        else:
            paper = LivePaperConfig.from_dict(_paper)

        live_run = cls(
            strategy_id=strategy_id,
            run_id=run_id,
            visibility=visibility,
            stage=stage,
            state=state,
            desired=desired,
            sources=sources,
            params=params,
            params_version=params_version,
            relay=relay,
            started_at_ms=started_at_ms,
            name=name,
            description=description,
            reason=reason,
            gate=gate,
            paper=paper,
        )

        live_run.additional_properties = d
        return live_run

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
