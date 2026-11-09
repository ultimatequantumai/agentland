from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_field_snapshot_response_200k import GetFieldSnapshotResponse200K
from ..models.get_field_snapshot_response_200v import GetFieldSnapshotResponse200V
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_field_snapshot_response_200c_item_item_type_1 import GetFieldSnapshotResponse200CItemItemType1
  from ..models.get_field_snapshot_response_200r_item_item_type_1 import GetFieldSnapshotResponse200RItemItemType1





T = TypeVar("T", bound="GetFieldSnapshotResponse200")



@_attrs_define
class GetFieldSnapshotResponse200:
    """ 
        Attributes:
            v (GetFieldSnapshotResponse200V):
            k (GetFieldSnapshotResponse200K):
            t (str):
            r (list[list[GetFieldSnapshotResponse200RItemItemType1 | str]]):
            slot (int): 10 s slot of the newest ring row folded into this key
            q (list[list[Any]] | Unset): key: every open light, sorted by id
            c (list[list[GetFieldSnapshotResponse200CItemItemType1 | int]] | Unset): delta: [index into the previous state's
                sorted ids, changed fields]
            a (list[list[Any]] | Unset): delta: added lights
            x (list[str] | Unset): delta: removed light ids
     """

    v: GetFieldSnapshotResponse200V
    k: GetFieldSnapshotResponse200K
    t: str
    r: list[list[GetFieldSnapshotResponse200RItemItemType1 | str]]
    slot: int
    q: list[list[Any]] | Unset = UNSET
    c: list[list[GetFieldSnapshotResponse200CItemItemType1 | int]] | Unset = UNSET
    a: list[list[Any]] | Unset = UNSET
    x: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_field_snapshot_response_200c_item_item_type_1 import GetFieldSnapshotResponse200CItemItemType1 # noqa: PLC0415
        from ..models.get_field_snapshot_response_200r_item_item_type_1 import GetFieldSnapshotResponse200RItemItemType1 # noqa: PLC0415
        v = self.v.value

        k = self.k.value

        t = self.t

        r = []
        for r_item_data in self.r:
            r_item = []
            for r_item_item_data in r_item_data:
                r_item_item: dict[str, Any] | str
                if isinstance(r_item_item_data, GetFieldSnapshotResponse200RItemItemType1):
                    r_item_item = r_item_item_data.to_dict()
                else:
                    r_item_item = r_item_item_data
                r_item.append(r_item_item)


            r.append(r_item)



        slot = self.slot

        q: list[list[Any]] | Unset = UNSET
        if not isinstance(self.q, Unset):
            q = []
            for q_item_data in self.q:
                q_item = q_item_data


                q.append(q_item)



        c: list[list[dict[str, Any] | int]] | Unset = UNSET
        if not isinstance(self.c, Unset):
            c = []
            for c_item_data in self.c:
                c_item = []
                for c_item_item_data in c_item_data:
                    c_item_item: dict[str, Any] | int
                    if isinstance(c_item_item_data, GetFieldSnapshotResponse200CItemItemType1):
                        c_item_item = c_item_item_data.to_dict()
                    else:
                        c_item_item = c_item_item_data
                    c_item.append(c_item_item)


                c.append(c_item)



        a: list[list[Any]] | Unset = UNSET
        if not isinstance(self.a, Unset):
            a = []
            for a_item_data in self.a:
                a_item = a_item_data


                a.append(a_item)



        x: list[str] | Unset = UNSET
        if not isinstance(self.x, Unset):
            x = self.x




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "v": v,
            "k": k,
            "t": t,
            "r": r,
            "slot": slot,
        })
        if q is not UNSET:
            field_dict["q"] = q
        if c is not UNSET:
            field_dict["c"] = c
        if a is not UNSET:
            field_dict["a"] = a
        if x is not UNSET:
            field_dict["x"] = x

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_field_snapshot_response_200c_item_item_type_1 import GetFieldSnapshotResponse200CItemItemType1 # noqa: PLC0415
        from ..models.get_field_snapshot_response_200r_item_item_type_1 import GetFieldSnapshotResponse200RItemItemType1 # noqa: PLC0415
        d = dict(src_dict)
        v = GetFieldSnapshotResponse200V(d.pop("v"))




        k = GetFieldSnapshotResponse200K(d.pop("k"))




        t = d.pop("t")

        r = []
        _r = d.pop("r")
        for r_item_data in (_r):
            r_item = []
            _r_item = r_item_data
            for r_item_item_data in (_r_item):
                def _parse_r_item_item(data: object) -> GetFieldSnapshotResponse200RItemItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        r_item_item_type_1 = GetFieldSnapshotResponse200RItemItemType1.from_dict(data)



                        return r_item_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(GetFieldSnapshotResponse200RItemItemType1 | str, data)

                r_item_item = _parse_r_item_item(r_item_item_data)

                r_item.append(r_item_item)

            r.append(r_item)


        slot = d.pop("slot")

        _q = d.pop("q", UNSET)
        q: list[list[Any]] | Unset = UNSET
        if _q is not UNSET:
            q = []
            for q_item_data in _q:
                q_item = cast(list[Any], q_item_data)

                q.append(q_item)


        _c = d.pop("c", UNSET)
        c: list[list[GetFieldSnapshotResponse200CItemItemType1 | int]] | Unset = UNSET
        if _c is not UNSET:
            c = []
            for c_item_data in _c:
                c_item = []
                _c_item = c_item_data
                for c_item_item_data in (_c_item):
                    def _parse_c_item_item(data: object) -> GetFieldSnapshotResponse200CItemItemType1 | int:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            c_item_item_type_1 = GetFieldSnapshotResponse200CItemItemType1.from_dict(data)



                            return c_item_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(GetFieldSnapshotResponse200CItemItemType1 | int, data)

                    c_item_item = _parse_c_item_item(c_item_item_data)

                    c_item.append(c_item_item)

                c.append(c_item)


        _a = d.pop("a", UNSET)
        a: list[list[Any]] | Unset = UNSET
        if _a is not UNSET:
            a = []
            for a_item_data in _a:
                a_item = cast(list[Any], a_item_data)

                a.append(a_item)


        x = cast(list[str], d.pop("x", UNSET))


        get_field_snapshot_response_200 = cls(
            v=v,
            k=k,
            t=t,
            r=r,
            slot=slot,
            q=q,
            c=c,
            a=a,
            x=x,
        )


        get_field_snapshot_response_200.additional_properties = d
        return get_field_snapshot_response_200

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
