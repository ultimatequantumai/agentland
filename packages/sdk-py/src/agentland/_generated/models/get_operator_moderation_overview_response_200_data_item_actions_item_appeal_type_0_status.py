from enum import StrEnum

class GetOperatorModerationOverviewResponse200DataItemActionsItemAppealType0Status(StrEnum):
    OVERTURNED = "overturned"
    PENDING = "pending"
    UPHELD = "upheld"

    def __str__(self) -> str:
        return str(self.value)
