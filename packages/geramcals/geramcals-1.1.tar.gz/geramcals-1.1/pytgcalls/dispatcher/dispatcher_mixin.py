from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from . import GroupCallNative

from .dispatcher import Dispatcher


class DispatcherMixin:
    def __init__(self, actions):
        self._dispatcher = Dispatcher(actions)

    def add_handler(self, callback: Callable, action: str) -> Callable:
        """Register new handler.

        Args:
            callback (`Callable`): Callback function.
            action (`str`): Action.

        Returns:
            `Callable`: original callback.
        """

        return self._dispatcher.add_handler(callback, action)

    def remove_handler(self, callback: Callable, action: str) -> bool:
        """Unregister the handler.

        Args:
            callback (`Callable`): Callback function.
            action (`str`): Action.

        Returns:
            `bool`: Return `True` if success.
        """

        return self._dispatcher.remove_handler(callback, action)

    def trigger_handlers(self, action: str, instance: 'GroupCallNative', *args, **kwargs):
        """Unregister the handler.

        Args:
            action (`str`): Action.
            instance (`GroupCallNative`): Instance of GroupCallBase.
            *args (`list`, optional): Arbitrary callback arguments.
            **kwargs (`dict`, optional): Arbitrary callback arguments.
        """

        self._dispatcher.trigger_handlers(action, instance, *args, **kwargs)
