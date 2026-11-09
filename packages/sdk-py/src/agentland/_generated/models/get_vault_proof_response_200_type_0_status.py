from enum import StrEnum

class GetVaultProofResponse200Type0Status(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
