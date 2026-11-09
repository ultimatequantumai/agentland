from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemTimelineItemResolvedByType1(StrEnum):
    SOURCE = "source"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
