from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_live_request_visibility import StartLiveRequestVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_source import LiveSource
    from ..models.start_live_request_params import StartLiveRequestParams


T = TypeVar("T", bound="StartLiveRequest")


@_attrs_define
class StartLiveRequest:
    """
    Attributes:
        sources (list[LiveSource]):
        params (StartLiveRequestParams | Unset): Strategy parameters to start with. Opaque key/value pairs — see this
            strategy's own `declaredProperties` (from `POST /strategy`) for the keys it accepts.
        visibility (StartLiveRequestVisibility | Unset): A `public` run appears in `GET /live/public` and its signal
            channel accepts subscriptions from anyone, not only you. Default: StartLiveRequestVisibility.PRIVATE.
        relay (bool | Unset): Request that this run's signals be relayed over its WebSocket channel once it reaches the
            `live` stage — see the "Live execution" guide. Has no effect while the run is still in the `sandbox` stage,
            regardless of this value. Default: False.
        name (str | Unset):
        description (str | Unset):
    """

    sources: list[LiveSource]
    params: StartLiveRequestParams | Unset = UNSET
    visibility: StartLiveRequestVisibility | Unset = StartLiveRequestVisibility.PRIVATE
    relay: bool | Unset = False
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        relay = self.relay

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sources": sources,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if relay is not UNSET:
            field_dict["relay"] = relay
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_source import LiveSource
        from ..models.start_live_request_params import StartLiveRequestParams

        d = dict(src_dict)
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = LiveSource.from_dict(sources_item_data)

            sources.append(sources_item)

        _params = d.pop("params", UNSET)
        params: StartLiveRequestParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = StartLiveRequestParams.from_dict(_params)

        _visibility = d.pop("visibility", UNSET)
        visibility: StartLiveRequestVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = StartLiveRequestVisibility(_visibility)

        relay = d.pop("relay", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        start_live_request = cls(
            sources=sources,
            params=params,
            visibility=visibility,
            relay=relay,
            name=name,
            description=description,
        )

        start_live_request.additional_properties = d
        return start_live_request

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
