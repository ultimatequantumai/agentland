from enum import StrEnum

class GetVaultProofResponse200Type1BundleEntriesItemOp(StrEnum):
    DELETE = "delete"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
