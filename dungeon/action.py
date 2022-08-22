import sys
import pygame
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from entity import Entity


class Action:
    def __init__(self, *args):
        pass

    def exec(self, entity: 'Entity'):
        raise NotImplementedError()


class EscapeAction(Action):
    def exec(self, entity: 'Entity'):
        pygame.quit()
        sys.exit()


class WaitAction(Action):
    def exec(self, entity: 'Entity'):
        pass


class ActionWithDirection(Action):
    def exec(self, entity: 'Entity'):
        pass

    def __init__(self, direction: Tuple[int, int]):
        super(ActionWithDirection, self).__init__()
        self.direction = direction


class ActionWithTarget(Action):
    def exec(self, entity: 'Entity'):
        pass


class MovementAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        dx, dy = self.direction
        target_x, target_y = entity.x + dx, entity.y + dy
        # 防止跑出地图.
        if target_x < 0 or target_x >= entity.gamemap.width or target_y < 0 or target_y >= entity.gamemap.height:
            return
        # check 目标位置 walkable.
        if entity.gamemap.walkable[target_x, target_y]:
            entity.move(self.direction)
        else:
            return


class ToggleInventor(Action):
    def exec(self, entity: 'Entity'):
        entity.engine.ui.toggle_inventory()
