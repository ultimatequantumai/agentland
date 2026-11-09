from enum import StrEnum

class ListChallengesResponse200DataItemStatus(StrEnum):
    CLOSED = "closed"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
