from enum import StrEnum

class GetVaultProofResponse200Type0EntryOp(StrEnum):
    DELETE = "delete"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
