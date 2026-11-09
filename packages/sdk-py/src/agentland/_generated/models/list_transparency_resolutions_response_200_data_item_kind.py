from enum import StrEnum

class ListTransparencyResolutionsResponse200DataItemKind(StrEnum):
    RESOLUTION = "resolution"
    VOID = "void"

    def __str__(self) -> str:
        return str(self.value)
