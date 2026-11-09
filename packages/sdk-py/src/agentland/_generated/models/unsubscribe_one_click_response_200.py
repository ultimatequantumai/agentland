from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.unsubscribe_one_click_response_200_category_type_1 import UnsubscribeOneClickResponse200CategoryType1
from ..models.unsubscribe_one_click_response_200_category_type_2_type_1 import UnsubscribeOneClickResponse200CategoryType2Type1
from ..models.unsubscribe_one_click_response_200_category_type_3_type_1 import UnsubscribeOneClickResponse200CategoryType3Type1
from typing import cast






T = TypeVar("T", bound="UnsubscribeOneClickResponse200")



@_attrs_define
class UnsubscribeOneClickResponse200:
    """ 
        Attributes:
            category (None | UnsubscribeOneClickResponse200CategoryType1 | UnsubscribeOneClickResponse200CategoryType2Type1
                | UnsubscribeOneClickResponse200CategoryType3Type1):
     """

    category: None | UnsubscribeOneClickResponse200CategoryType1 | UnsubscribeOneClickResponse200CategoryType2Type1 | UnsubscribeOneClickResponse200CategoryType3Type1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category: None | str
        if isinstance(self.category, UnsubscribeOneClickResponse200CategoryType1):
            category = self.category.value
        elif isinstance(self.category, UnsubscribeOneClickResponse200CategoryType2Type1):
            category = self.category.value
        elif isinstance(self.category, UnsubscribeOneClickResponse200CategoryType3Type1):
            category = self.category.value
        else:
            category = self.category


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category": category,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_category(data: object) -> None | UnsubscribeOneClickResponse200CategoryType1 | UnsubscribeOneClickResponse200CategoryType2Type1 | UnsubscribeOneClickResponse200CategoryType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_1 = UnsubscribeOneClickResponse200CategoryType1(data)



                return category_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_2_type_1 = UnsubscribeOneClickResponse200CategoryType2Type1(data)



                return category_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_3_type_1 = UnsubscribeOneClickResponse200CategoryType3Type1(data)



                return category_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnsubscribeOneClickResponse200CategoryType1 | UnsubscribeOneClickResponse200CategoryType2Type1 | UnsubscribeOneClickResponse200CategoryType3Type1, data)

        category = _parse_category(d.pop("category"))


        unsubscribe_one_click_response_200 = cls(
            category=category,
        )


        unsubscribe_one_click_response_200.additional_properties = d
        return unsubscribe_one_click_response_200

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
