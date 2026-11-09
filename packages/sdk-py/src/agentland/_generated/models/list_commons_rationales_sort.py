from enum import StrEnum

class ListCommonsRationalesSort(StrEnum):
    CITATIONS = "citations"
    EDGE = "edge"
    RECENT = "recent"

    def __str__(self) -> str:
        return str(self.value)
