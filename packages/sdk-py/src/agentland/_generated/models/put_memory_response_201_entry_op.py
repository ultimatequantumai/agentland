from enum import StrEnum

class PutMemoryResponse201EntryOp(StrEnum):
    DELETE = "delete"
    PUT = "put"

    def __str__(self) -> str:
        return str(self.value)
