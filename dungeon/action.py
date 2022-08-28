import sys
from typing import Tuple, TYPE_CHECKING
from dungeon.components.message_manager import MessageManager

import pygame

if TYPE_CHECKING:
    from entity import Entity


class Action:
    def __init__(self, *args):
        self.time = 1
        pass

    def exec(self, entity: 'Entity'):
        pass


class EscapeAction(Action):
    def exec(self, entity: 'Entity'):
        pygame.quit()
        sys.exit()


class WaitAction(Action):
    pass


class ActionWithDirection(Action):
    def exec(self, entity: 'Entity'):
        pass

    def __init__(self, direction: Tuple[int, int]):
        super(ActionWithDirection, self).__init__()
        self.direction = direction

    def target(self, entity: 'Entity'):
        return self.direction[0]+entity.x, self.direction[1]+entity.y


class ActionWithTarget(Action):
    def exec(self, entity: 'Entity'):
        pass


class HeadToAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        dx, dy = self.direction
        target_x, target_y = entity.x + dx, entity.y + dy
        # 防止跑出地图.
        if target_x < 0 or target_x >= entity.gamemap.width or target_y < 0 or target_y >= entity.gamemap.height:
            return
        if entity.gamemap.get_entities_in_xy((target_x, target_y)):
            return AttackAction(self.direction).exec(entity)
        if entity.gamemap.walkable[target_x, target_y]:
            entity.spend(self.time)
            return MovementAction(self.direction).exec(entity)


class MovementAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        entity.move(self.direction)


class AttackAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        MessageManager._instance.log(f"{entity} attacked {entity.gamemap.get_entities_in_xy(self.target(entity))}")
        entity.spend(self.time)


class DebugAction(Action):
    def exec(self, entity: 'Entity'):
        print('message from DebugAction.')


class ToggleInventor(Action):
    def exec(self, entity: 'Entity'):
        entity.engine.ui.toggle_inventory()
