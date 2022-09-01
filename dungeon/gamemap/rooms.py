import random
from typing import Optional, Tuple, TYPE_CHECKING
from utils.typing import Position

if TYPE_CHECKING:
    from dungeon.gamemap import GameMap


class RectangularRoom:
    """游戏内房间的抽象模型."""

    def __init__(self, x: int, y: int, width: int, height: int, *, gamemap: 'Optional[GameMap]' = None):
        self._gamemap = gamemap
        self.x1, self.y1 = x, y
        self.width, self.height = width, height
        self.x2, self.y2 = x + width, y + height

    @property
    def gamemap(self):
        return self._gamemap

    @gamemap.setter
    def gamemap(self, value: 'Optional[GameMap]'):
        if value:
            value.add_room(self)
        else:
            if self.gamemap:
                if self in self.gamemap.rooms:
                    self.gamemap.rooms.remove(self)
        self._gamemap = value

    @property
    def tiles(self):
        if self.gamemap:
            return self.gamemap.tiles

    @property
    def walkable(self):
        if self.gamemap:
            return self.gamemap.walkable

    @property
    def random(self):
        if self.gamemap:
            return self.gamemap.random

    @property
    def weight(self):
        if self.gamemap:
            return self.gamemap.weight

    @property
    def explored(self):
        if self.gamemap:
            return self.gamemap.explored

    @property
    def visiting(self):
        if self.visiting:
            return self.gamemap.visiting

    @property
    def center_xy(self) -> 'Position':
        """房间中心."""
        return Position(x=self.x1 + self.width // 2, y=self.y1 + self.height // 2)

    @property
    def random_pos(self) -> 'Position':
        random_x = random.randint(self.x1+1, self.x2-1)
        random_y = random.randint(self.y1+1, self.y2-1)
        return Position(x=random_x, y=random_y)

    @property
    def inner(self) -> Tuple[slice, slice]:
        """房间内部."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    @property
    def corner(self) -> Tuple[slice, slice]:
        return slice(self.x1, self.x2+1, self.width), slice(self.y1, self.y2+1, self.height)

    def intersects(self, other_room: 'RectangularRoom') -> bool:
        """判断房间是否重叠."""
        return (
                self.x1 <= other_room.x2
                and self.x2 >= other_room.x1
                and self.y1 <= other_room.y2
                and self.y2 >= other_room.y1
        )
