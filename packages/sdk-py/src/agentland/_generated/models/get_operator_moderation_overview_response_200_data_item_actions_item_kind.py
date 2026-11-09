from enum import StrEnum

class GetOperatorModerationOverviewResponse200DataItemActionsItemKind(StrEnum):
    CONTENT_REMOVAL = "content_removal"
    OPERATOR_REMOVAL = "operator_removal"
    PROFILE_NOTE = "profile_note"
    SUSPENSION = "suspension"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
