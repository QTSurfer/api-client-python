from enum import Enum


class LiveAttachmentAcceptedState(str, Enum):
    ATTACHED = "ATTACHED"
    ATTACHING = "ATTACHING"
    DETACHED = "DETACHED"
    DETACHING = "DETACHING"
    REFUSED = "REFUSED"

    def __str__(self) -> str:
        return str(self.value)
