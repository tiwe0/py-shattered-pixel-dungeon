from typing import Tuple, TYPE_CHECKING
if TYPE_CHECKING:
    from entity import Entity


class Action:
    def __init__(self, *args):
        pass

    def exec(self, entity: 'Entity'):
        raise NotImplementedError()


class Wait(Action):
    def exec(self, entity: 'Entity'):
        pass


class ActionWithDirection(Action):
    def __init__(self, direction: Tuple[int, int]):
        super(ActionWithDirection, self).__init__()
        self.direction = direction


class ActionWithTarget(Action):
    pass


class Movement(ActionWithDirection):
    def exec(self, entity: 'Entity'):
        dx, dy = self.direction
        target_x, target_y = entity.x+dx, entity.y+dy
        if entity.gamemap.walkable[target_x, target_y]:
            entity.move(self.direction)
        else:
            return
