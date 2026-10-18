from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.live_run_compact_stage import LiveRunCompactStage
from ..models.live_run_compact_visibility import LiveRunCompactVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_source import LiveSource


T = TypeVar("T", bound="LiveRunCompact")


@_attrs_define
class LiveRunCompact:
    """A run's state as returned by `PATCH /live/{runId}` — narrower than `LiveRun` (no `strategyId`, `params`, or
    `desired`), since this endpoint is addressed by `runId` alone.

        Attributes:
            run_id (str):
            visibility (LiveRunCompactVisibility):
            stage (LiveRunCompactStage):
            state (str):
            sources (list[LiveSource]):
            name (str | Unset):
            description (str | Unset):
    """

    run_id: str
    visibility: LiveRunCompactVisibility
    stage: LiveRunCompactStage
    state: str
    sources: list[LiveSource]
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        visibility = self.visibility.value

        stage = self.stage.value

        state = self.state

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "visibility": visibility,
                "stage": stage,
                "state": state,
                "sources": sources,
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
        run_id = d.pop("runId")

        visibility = LiveRunCompactVisibility(d.pop("visibility"))

        stage = LiveRunCompactStage(d.pop("stage"))

        state = d.pop("state")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = LiveSource.from_dict(sources_item_data)

            sources.append(sources_item)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        live_run_compact = cls(
            run_id=run_id,
            visibility=visibility,
            stage=stage,
            state=state,
            sources=sources,
            name=name,
            description=description,
        )

        live_run_compact.additional_properties = d
        return live_run_compact

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
