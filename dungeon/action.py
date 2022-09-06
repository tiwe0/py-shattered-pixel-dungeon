import sys
from typing import TYPE_CHECKING, Union

import pygame

from dungeon.tweener.tweener import BounceTweener
from utils.typing import Position

if TYPE_CHECKING:
    from dungeon.entity import Entity
    from dungeon.actors.actor import Actor
    from dungeon.input_handler import InventoryEventHandler


class Action:
    def __init__(self, *args, **kwargs):
        self.time = 1
        pass

    def exec(self, entity: 'Entity'):
        pass


class InventoryAction:
    def __init__(self, *args, **kwargs):
        self.time = 0
        pass

    def exec(self, entity: 'Entity'):
        pass


class SystemActionEscape(Action):
    def exec(self, entity: 'Entity'):
        pygame.quit()
        sys.exit()


class ActorActionWait(Action):
    def exec(self, entity: 'Entity'):
        entity.spend(1)


class ActorActionWithDirection(Action):
    def exec(self, entity: 'Entity'):
        pass

    def __init__(self, direction: 'Position'):
        super(ActorActionWithDirection, self).__init__()
        if not isinstance(direction, Position):
            direction = Position(x=direction[0], y=direction[1])
        self.direction: 'Position' = direction

    def target(self, entity: 'Entity') -> 'Position':
        return self.direction + entity.xy


class ActorActionWithTarget(Action):
    def exec(self, entity: 'Entity'):
        pass


class ActorActionHeadTo(ActorActionWithDirection):
    def exec(self, entity: 'Entity'):
        # 防止跑出地图.
        if self.target(entity=entity) not in entity.gamemap:
            return
        if entity.gamemap.get_entities_in_xy(self.target(entity=entity)):
            return ActorActionAttack(self.direction).exec(entity)
        if entity.gamemap.walkable[self.target(entity=entity)]:
            entity.spend(entity.gamemap.weight[self.target(entity=entity)])
            return ActorActionMovement(self.direction).exec(entity)


class ActorActionMovement(ActorActionWithDirection):
    def exec(self, entity: 'Entity'):
        entity.move(self.direction)


class ActorActionAttack(ActorActionWithDirection):
    def exec(self, entity: 'Union[Entity, Actor]'):
        enemy: 'Actor' = entity.gamemap.get_entities_in_xy(self.target(entity))
        entity.spend(self.time)
        target = entity.sprite.pos + 4 * self.direction
        # TODO 后续再优化一下with
        if entity.is_player():
            with entity.followed.suspend_follow():
                entity.sprite.pos_tweeners.append(BounceTweener(entity.sprite, target, 200))
        else:
            entity.sprite.pos_tweeners.append(BounceTweener(entity.sprite, target, 200))
        attack = entity.attack_dice.roll()
        defence = enemy.defence_dice.roll()
        damage = max(0, attack-defence)
        enemy.hp -= damage


class DebugAction(Action):
    def exec(self, entity: 'Entity'):
        print('message from DebugAction.')


class TimeManagerActionSuspend(Action):
    pass


class ActorActionUpStair(Action):
    pass


class ActorActionDownStair(Action):
    pass


class ActorActionDrink(Action):
    pass


class ActorActionEat(Action):
    pass


class ActorActionPickUp(Action):
    pass


class ActorActionOpen(Action):
    pass


class ActorActionClose(Action):
    pass


class ActorActionKick(Action):
    pass


class InventoryActionToggle(InventoryAction):
    def exec(self, entity: 'Union[Actor, InventoryEventHandler]'):
        entity.engine.ui.toggle_inventory()


class InventoryActionShiftPage(InventoryAction):
    pass


class InventoryActionShiftItem(InventoryAction):
    pass


class InventoryActionShiftCate(InventoryAction):
    pass


class InventoryActionSelect(InventoryAction):
    pass
