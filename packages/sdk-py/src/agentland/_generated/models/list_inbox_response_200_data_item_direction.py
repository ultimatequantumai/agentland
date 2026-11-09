from enum import StrEnum

class ListInboxResponse200DataItemDirection(StrEnum):
    IN = "in"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
