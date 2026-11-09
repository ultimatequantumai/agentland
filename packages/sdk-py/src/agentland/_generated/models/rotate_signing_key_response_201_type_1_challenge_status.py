from enum import StrEnum

class RotateSigningKeyResponse201Type1ChallengeStatus(StrEnum):
    CANCELLED = "cancelled"
    FINALIZED = "finalized"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
