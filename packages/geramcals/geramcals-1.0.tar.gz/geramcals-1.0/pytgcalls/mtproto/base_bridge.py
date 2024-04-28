from abc import ABC
from asyncio import AbstractEventLoop
from typing import Callable


class MTProtoBridgeBase(ABC):
    def __init__(self, client):
        self.client = client
        '''Any MTProto client. Pyrogram/Telethon and so on'''

        self.group_call_participants_update_callback = None
        '''Native handler of wrapped group call participants update'''
        self.group_call_update_callback = None
        '''Native handler of wrapped group call update'''

        self.full_chat = None
        '''Full chat information'''
        self.chat_peer = None
        '''Chat peer where bot is now'''

        self.group_call = None
        '''Instance of MTProto's group call'''

        self.my_ssrc = None
        '''Client SSRC (Synchronization Source)'''
        self.my_peer = None
        '''Client user peer'''

        self.join_as = None
        '''How to present yourself in participants list'''

    def reset(self):
        self.group_call = self.full_chat = self.chat_peer = self.join_as = self.my_peer = self.my_ssrc = None

    def register_group_call_native_callback(
        self, group_call_participants_update_callback: Callable, group_call_update_callback: Callable
    ):
        self.group_call_participants_update_callback = group_call_participants_update_callback
        self.group_call_update_callback = group_call_update_callback

    def re_register_update_handlers(self):
        """Delete and add pytgcalls handler in MTProto client."""
        self.unregister_update_handlers()
        self.register_update_handlers()

    async def check_group_call(self) -> bool:
        """Check if client is in a voice chat.

        Returns:
            `bool`: Is in voice chat by opinion of Telegram server.

        raise wrapped BadRequest if you got [400 GROUPCALL_JOIN_MISSING] response!
        """

        raise NotImplementedError

    async def leave_current_group_call(self):
        """
        call phone.LeaveGroupCall and handle returned updates
        """
        raise NotImplementedError

    async def edit_group_call_member(self, peer, volume: int = None, muted=False):
        """
        call phone.EditGroupCallParticipant
        """
        raise NotImplementedError

    async def get_and_set_self_peer(self):
        """
        resolve self peer and set to obj field
        """
        raise NotImplementedError

    async def get_and_set_group_call(self, group):
        """
        there is group arg can be peer, int, string with username and so on
        need to support all of them

        in this method be set chat_peer, full_chat and group_call class fields

        I think group_call don't need to wrap cuz it will be used in phone.JoinGroupCall
        """
        raise NotImplementedError

    def unregister_update_handlers(self):
        """
        delete all registered handlers from MTProto client
        """
        raise NotImplementedError

    def register_update_handlers(self):
        """
        register handlers
        """
        raise NotImplementedError

    async def resolve_and_set_join_as(self, join_as):
        """
        join_as arg can be str on peer. if it str we need to resolve peer
        save join_as to class field
        """
        raise NotImplementedError

    async def send_speaking_group_call_action(self):
        """
        call messages.SetTyping with SpeakingInGroupCallAction by chat_peer
        """
        raise NotImplementedError

    async def join_group_call(
        self, invite_hash: str, params: dict, muted: bool, video_stopped: bool, pre_update_processing: Callable
    ):
        """
        call phone.JoinGroupCall with group_call, join_as, invite hash, muted and params

        handle updates from response!

        reraise wrapped GroupcallSsrcDuplicateMuch!
        """
        raise NotImplementedError

    def set_my_ssrc(self, ssrc):
        self.my_ssrc = ssrc

    def handle_updates(self, updates):
        raise NotImplementedError
