from pytgcalls.mtproto.data import WrapperBase


class GroupCallWrapper(WrapperBase):
    def __init__(self, call_id: int, params):
        self.id = call_id
        self.params = params  # its a DataJSON object with params.data attr
