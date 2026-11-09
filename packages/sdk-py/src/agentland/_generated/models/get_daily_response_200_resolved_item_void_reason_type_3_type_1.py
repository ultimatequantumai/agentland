from enum import StrEnum

class GetDailyResponse200ResolvedItemVoidReasonType3Type1(StrEnum):
    DISPUTE = "dispute"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
