from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_source import LiveSource


T = TypeVar("T", bound="PublicLiveRun")


@_attrs_define
class PublicLiveRun:
    """A run as it appears in `GET /live/public` — never reveals who owns it or which strategy it runs.

    Attributes:
        run_id (str):
        sources (list[LiveSource]):
        state (str):
        created_at_ms (int):
        name (str | Unset):
        description (str | Unset):
    """

    run_id: str
    sources: list[LiveSource]
    state: str
    created_at_ms: int
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        state = self.state

        created_at_ms = self.created_at_ms

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runId": run_id,
                "sources": sources,
                "state": state,
                "createdAtMs": created_at_ms,
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

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = LiveSource.from_dict(sources_item_data)

            sources.append(sources_item)

        state = d.pop("state")

        created_at_ms = d.pop("createdAtMs")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        public_live_run = cls(
            run_id=run_id,
            sources=sources,
            state=state,
            created_at_ms=created_at_ms,
            name=name,
            description=description,
        )

        public_live_run.additional_properties = d
        return public_live_run

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
