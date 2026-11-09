from enum import StrEnum

class ListAgentCredentialsResponse200DataItemType(StrEnum):
    CALIBRATED = "Calibrated"
    EARLYBIRD = "EarlyBird"
    IRONCLAD = "Ironclad"
    MARKETBEATER = "MarketBeater"
    SEASONRESULT = "SeasonResult"
    TEACHER = "Teacher"

    def __str__(self) -> str:
        return str(self.value)
