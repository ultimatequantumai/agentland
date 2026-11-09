from enum import StrEnum

class UnsubscribeOneClickResponse200CategoryType1(StrEnum):
    INACTIVITY_NUDGE = "inactivity_nudge"
    REPORT_CARD = "report_card"
    SEASON_NOTES = "season_notes"
    SEASON_SUMMARY = "season_summary"

    def __str__(self) -> str:
        return str(self.value)
