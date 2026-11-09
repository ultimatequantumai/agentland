from enum import StrEnum

class SearchTransparencyResponse200ResolutionsDataItemResolvedByType2Type1(StrEnum):
    SOURCE = "source"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
