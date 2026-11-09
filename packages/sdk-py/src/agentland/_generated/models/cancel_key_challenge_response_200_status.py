from enum import StrEnum

class CancelKeyChallengeResponse200Status(StrEnum):
    CANCELLED = "cancelled"
    FINALIZED = "finalized"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
