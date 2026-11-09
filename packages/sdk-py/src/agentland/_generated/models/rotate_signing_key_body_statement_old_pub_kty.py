from enum import StrEnum

class RotateSigningKeyBodyStatementOldPubKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
