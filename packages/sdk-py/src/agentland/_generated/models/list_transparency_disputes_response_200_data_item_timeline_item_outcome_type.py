from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemTimelineItemOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
