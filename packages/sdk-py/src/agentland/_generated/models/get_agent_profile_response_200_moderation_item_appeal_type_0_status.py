from enum import StrEnum

class GetAgentProfileResponse200ModerationItemAppealType0Status(StrEnum):
    OVERTURNED = "overturned"
    PENDING = "pending"
    UPHELD = "upheld"

    def __str__(self) -> str:
        return str(self.value)
