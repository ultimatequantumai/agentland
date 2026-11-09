from enum import StrEnum

class GetTransparencyDisputeResponse200TimelineItemResolvedByType1(StrEnum):
    SOURCE = "source"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
