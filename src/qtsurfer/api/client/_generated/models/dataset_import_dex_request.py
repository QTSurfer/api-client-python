from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_import_dex_request_id import DatasetImportDexRequestId
from ..models.dataset_import_dex_request_network import DatasetImportDexRequestNetwork
from ..models.dataset_import_dex_request_version import DatasetImportDexRequestVersion
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetImportDexRequest")


@_attrs_define
class DatasetImportDexRequest:
    """The `dex` source's own fields — required when `type` is `dex`. `id`/`version` are required
    for a plain (native-cadence) import; both are ignored if the top-level `cadence` requested
    pre-aggregated candles instead, since that path needs neither a protocol nor a version
    distinction.

        Example:
            {'network': 'ethereum', 'id': 'uniswap', 'version': 'v3', 'contract':
                '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640'}

        Attributes:
            network (DatasetImportDexRequestNetwork): Which chain the pool/pair lives on. Example: ethereum.
            contract (str): The pool (v3) or pair (v2) contract address. Example:
                0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640.
            id (DatasetImportDexRequestId | Unset): Which on-chain DEX protocol `contract` implements. Required unless the
                top-level
                `cadence` requested pre-aggregated candles, in which case it's ignored.
                 Example: uniswap.
            version (DatasetImportDexRequestVersion | Unset): Uniswap version the pool/pair contract implements. Required
                unless the top-level
                `cadence` requested pre-aggregated candles, in which case it's ignored.
                 Example: v3.
            factory (str | Unset): The factory that deployed `contract`. Optional — when omitted, it is discovered
                on-chain from `contract` itself at fetch time. Supply it explicitly only if you
                already know it, or the pool/pair belongs to a factory other than the canonical one
                for `network`/`version`. Either way, the pool/pair is validated against whichever
                factory is used before anything is fetched — a wrong or unrelated factory fails the
                import rather than silently fetching from the wrong pool. Ignored if the top-level
                `cadence` requested pre-aggregated candles.
    """

    network: DatasetImportDexRequestNetwork
    contract: str
    id: DatasetImportDexRequestId | Unset = UNSET
    version: DatasetImportDexRequestVersion | Unset = UNSET
    factory: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network.value

        contract = self.contract

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.value

        version: str | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.value

        factory = self.factory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
                "contract": contract,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if factory is not UNSET:
            field_dict["factory"] = factory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network = DatasetImportDexRequestNetwork(d.pop("network"))

        contract = d.pop("contract")

        _id = d.pop("id", UNSET)
        id: DatasetImportDexRequestId | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = DatasetImportDexRequestId(_id)

        _version = d.pop("version", UNSET)
        version: DatasetImportDexRequestVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatasetImportDexRequestVersion(_version)

        factory = d.pop("factory", UNSET)

        dataset_import_dex_request = cls(
            network=network,
            contract=contract,
            id=id,
            version=version,
            factory=factory,
        )

        dataset_import_dex_request.additional_properties = d
        return dataset_import_dex_request

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
