import asyncio
import logging
from typing import Callable, List

from typing import TYPE_CHECKING

from ..exceptions import PytgcallsError

if TYPE_CHECKING:
    from . import GroupCallNative

logger = logging.getLogger(__name__)


class Dispatcher:
    def __init__(self, available_actions: type):
        self.actions = available_actions
        self.__action_to_handlers = self.__build_handler_storage()

    def __build_handler_storage(self):
        logger.debug('Build storage of handlers for dispatcher.')
        return {action: [] for action in dir(self.actions) if not action.startswith('_')}

    def add_handler(self, callback: Callable, action: str) -> Callable:
        logger.debug(f'Add handler to {action} action...')
        if not asyncio.iscoroutinefunction(callback):
            raise PytgcallsError('Sync callback does not supported')

        try:
            handlers = self.__action_to_handlers[action]
            if callback in handlers:
                logger.debug('Handler is already set.')
                return callback

            handlers.append(callback)
        except KeyError:
            raise PytgcallsError('Invalid action')

        logger.debug('Handler added.')
        return callback

    def remove_handler(self, callback: Callable, action: str) -> bool:
        logger.debug(f'Remove handler of {action} action...')
        try:
            handlers = self.__action_to_handlers[action]
            for i in range(len(handlers)):
                if handlers[i] == callback:
                    del handlers[i]
                    return True
        except KeyError:
            raise PytgcallsError('Invalid action')

        return False

    def remove_all(self):
        self.__action_to_handlers = self.__build_handler_storage()

    def get_handlers(self, action: str) -> List[Callable]:
        try:
            logger.debug(f'Get {action} handlers...')
            return self.__action_to_handlers[action]
        except KeyError:
            raise PytgcallsError('Invalid action')

    def trigger_handlers(self, action: str, instance: 'GroupCallNative', *args, **kwargs):
        logger.debug(f'Trigger {action} handlers...')

        for handler in self.get_handlers(action):
            logger.debug(f'Trigger {handler.__name__}...')
            instance.get_event_loop().create_task(handler(instance, *args, **kwargs))
