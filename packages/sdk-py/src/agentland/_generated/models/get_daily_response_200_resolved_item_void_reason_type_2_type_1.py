from enum import StrEnum

class GetDailyResponse200ResolvedItemVoidReasonType2Type1(StrEnum):
    DISPUTE = "dispute"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
