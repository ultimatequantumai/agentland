from enum import StrEnum

class CreateAgentResponse201ApiKeyPrefix(StrEnum):
    AL_AG = "al_ag_"
    AL_OP = "al_op_"

    def __str__(self) -> str:
        return str(self.value)
