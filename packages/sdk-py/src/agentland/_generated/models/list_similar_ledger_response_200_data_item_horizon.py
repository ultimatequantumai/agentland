from enum import StrEnum

class ListSimilarLedgerResponse200DataItemHorizon(StrEnum):
    DAY = "day"
    HOUR = "hour"
    LONG = "long"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
