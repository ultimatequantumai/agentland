from enum import StrEnum

class AppendLineageBodyKind(StrEnum):
    MODEL_CHANGE = "model_change"

    def __str__(self) -> str:
        return str(self.value)
