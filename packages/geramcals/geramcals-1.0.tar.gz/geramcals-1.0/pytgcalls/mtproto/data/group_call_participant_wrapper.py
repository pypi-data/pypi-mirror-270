from datetime import datetime
from typing import Optional, Union

from pytgcalls.mtproto.data import WrapperBase


class GroupCallParticipantWrapper(WrapperBase):
    """Group Call Participant wrapper for any MTProto client.

    Note:
        `peer` will be `raw.base.Peer` when you are using Pyrogram bridge.

        `peer` will be `TypePeer` when you are using Telethon bridge.

        `date` and `active_date`will be `int` when you are using Pyrogram bridge.

        `date` and `active_date`will be `datetime` when you are using Telethon bridge.

        `video_joined` always will be `None` for Pyrogram until it will update.
    """

    def __init__(
        self,
        peer: Union['raw.base.Peer', 'TypePeer'],
        date: Optional[Union[int, datetime]],
        source: int,
        muted: Optional[bool] = None,
        left: Optional[bool] = None,
        can_self_unmute: Optional[bool] = None,
        just_joined: Optional[bool] = None,
        versioned: Optional[bool] = None,
        min: Optional[bool] = None,
        muted_by_you: Optional[bool] = None,
        volume_by_admin: Optional[bool] = None,
        is_self: Optional[bool] = None,
        video_joined: Optional[bool] = None,
        active_date: Optional[Union[int, datetime]] = None,
        volume: Optional[int] = None,
        about: Optional[str] = None,
        raise_hand_rating: Optional[int] = None,
        **kwargs,  # to bypass new attr from layers
    ):
        self.peer = peer
        '''Peer (as joined) of the group call participant'''
        self.date = date
        self.source = source
        '''User's audio channel synchronization source identifier'''
        self.muted = muted
        '''True, if the participant is muted for all users'''
        self.left = left
        '''True, if the participant left the group call'''
        self.can_self_unmute = can_self_unmute
        '''True, if the participant is muted for all users, but can unmute themselves'''
        self.just_joined = just_joined
        self.versioned = versioned
        self.min = min
        self.muted_by_you = muted_by_you
        '''True, if the current user can mute the participant only for self'''
        self.volume_by_admin = volume_by_admin
        self.is_self = is_self
        '''True, if the participant is the current user'''
        self.video_joined = video_joined
        self.active_date = active_date
        self.volume = volume
        '''Participant's volume level'''
        self.about = about
        '''The participant user's bio or the participant chat's description'''
        self.raise_hand_rating = raise_hand_rating

    @classmethod
    def create(cls, participant):
        if hasattr(participant, '__slots__'):  # pyrogram
            attrs = participant.__slots__
            args_for_init = {}
            for attr in attrs:
                args_for_init[attr] = getattr(participant, attr, None)

            return cls(**args_for_init)
        else:  # telethon
            return cls(**vars(participant))
