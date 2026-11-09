from enum import StrEnum

class UnsubscribeOneClickFilesBodyListUnsubscribe(StrEnum):
    ONE_CLICK = "One-Click"

    def __str__(self) -> str:
        return str(self.value)
