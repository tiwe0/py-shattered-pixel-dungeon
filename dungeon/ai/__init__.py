from typing import TYPE_CHECKING, Optional
from dungeon.action import Action, DebugAction, MovementAction, HeadToAction
from dungeon.components.message_manager import MessageManager
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
        actor.update_fov()
        if actor.fov.player_in_fov():
            actor.ai = AIAttack()
            return AIAttack().generate_action(actor)
        else:
            position_walkable = Path.path_walkable_direction(actor.gamemap, Position(actor.x, actor.y))
            random_target = position_walkable[random.randint(0, len(position_walkable)-1)]
            return HeadToAction(direction=random_target)


class AIAttack(AI):
    def generate_action(self, actor: 'Actor') -> 'Optional[Action]':
        actor.update_fov()
        position_walkable = Path.path_walkable(actor.gamemap, Position(actor.x, actor.y))
        if actor.fov.player_in_fov():
            path_to_player = list(Path.path_to(actor.fov, actor.xy, actor.gamemap.player().xy))
            next_position = list(set(position_walkable).intersection(set(path_to_player)))[0]
            direction = (next_position[0]-actor.x, next_position[1]-actor.y)
            return HeadToAction(direction=direction)
        else:
            actor.ai = AIWonder()
            return AIWonder().generate_action(actor)
