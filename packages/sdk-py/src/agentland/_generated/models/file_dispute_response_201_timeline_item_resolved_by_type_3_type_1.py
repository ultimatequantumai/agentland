from enum import StrEnum

class FileDisputeResponse201TimelineItemResolvedByType3Type1(StrEnum):
    SOURCE = "source"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
