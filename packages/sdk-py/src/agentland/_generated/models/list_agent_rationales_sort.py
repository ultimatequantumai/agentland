from enum import StrEnum

class ListAgentRationalesSort(StrEnum):
    CITATIONS = "citations"
    EDGE = "edge"
    RECENT = "recent"

    def __str__(self) -> str:
        return str(self.value)
