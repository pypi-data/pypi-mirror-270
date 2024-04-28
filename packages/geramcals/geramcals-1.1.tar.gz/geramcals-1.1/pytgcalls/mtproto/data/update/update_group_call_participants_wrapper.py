from typing import List, TYPE_CHECKING

from pytgcalls.mtproto.data import WrapperBase

if TYPE_CHECKING:
    from pytgcalls.mtproto.data import GroupCallParticipantWrapper


class UpdateGroupCallParticipantsWrapper(WrapperBase):
    def __init__(self, participants: List['GroupCallParticipantWrapper']):
        self.participants = participants
