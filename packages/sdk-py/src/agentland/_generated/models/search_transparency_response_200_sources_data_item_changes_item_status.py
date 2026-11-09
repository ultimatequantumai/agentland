from enum import StrEnum

class SearchTransparencyResponse200SourcesDataItemChangesItemStatus(StrEnum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
