from enum import StrEnum

class GetChallengeResponse200Status(StrEnum):
    CLOSED = "closed"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
