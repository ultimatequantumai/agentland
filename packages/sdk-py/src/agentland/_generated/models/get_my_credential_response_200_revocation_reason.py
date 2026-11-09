from enum import StrEnum

class GetMyCredentialResponse200RevocationReason(StrEnum):
    UPHELD_FRAUD = "upheld_fraud"

    def __str__(self) -> str:
        return str(self.value)
