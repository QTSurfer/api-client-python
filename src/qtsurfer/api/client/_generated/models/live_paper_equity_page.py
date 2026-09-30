from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_paper_equity_page_links import LivePaperEquityPageLinks
    from ..models.live_paper_equity_point import LivePaperEquityPoint


T = TypeVar("T", bound="LivePaperEquityPage")


@_attrs_define
class LivePaperEquityPage:
    """
    Attributes:
        points (list[LivePaperEquityPoint]):
        field_links (LivePaperEquityPageLinks | Unset):
    """

    points: list[LivePaperEquityPoint]
    field_links: LivePaperEquityPageLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = []
        for points_item_data in self.points:
            points_item = points_item_data.to_dict()
            points.append(points_item)

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_paper_equity_page_links import LivePaperEquityPageLinks
        from ..models.live_paper_equity_point import LivePaperEquityPoint

        d = dict(src_dict)
        points = []
        _points = d.pop("points")
        for points_item_data in _points:
            points_item = LivePaperEquityPoint.from_dict(points_item_data)

            points.append(points_item)

        _field_links = d.pop("_links", UNSET)
        field_links: LivePaperEquityPageLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = LivePaperEquityPageLinks.from_dict(_field_links)

        live_paper_equity_page = cls(
            points=points,
            field_links=field_links,
        )

        live_paper_equity_page.additional_properties = d
        return live_paper_equity_page

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
