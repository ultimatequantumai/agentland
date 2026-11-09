from enum import StrEnum

class GetOperatorModerationOverviewResponse200DataItemActionsItemOffense(StrEnum):
    IDENTITY_FRAUD = "identity_fraud"
    ORDINARY = "ordinary"

    def __str__(self) -> str:
        return str(self.value)
