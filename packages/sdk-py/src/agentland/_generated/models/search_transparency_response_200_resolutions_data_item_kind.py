from enum import StrEnum

class SearchTransparencyResponse200ResolutionsDataItemKind(StrEnum):
    RESOLUTION = "resolution"
    VOID = "void"

    def __str__(self) -> str:
        return str(self.value)
