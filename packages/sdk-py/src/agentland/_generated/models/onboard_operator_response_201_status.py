from enum import StrEnum

class OnboardOperatorResponse201Status(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
