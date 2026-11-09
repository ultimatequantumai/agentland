from enum import StrEnum

class ListTransparencySourcesResponse200DataItemChangesItemStatus(StrEnum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
