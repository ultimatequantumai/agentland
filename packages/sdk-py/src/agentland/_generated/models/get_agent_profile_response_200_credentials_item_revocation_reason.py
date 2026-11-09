from enum import StrEnum

class GetAgentProfileResponse200CredentialsItemRevocationReason(StrEnum):
    UPHELD_FRAUD = "upheld_fraud"

    def __str__(self) -> str:
        return str(self.value)
