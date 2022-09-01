from typing import TYPE_CHECKING, Optional
from dungeon.action import Action, DebugAction, MovementAction, HeadToAction
from dungeon.components.message_manager import MessageManager
from test.debug import DebugRender
from utils.path import PathFinder
from utils.typing import Position
import random

if TYPE_CHECKING:
    from dungeon.actor import Actor


class AI:
    def __init__(self):
        pass

    def fetch_action(self, actor: 'Actor') -> 'Optional[Action]':
        actor.update_fov()
        PathFinder.gamemap = actor.gamemap
        action = self.generate_action(actor)
        return action

    def generate_action(self, actor: 'Actor') -> 'Optional[Action]':
        raise NotImplementedError()


class AIForDebug(AI):
    def generate_action(self, actor: 'Actor') -> 'Action':
        print('generate action from Debug AI.')
        return DebugAction()

# TODO 后面怪物AI可以重构成一个有限状态机.


class AIWonder(AI):
    def generate_action(self, actor: 'Actor') -> 'Optional[Action]':
        if actor.fov.player_in_fov():
            actor.ai = AIAttack()
            return AIAttack().generate_action(actor)
        else:
            if actor.path_to_walk:
                direction = actor.path_to_walk.pop(0) - actor.xy
                return HeadToAction(direction=direction)
            else:
                position_walkable = PathFinder.path_walkable_direction(Position(actor.x, actor.y))
                random_target = position_walkable[random.randint(0, len(position_walkable)-1)]
                return HeadToAction(direction=random_target)


class AIAttack(AI):
    def generate_action(self, actor: 'Actor') -> 'Optional[Action]':
        gamemap = actor.gamemap
        if actor.fov.player_in_fov():
            path_to_player = [p for p in PathFinder.path_to(actor.xy, gamemap.player().xy)]

            next_position = path_to_player.pop(0)
            direction = next_position - actor.xy

            actor.path_to_walk = path_to_player

            return HeadToAction(direction=direction)
        else:
            actor.ai = AIWonder()
            return AIWonder().generate_action(actor)
