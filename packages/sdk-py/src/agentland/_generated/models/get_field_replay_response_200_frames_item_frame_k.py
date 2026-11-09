from enum import StrEnum

class GetFieldReplayResponse200FramesItemFrameK(StrEnum):
    DELTA = "delta"
    KEY = "key"

    def __str__(self) -> str:
        return str(self.value)
