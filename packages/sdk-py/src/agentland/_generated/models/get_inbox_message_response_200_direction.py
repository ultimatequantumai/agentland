from enum import StrEnum

class GetInboxMessageResponse200Direction(StrEnum):
    IN = "in"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
