from enum import StrEnum

class RevokeSigningKeyResponse201Status(StrEnum):
    CANCELLED = "cancelled"
    FINALIZED = "finalized"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
