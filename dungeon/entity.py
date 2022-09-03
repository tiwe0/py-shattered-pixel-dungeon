from typing import Tuple, TYPE_CHECKING, Optional

from dungeon.config import GRID_SIZE
from utils.path import Position

if TYPE_CHECKING:
    from dungeon.gamemap.__init__ import GameMap
    from dungeon.dsprite import DSprite
    from dungeon.engine import Engine
    from dungeon.view_port import ViewPort


class Entity:
    """游戏中实体的抽象模型."""

    def __init__(self, x: int = 0, y: int = 0, sprite: 'Optional[DSprite]' = None):
        """

        :param x: x 坐标, 这里为地图坐标, 而非渲染坐标.
        :param y: y 坐标, 这里为地图坐标, 而非渲染坐标.
        :param sprite: 对应的 DSprite 实例, 通常情况 每个实例应对应唯一的 DSprite.
        """
        self.x, self.y = x, y

        self.status = "idle"  # 默认状态. (废弃)

        # sprite 应当知晓 entity
        self.sprite = sprite
        sprite.entity = self

        # entity 应当知晓 gamemap, engine
        self.gamemap: 'Optional[GameMap]' = None
        self.engine: 'Optional[Engine]' = None

        # 用于游戏内回合数判断.
        self.game_time = 0
        self.time_manager = None
        self.last_spend = 0

        self.followed: 'ViewPort' = None

    def spend(self, time):
        self.game_time += time
        self.last_spend = time

    def __lt__(self, other: 'Entity'):
        return self.game_time < other.game_time

    def __eq__(self, other: 'Entity'):
        return self.game_time == other.game_time

    def action_override(self, action_name: str):
        return f'exec_{action_name.lower()}' in self.__dir__()

    @property
    def xy(self):
        return Position(x=self.x, y=self.y)

    @property
    def pos(self):
        """返回对应的渲染位置."""
        return GRID_SIZE * self.x, GRID_SIZE * self.y

    def update_sprite_pos(self):
        self.sprite.x, self.sprite.y = GRID_SIZE * self.x, GRID_SIZE * self.y

    def render(self):
        """render 委托给 sprite."""
        self.sprite.render()

    def is_player(self):
        """判断自己是否为玩家控制的entity."""
        return self is self.gamemap.player()

    def move(self, direction: 'Tuple[int, int]'):
        """移动函数, 这里不作任何判断, 位置是否合法, 判断应当由事件处理器或AI自行判断."""
        dx, dy = direction
        self.x += dx
        self.y += dy

        # 如果为玩家, 则更新地图信息.
        if self.is_player():
            self.gamemap.update_map()

        # sprite 移动
        self.sprite.move(direction)
