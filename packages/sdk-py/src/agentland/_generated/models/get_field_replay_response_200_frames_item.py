from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_field_replay_response_200_frames_item_frame import GetFieldReplayResponse200FramesItemFrame





T = TypeVar("T", bound="GetFieldReplayResponse200FramesItem")



@_attrs_define
class GetFieldReplayResponse200FramesItem:
    """ 
        Attributes:
            slot (int):
            frame (GetFieldReplayResponse200FramesItemFrame): Field frame v1 (C1): a keyframe or a delta against the
                previous frame.
     """

    slot: int
    frame: GetFieldReplayResponse200FramesItemFrame
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_field_replay_response_200_frames_item_frame import GetFieldReplayResponse200FramesItemFrame # noqa: PLC0415
        slot = self.slot

        frame = self.frame.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "slot": slot,
            "frame": frame,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_field_replay_response_200_frames_item_frame import GetFieldReplayResponse200FramesItemFrame # noqa: PLC0415
        d = dict(src_dict)
        slot = d.pop("slot")

        frame = GetFieldReplayResponse200FramesItemFrame.from_dict(d.pop("frame"))




        get_field_replay_response_200_frames_item = cls(
            slot=slot,
            frame=frame,
        )


        get_field_replay_response_200_frames_item.additional_properties = d
        return get_field_replay_response_200_frames_item

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
