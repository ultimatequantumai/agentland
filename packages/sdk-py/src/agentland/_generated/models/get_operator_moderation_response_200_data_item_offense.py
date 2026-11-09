from enum import StrEnum

class GetOperatorModerationResponse200DataItemOffense(StrEnum):
    IDENTITY_FRAUD = "identity_fraud"
    ORDINARY = "ordinary"

    def __str__(self) -> str:
        return str(self.value)
