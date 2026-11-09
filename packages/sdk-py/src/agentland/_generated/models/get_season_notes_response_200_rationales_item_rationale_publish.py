from enum import StrEnum

class GetSeasonNotesResponse200RationalesItemRationalePublish(StrEnum):
    CLOSE = "close"
    RESOLVE = "resolve"

    def __str__(self) -> str:
        return str(self.value)
