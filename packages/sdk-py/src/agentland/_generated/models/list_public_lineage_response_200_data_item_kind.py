from enum import StrEnum

class ListPublicLineageResponse200DataItemKind(StrEnum):
    CUSTODY_CHANGE = "custody_change"
    KEY_ROTATION = "key_rotation"
    MODEL_CHANGE = "model_change"
    OPERATOR_TRANSFER = "operator_transfer"
    RECOVERY = "recovery"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
