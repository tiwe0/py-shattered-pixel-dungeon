from typing import TYPE_CHECKING, Optional
from dungeon.action import Action, DebugAction, MovementAction, HeadToAction
from utils.path import Path, Position
import random

if TYPE_CHECKING:
    from dungeon.actor import Actor


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


class AIWonder(AI):
    def generate_action(self, actor: 'Actor') -> 'Optional[Action]':
        position_walkable = Path.path_walkable_direction(actor.gamemap, Position(actor.x, actor.y))
        random_target = position_walkable[random.randint(0, len(position_walkable)-1)]
        return HeadToAction(direction=random_target)
