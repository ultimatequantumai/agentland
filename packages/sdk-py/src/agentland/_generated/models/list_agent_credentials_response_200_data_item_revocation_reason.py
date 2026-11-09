from enum import StrEnum

class ListAgentCredentialsResponse200DataItemRevocationReason(StrEnum):
    UPHELD_FRAUD = "upheld_fraud"

    def __str__(self) -> str:
        return str(self.value)
