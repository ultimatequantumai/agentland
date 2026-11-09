from enum import StrEnum

class ListVaultEntriesResponse200DataItemEntryOp(StrEnum):
    DELETE = "delete"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
