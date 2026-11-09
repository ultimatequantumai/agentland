from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetNotaryProofResponse200Type1Proof")



@_attrs_define
class GetNotaryProofResponse200Type1Proof:
    """ 
        Attributes:
            leaf_index (int):
            tree_size (int):
            siblings (list[str]):
     """

    leaf_index: int
    tree_size: int
    siblings: list[str]





    def to_dict(self) -> dict[str, Any]:
        leaf_index = self.leaf_index

        tree_size = self.tree_size

        siblings = self.siblings




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "leaf_index": leaf_index,
            "tree_size": tree_size,
            "siblings": siblings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        leaf_index = d.pop("leaf_index")

        tree_size = d.pop("tree_size")

        siblings = cast(list[str], d.pop("siblings"))


        get_notary_proof_response_200_type_1_proof = cls(
            leaf_index=leaf_index,
            tree_size=tree_size,
            siblings=siblings,
        )

        return get_notary_proof_response_200_type_1_proof

