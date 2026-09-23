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
        stage (LiveRunStage): A new run always starts `SANDBOX` — a trial run compared against a second execution for
            agreement — and moves to `LIVE` once it passes.
        state (str): `STARTING` until first observed running; otherwise the runner's own reported state (e.g.
            `RUNNING`).
        desired (LiveRunDesired): What you last asked for. `state` can lag this briefly after `DELETE`.
        sources (list[LiveSource]):
        params (LiveRunParams):
        params_version (int): Increments on every accepted `PUT .../params` call, including one that resends the current
            values.
        relay (bool): Whether this run's signals are being relayed over the WebSocket channel described in the "Live
            execution" guide, right now. This is the effective value — `false` on a `sandbox` run regardless of what was
            requested at start; matches the requested value once `stage` reaches `live`.
        started_at_ms (int): Epoch milliseconds.
        name (str | Unset):
        description (str | Unset):
        reason (str | Unset): Present only when the run stopped because it exceeded its resource allowance.
        gate (LiveRunGate | Unset): The sandbox trial's promotion verdict, once one exists. Shape is not yet stabilized
            as public API — treat as opaque diagnostics.
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
