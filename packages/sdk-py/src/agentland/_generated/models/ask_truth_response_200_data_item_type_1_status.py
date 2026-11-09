from enum import StrEnum

class AskTruthResponse200DataItemType1Status(StrEnum):
    UNRESOLVED = "unresolved"

    def __str__(self) -> str:
        return str(self.value)
