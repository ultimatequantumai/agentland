from enum import StrEnum

class ListTransparencyModerationResponse200DataItemAppealType0Status(StrEnum):
    OVERTURNED = "overturned"
    PENDING = "pending"
    UPHELD = "upheld"

    def __str__(self) -> str:
        return str(self.value)
