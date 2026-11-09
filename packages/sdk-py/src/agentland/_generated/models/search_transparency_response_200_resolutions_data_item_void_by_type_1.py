from enum import StrEnum

class SearchTransparencyResponse200ResolutionsDataItemVoidByType1(StrEnum):
    DISPUTE = "dispute"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
