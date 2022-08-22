import random
from typing import Tuple, Iterator, List, TYPE_CHECKING, Set, Optional

import numpy as np
import pygame

from dungeon.assets import Assets
from dungeon.dsprite import DSpriteSheetReader
from dungeon.tileset.fog_of_war import FogOfWar
from utils.line import line
from utils.compute_fov import compute_fov

if TYPE_CHECKING:
    from entity import Entity
    from dungeon.engine import Engine

# for test
tmp_test_tiles = DSpriteSheetReader(Assets.Environment.tiles_sewers, frame_width=16, frame_height=16, row=4)
wall_tile = tmp_test_tiles[48]
floor_tile = tmp_test_tiles[0]


class GameMap:
    """游戏中地图的抽象模型."""
    max_room = 30
    min_room_width = 5
    min_room_height = 5
    max_room_width = 9
    max_room_height = 9

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height

        # 地图信息.
        self.tiles = np.full((width, height), fill_value=1, order='F')
        self.walkable = np.full((width, height), fill_value=False, order='F')
        self.explored = np.full((width, height), fill_value=False, order='F')
        self.visiting = np.full((width, height), fill_value=False, order='F')

        # 负责优化渲染. 后续的 16 要抽象出来.
        self.surface: 'pygame.Surface' = pygame.Surface((width*16, height*16))

        # 其他信息
        self.entities: 'Set[Entity]' = set()
        self.rooms: 'List[RectangularRoom]' = []
        self.engine: 'Optional[Engine]' = None

    def player(self):
        return self.engine.player

    def update_map(self):
        self.visiting[:] = compute_fov(origin=(self.player().x, self.player().y), gamemap=self, radius=7)
        self.explored |= self.visiting
        self.update_surface()

    def update_surface(self):
        """负责更新应当渲染的 surface, 通常不需要每帧都渲染, 而是特定动作后渲染一次即可."""
        self.surface.fill((0, 0, 0))
        for c in range(self.width):
            for r in range(self.height):
                # 只渲染已访问地图
                if self.explored[c, r]:
                    # 根据 tiles 渲染.
                    if self.tiles[c, r] == 1:
                        self.surface.blit(wall_tile, (c*16, r*16))
                    else:
                        self.surface.blit(floor_tile, (c*16, r*16))
                    # 若该块没有正在视野中, 再加一层记忆遮罩.
                    if not self.visiting[c, r]:
                        self.surface.blit(FogOfWar.explored_surface, (c*16, r*16))

    def render_map(self):
        """渲染自己."""
        screen = pygame.display.get_surface()
        screen.blit(self.surface, (0, 0))

    def get_entities_in_xy(self, xy: Tuple[int, int]):
        """检索目标位置的第一个 entity."""
        for entity in self.entities:
            if entity.xy == xy:
                return entity
        return None

    def render(self):
        """先渲染地图, 再渲染实体."""
        self.render_map()
        for entity in self.entities:
            entity.render()

    def place_entity(self, *, entity: 'Entity', position: 'Tuple[int, int]'):
        """将实体放入地图的某个位置."""
        # 先注册.
        entity.gamemap = self
        self.entities.add(entity)
        # 再放置.
        entity.x, entity.y = position
        # 最后更新 sprite 位置.
        entity.update_sprite_pos()


class RectangularRoom:
    """游戏内房间的抽象模型."""
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1, self.y1 = x, y
        self.width, self.height = width, height
        self.x2, self.y2 = x+width, y+height

    @property
    def center_xy(self) -> Tuple[int, int]:
        """房间中心."""
        return self.x1+self.width//2, self.y1+self.height//2

    @property
    def inner(self) -> Tuple[slice, slice]:
        """房间内部."""
        return slice(self.x1+1, self.x2), slice(self.y1+1, self.y2)

    def intersects(self, other_room: 'RectangularRoom') -> bool:
        """判断房间是否重叠."""
        return (
            self.x1 <= other_room.x2
            and self.x2 >= other_room.x1
            and self.y1 <= other_room.y2
            and self.y2 >= other_room.y1
        )


def tunnel_between(
        start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    yield from line(start, end)


def gen_gamemap(map_width: int, map_height: int):
    """基础地图生成算法."""
    gamemap = GameMap(map_width, map_height)
    rooms_list: 'List[RectangularRoom]' = []

    for i in range(gamemap.max_room):
        room_width = random.randint(gamemap.min_room_width, gamemap.max_room_width)
        room_height = random.randint(gamemap.min_room_height, gamemap.max_room_height)
        room_x = random.randint(1, gamemap.width-room_width-1)
        room_y = random.randint(1, gamemap.height-room_height-1)
        new_room = RectangularRoom(room_x, room_y, room_width, room_height)

        if any(new_room.intersects(r) for r in rooms_list):
            continue

        gamemap.tiles[new_room.inner] = 0
        gamemap.walkable[new_room.inner] = True

        if len(rooms_list) != 0:
            for x, y in tunnel_between(new_room.center_xy, rooms_list[-1].center_xy):
                gamemap.tiles[x, y] = 0
                gamemap.walkable[x, y] = True

        rooms_list.append(new_room)

    gamemap.rooms = rooms_list
    gamemap.update_surface()

    return gamemap
