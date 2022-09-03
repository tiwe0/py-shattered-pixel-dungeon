import random
from typing import Tuple, Iterator, List, TYPE_CHECKING, Optional

import numpy as np
import pygame

from dungeon.assets import Assets
from dungeon.config import GRID_SIZE
from dungeon.dsprite import DSpriteSheetReader
from dungeon.gamemap.gamemap_render import GameMapRender
from dungeon.gamemap.rooms import RectangularRoom
from dungeon.tileset.terrain import Terrain
from dungeon.tileset.tiles_map import Tiles
from utils.compute_fov import FOV
from utils.line import line
from utils.typing import Position
from utils.typing import map_tile_type

if TYPE_CHECKING:
    from dungeon.item import Item
    from dungeon.entity import Entity
    from dungeon.engine import Engine
    from dungeon.actor import Actor

# for test
tmp_test_tiles = DSpriteSheetReader(Assets.Environment.tiles_sewers, frame_width=GRID_SIZE, frame_height=GRID_SIZE,
                                    row=4)
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
        self.info = np.full(
            (width, height),
            fill_value=np.array((Terrain.WALL, np.inf, 0, False, False, False), dtype=map_tile_type),
            order='F'
        )

        self.tiles = self.info['tiles']
        self.weight = self.info['weight']
        self.random = self.info['random']
        self.walkable = self.info['walkable']
        self.explored = self.info['explored']
        self.visiting = self.info['visiting']

        self.surface_middle: 'pygame.Surface' = pygame.Surface((width * GRID_SIZE, height * GRID_SIZE)).convert_alpha()
        self.surface_down: 'pygame.Surface' = pygame.Surface((width * GRID_SIZE, height * GRID_SIZE)).convert_alpha()
        self.surface_up: 'pygame.Surface' = pygame.Surface((width * GRID_SIZE, height * GRID_SIZE)).convert_alpha()

        # 其他信息
        self.entities: 'List[Entity]' = []
        self.items: 'List[Item]' = []
        self.rooms: 'List[RectangularRoom]' = []
        self.engine: 'Optional[Engine]' = None
        self.gamemap_render: 'Optional[GameMapRender]' = None
        self.tileset_test = Tiles()
        self.fov = None

    def get_tile(self, pos: 'Position'):
        if pos in self:
            return self.tiles[pos]
        else:
            return Terrain.WALL

    def add_room(self, room: 'RectangularRoom'):
        self.rooms.append(room)

    def __getitem__(self, item: 'Position'):
        if item in self:
            return self.info[item]
        else:
            return None

    def __contains__(self, item: 'Position'):
        x, y = item
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    def player(self) -> 'Actor':
        return self.engine.player

    def update_map(self):
        if self.fov is None:
            self.fov = FOV(self)
        self.fov.compute_fov(self.player().xy, self.player().radius)
        self.visiting = self.fov.fov
        self.explored |= self.visiting
        self.update_surface()

    def update_surface(self):
        if self.gamemap_render is None:
            self.gamemap_render = GameMapRender(self)
        self.gamemap_render.update_surface()

    def render_map(self):
        self.gamemap_render.render()

    def get_item_in_xy(self, xy: 'Position'):
        for item in self.items:
            if item.xy == xy:
                return item
        return None

    def get_entities_in_xy(self, xy: 'Position'):
        """检索目标位置的第一个 entity."""
        for entity in self.entities:
            if entity.xy == xy:
                return entity
        return None

    def render_entity(self):
        for entity in self.entities:
            entity.render()

    def render(self):
        """分层渲染, 不需要考虑地图与实体顺序"""
        self.render_map()
        self.render_entity()

    def place_entity(self, *, entity: 'Entity', position: 'Position'):
        """将实体放入地图的某个位置."""
        # 先注册.
        entity.gamemap = self
        self.entities.append(entity)
        # 再放置.
        entity.x, entity.y = position
        entity.fov = FOV(self)
        # 最后更新 sprite 位置.
        entity.update_sprite_pos()


def tunnel_between(
        start: 'Position', end: 'Position'
) -> Iterator[Tuple[int, int]]:
    yield from line(start, end)


def gen_gamemap(map_width: int, map_height: int):
    """基础地图生成算法."""
    # TODO Bad Code
    gamemap = GameMap(map_width, map_height)

    for i in range(gamemap.max_room):
        room_width = random.randint(gamemap.min_room_width, gamemap.max_room_width)
        room_height = random.randint(gamemap.min_room_height, gamemap.max_room_height)
        room_x = random.randint(1, gamemap.width - room_width - 1)
        room_y = random.randint(1, gamemap.height - room_height - 1)
        new_room = RectangularRoom(room_x, room_y, room_width, room_height, gamemap=gamemap)

        if any(new_room.intersects(r) for r in gamemap.rooms):
            new_room.gamemap = None
            continue

        new_room.tiles[new_room.inner] = Terrain.EMPTY
        new_room.walkable[new_room.inner] = True
        new_room.weight[new_room.inner] = 1

        new_room.tiles[new_room.corner] = Terrain.WALL
        new_room.walkable[new_room.corner] = False

        if len(gamemap.rooms) != 0:
            for x, y in tunnel_between(new_room.center_xy, gamemap.rooms[-1].center_xy):
                new_room.tiles[x, y] = Terrain.EMPTY
                new_room.walkable[x, y] = True
                new_room.weight[x, y] = 1

        gamemap.add_room(new_room)

    gamemap.rooms[-1].tiles[gamemap.rooms[-1].center_xy] = Terrain.ENTRANCE
    gamemap.rooms[0].tiles[gamemap.rooms[0].center_xy] = Terrain.EXIT

    gamemap.update_surface()

    return gamemap
