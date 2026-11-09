from enum import StrEnum

class CosignTransferBodyStatementKind(StrEnum):
    OPERATOR_TRANSFER = "operator_transfer"

    def __str__(self) -> str:
        return str(self.value)
