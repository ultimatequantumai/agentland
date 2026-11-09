from enum import StrEnum

class DeleteMemoryResponse201EntryOp(StrEnum):
    DELETE = "delete"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
