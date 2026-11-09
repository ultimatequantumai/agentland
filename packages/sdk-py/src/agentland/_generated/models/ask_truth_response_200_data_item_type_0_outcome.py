from enum import StrEnum

class AskTruthResponse200DataItemType0Outcome(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
