from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_signal_stage import LiveSignalStage
from ..models.live_signal_type import LiveSignalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_signal_data import LiveSignalData
    from ..models.live_signal_instrument import LiveSignalInstrument
    from ..models.live_signal_order_type_0 import LiveSignalOrderType0


T = TypeVar("T", bound="LiveSignal")


@_attrs_define
class LiveSignal:
    """One signal, in the same shape the real-time signal channel delivers.

    Attributes:
        v (int): Envelope schema version.
        signal_id (str): Stable id for this exact signal — dedupe on it across reconnects or overlapping reads.
        run_id (str):
        stage (LiveSignalStage): The stage the run was in when this signal was produced.
        type_ (LiveSignalType): `paper` items appear only for a run whose `paper.output` is `mix`; they are not relayed
            over the WebSocket channel.
        event_ts_ms (int): Market time the signal was produced.
        emitted_at_ms (int): Time it was published — always at or after `eventTsMs`.
        instrument (LiveSignalInstrument | None): The instrument the signal is about. `null` only for a `paper` item
            about a whole account (`equity`, `mark`, `kpi`), whose `data.currency` names the account.
        digest (str): Content hash, for checking that two independent deliveries of the same signal agree.
        params_version (int | Unset): The parameter set in force when this signal was produced.
        kind (None | str | Unset): `BUY`/`SELL` for a `hint`, the command name for a `command`; for `paper`, what the
            item is: `fill`, `trade`, `equity`, `mark`, `kpi` or `gap`. Absent otherwise.
        order (LiveSignalOrderType0 | None | Unset): Present only for a `hint`.
        data (LiveSignalData | Unset): The signal's own free-form payload, what the strategy put there with
            `signal.set(...)`. Whoever may read the run may read it, so on a `public` run it is public. A signal whose
            `data` is over 8 KiB (8,192 bytes of its JSON) is not pushed on the WebSocket channel, and `GET
            /live/{runId}/signals` returns it whole.
        regenerated (bool | Unset): `true` only for a signal republished to fill a gap in the record.
    """

    v: int
    signal_id: str
    run_id: str
    stage: LiveSignalStage
    type_: LiveSignalType
    event_ts_ms: int
    emitted_at_ms: int
    instrument: LiveSignalInstrument | None
    digest: str
    params_version: int | Unset = UNSET
    kind: None | str | Unset = UNSET
    order: LiveSignalOrderType0 | None | Unset = UNSET
    data: LiveSignalData | Unset = UNSET
    regenerated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.live_signal_instrument import LiveSignalInstrument
        from ..models.live_signal_order_type_0 import LiveSignalOrderType0

        v = self.v

        signal_id = self.signal_id

        run_id = self.run_id

        stage = self.stage.value

        type_ = self.type_.value

        event_ts_ms = self.event_ts_ms

        emitted_at_ms = self.emitted_at_ms

        instrument: dict[str, Any] | None
        if isinstance(self.instrument, LiveSignalInstrument):
            instrument = self.instrument.to_dict()
        else:
            instrument = self.instrument

        digest = self.digest

        params_version = self.params_version

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        order: dict[str, Any] | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, LiveSignalOrderType0):
            order = self.order.to_dict()
        else:
            order = self.order

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        regenerated = self.regenerated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "v": v,
                "signalId": signal_id,
                "runId": run_id,
                "stage": stage,
                "type": type_,
                "eventTsMs": event_ts_ms,
                "emittedAtMs": emitted_at_ms,
                "instrument": instrument,
                "digest": digest,
            }
        )
        if params_version is not UNSET:
            field_dict["paramsVersion"] = params_version
        if kind is not UNSET:
            field_dict["kind"] = kind
        if order is not UNSET:
            field_dict["order"] = order
        if data is not UNSET:
            field_dict["data"] = data
        if regenerated is not UNSET:
            field_dict["regenerated"] = regenerated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_signal_data import LiveSignalData
        from ..models.live_signal_instrument import LiveSignalInstrument
        from ..models.live_signal_order_type_0 import LiveSignalOrderType0

        d = dict(src_dict)
        v = d.pop("v")

        signal_id = d.pop("signalId")

        run_id = d.pop("runId")

        stage = LiveSignalStage(d.pop("stage"))

        type_ = LiveSignalType(d.pop("type"))

        event_ts_ms = d.pop("eventTsMs")

        emitted_at_ms = d.pop("emittedAtMs")

        def _parse_instrument(data: object) -> LiveSignalInstrument | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_0 = LiveSignalInstrument.from_dict(data)

                return instrument_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiveSignalInstrument | None, data)

        instrument = _parse_instrument(d.pop("instrument"))

        digest = d.pop("digest")

        params_version = d.pop("paramsVersion", UNSET)

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_order(data: object) -> LiveSignalOrderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_live_signal_order_type_0 = LiveSignalOrderType0.from_dict(data)

                return componentsschemas_live_signal_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiveSignalOrderType0 | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        _data = d.pop("data", UNSET)
        data: LiveSignalData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = LiveSignalData.from_dict(_data)

        regenerated = d.pop("regenerated", UNSET)

        live_signal = cls(
            v=v,
            signal_id=signal_id,
            run_id=run_id,
            stage=stage,
            type_=type_,
            event_ts_ms=event_ts_ms,
            emitted_at_ms=emitted_at_ms,
            instrument=instrument,
            digest=digest,
            params_version=params_version,
            kind=kind,
            order=order,
            data=data,
            regenerated=regenerated,
        )

        live_signal.additional_properties = d
        return live_signal

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
