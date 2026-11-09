from enum import StrEnum

class GetNotaryProofResponse200Type1Status(StrEnum):
    INCLUDED = "included"

    def __str__(self) -> str:
        return str(self.value)
