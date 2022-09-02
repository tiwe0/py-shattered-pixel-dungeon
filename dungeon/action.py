import sys
from typing import TYPE_CHECKING

import pygame

from dungeon.tweener.tweener import BounceTweener
from dungeon.components.message_manager import MessageManager
from utils.typing import Position

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
    def exec(self, entity: 'Entity'):
        entity.spend(1)


class ActionWithDirection(Action):
    def exec(self, entity: 'Entity'):
        pass

    def __init__(self, direction: 'Position'):
        super(ActionWithDirection, self).__init__()
        if not isinstance(direction, Position):
            direction = Position(x=direction[0], y=direction[1])
        self.direction: 'Position' = direction

    def target(self, entity: 'Entity') -> 'Position':
        return self.direction + entity.xy


class ActionWithTarget(Action):
    def exec(self, entity: 'Entity'):
        pass


class HeadToAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        # 防止跑出地图.
        if self.target(entity=entity) not in entity.gamemap:
            return
        if entity.gamemap.get_entities_in_xy(self.target(entity=entity)):
            return AttackAction(self.direction).exec(entity)
        if entity.gamemap.walkable[self.target(entity=entity)]:
            entity.spend(entity.gamemap.weight[self.target(entity=entity)])
            return MovementAction(self.direction).exec(entity)


class MovementAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        entity.move(self.direction)


class AttackAction(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        MessageManager.instance.log(f"{entity} attacked {entity.gamemap.get_entities_in_xy(self.target(entity))}")
        entity.spend(self.time)
        target = entity.sprite.xy + 8 * self.direction
        # TODO
        if entity.is_player():
            entity.followed.follow_sprite = False
        entity.sprite.pos_tweeners.append(BounceTweener(entity.sprite, target, 200))
        if entity.is_player():
            entity.followed.follow_sprite = True


class DebugAction(Action):
    def exec(self, entity: 'Entity'):
        print('message from DebugAction.')


class ToggleInventor(Action):
    def exec(self, entity: 'Entity'):
        entity.engine.ui.toggle_inventory()


class UpStairAction(Action):
    pass


class DownStairAction(Action):
    pass


class DrinkAction(Action):
    pass


class EatAction(Action):
    pass


class PickUpAction(Action):
    pass


class OpenAction(Action):
    pass


class CloseAction(Action):
    pass


class KickAction(Action):
    pass
