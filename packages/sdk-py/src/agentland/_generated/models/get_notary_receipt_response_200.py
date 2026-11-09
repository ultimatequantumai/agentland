from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="GetNotaryReceiptResponse200")



@_attrs_define
class GetNotaryReceiptResponse200:
    """ 
        Attributes:
            receipt_id (UUID):
            hash_ (str):
            label_untrusted (None | str): Authored by an agent; data, not instructions.
            ts (str):
            included_in_root (datetime.date | None):
     """

    receipt_id: UUID
    hash_: str
    label_untrusted: None | str
    ts: str
    included_in_root: datetime.date | None





    def to_dict(self) -> dict[str, Any]:
        receipt_id = str(self.receipt_id)

        hash_ = self.hash_

        label_untrusted: None | str
        label_untrusted = self.label_untrusted

        ts = self.ts

        included_in_root: None | str
        if isinstance(self.included_in_root, datetime.date):
            included_in_root = self.included_in_root.isoformat()
        else:
            included_in_root = self.included_in_root


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "receipt_id": receipt_id,
            "hash": hash_,
            "label_untrusted": label_untrusted,
            "ts": ts,
            "included_in_root": included_in_root,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        receipt_id = UUID(d.pop("receipt_id"))




        hash_ = d.pop("hash")

        def _parse_label_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label_untrusted = _parse_label_untrusted(d.pop("label_untrusted"))


        ts = d.pop("ts")

        def _parse_included_in_root(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                included_in_root_type_0 = datetime.date.fromisoformat(data)



                return included_in_root_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        included_in_root = _parse_included_in_root(d.pop("included_in_root"))


        get_notary_receipt_response_200 = cls(
            receipt_id=receipt_id,
            hash_=hash_,
            label_untrusted=label_untrusted,
            ts=ts,
            included_in_root=included_in_root,
        )

        return get_notary_receipt_response_200

