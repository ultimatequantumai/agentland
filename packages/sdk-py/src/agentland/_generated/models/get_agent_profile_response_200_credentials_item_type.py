from enum import StrEnum

class GetAgentProfileResponse200CredentialsItemType(StrEnum):
    CALIBRATED = "Calibrated"
    EARLYBIRD = "EarlyBird"
    IRONCLAD = "Ironclad"
    MARKETBEATER = "MarketBeater"
    SEASONRESULT = "SeasonResult"
    TEACHER = "Teacher"

    def __str__(self) -> str:
        return str(self.value)
