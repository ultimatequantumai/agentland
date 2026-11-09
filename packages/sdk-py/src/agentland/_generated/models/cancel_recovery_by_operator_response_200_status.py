from enum import StrEnum

class CancelRecoveryByOperatorResponse200Status(StrEnum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
