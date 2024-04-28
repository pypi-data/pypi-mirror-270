class PytgcallsBaseException(Exception):
    ...


class PytgcallsError(PytgcallsBaseException):
    ...


class CallBeforeStartError(PytgcallsBaseException):
    ...


class NotConnectedError(PytgcallsBaseException):
    ...


class GroupCallNotFoundError(PytgcallsBaseException):
    ...
