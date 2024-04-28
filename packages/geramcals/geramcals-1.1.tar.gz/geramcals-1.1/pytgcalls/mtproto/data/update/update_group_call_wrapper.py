from typing import TYPE_CHECKING, Union

from pytgcalls.mtproto.data import WrapperBase

if TYPE_CHECKING:
    from pytgcalls.mtproto.data import GroupCallWrapper, GroupCallDiscardedWrapper


class UpdateGroupCallWrapper(WrapperBase):
    def __init__(self, chat_id: int, call: Union['GroupCallWrapper', 'GroupCallDiscardedWrapper']):
        self.chat_id = chat_id
        self.call = call
