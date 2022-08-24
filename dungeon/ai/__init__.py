from typing import TYPE_CHECKING, Optional
from dungeon.actor import Actor
from dungeon.action import Action, DebugAction

if TYPE_CHECKING:
    pass


class AI:
    def __init__(self):
        pass

    def fetch_action(self, actor: 'Actor') -> 'Optional[Action]':
        action = self.generate_action(actor)
        return action

    def generate_action(self, actor: 'Actor') -> 'Optional[Action]':
        raise NotImplementedError()


class AIForDebug(AI):
    def generate_action(self, actor: 'Actor') -> 'Action':
        print('generate action from Debug AI.')
        return DebugAction()
