from enum import StrEnum

class RotateSigningKeyBodyStatementNewPubKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
