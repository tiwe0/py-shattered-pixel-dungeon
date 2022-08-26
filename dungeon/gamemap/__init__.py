import random
from typing import Tuple, Iterator, List, TYPE_CHECKING, Optional

import numpy as np
import pygame

from dungeon import pre_screen_middle, pre_screen_down, pre_screen_up
from dungeon.assets import Assets
from dungeon.config import GRID_SIZE
from dungeon.dsprite import DSpriteSheetReader
from dungeon.gamemap.rooms import RectangularRoom
from dungeon.tileset.fog_of_war import FogOfWar
from dungeon.tileset.terrain import Terrain
from dungeon.tileset.tiles_map import Tiles
from utils.compute_fov import compute_fov
from utils.line import line

if TYPE_CHECKING:
    from pygame import Surface
    from dungeon.entity import Entity
    from dungeon.engine import Engine

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
        self.tiles = np.full((width, height), fill_value=Terrain.WALL, order='F')
        self.walkable = np.full((width, height), fill_value=False, order='F')
        self.explored = np.full((width, height), fill_value=False, order='F')
        self.visiting = np.full((width, height), fill_value=False, order='F')
        self.random = np.random.random((width, height))

        self.surface_middle: 'pygame.Surface' = pygame.Surface((width * GRID_SIZE, height * GRID_SIZE)).convert_alpha()
        self.surface_down: 'pygame.Surface' = pygame.Surface((width * GRID_SIZE, height * GRID_SIZE)).convert_alpha()
        self.surface_up: 'pygame.Surface' = pygame.Surface((width * GRID_SIZE, height * GRID_SIZE)).convert_alpha()

        # 其他信息
        self.entities: 'List[Entity]' = []
        self.rooms: 'List[RectangularRoom]' = []
        self.engine: 'Optional[Engine]' = None
        self.gamemap_render: 'Optional' = None
        self.tileset_test = Tiles()

    def add_room(self, room: 'RectangularRoom'):
        self.rooms.append(room)

    def __getitem__(self, item: Tuple[int, int]):
        x, y = item
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return Terrain.WALL
        else:
            return self.tiles[x, y]

    def player(self):
        return self.engine.player

    def update_map(self):
        self.visiting[:] = compute_fov(origin=(self.player().x, self.player().y), gamemap=self, radius=7)
        self.explored |= self.visiting
        self.update_surface()

    def update_surface(self):
        """负责更新应当渲染的 surface, 通常不需要每帧都渲染, 而是特定动作后渲染一次即可."""
        self.surface_down.fill((0, 0, 0, 0))
        self.surface_middle.fill((0, 0, 0, 0))
        self.surface_up.fill((0, 0, 0, 0))
        for c in range(self.width):
            for r in range(self.height):
                # 只渲染已访问地图
                if self.explored[c, r]:
                    # 使用 tileset_test 渲染地图
                    self.tileset_test.render_gamemap_tiles(self, (c, r))

                    # 若该块没有正在视野中, 再加一层记忆遮罩.
                    if not self.visiting[c, r]:
                        self.blit_middle(FogOfWar.explored_surface, (c, r))

    def blit_up(self, tile: 'Surface', pos: Tuple[int, int]):
        self.surface_up.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    def blit_middle(self, tile: 'Surface', pos: Tuple[int, int]):
        self.surface_middle.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    def blit_down(self, tile: 'Surface', pos: Tuple[int, int]):
        self.surface_down.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    def render_map_up(self):
        """渲染自己."""
        pre_screen_up.blit(self.surface_up, (0, 0))

    def render_map_middle(self):
        """渲染自己."""
        pre_screen_middle.blit(self.surface_middle, (0, 0))

    def render_map_down(self):
        """渲染自己."""
        pre_screen_down.blit(self.surface_down, (0, 0))

    def render_map(self):
        self.render_map_up()
        self.render_map_middle()
        self.render_map_down()

    def get_entities_in_xy(self, xy: Tuple[int, int]):
        """检索目标位置的第一个 entity."""
        for entity in self.entities:
            if entity.xy == xy:
                return entity
        return None

    def render(self):
        """分层渲染, 不需要考虑地图与实体顺序"""
        self.render_map()
        for entity in self.entities:
            entity.render()

    def place_entity(self, *, entity: 'Entity', position: 'Tuple[int, int]'):
        """将实体放入地图的某个位置."""
        # 先注册.
        entity.gamemap = self
        self.entities.append(entity)
        # 再放置.
        entity.x, entity.y = position
        # 最后更新 sprite 位置.
        entity.update_sprite_pos()


def tunnel_between(
        start: Tuple[int, int], end: Tuple[int, int]
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

        new_room.tiles[new_room.corner] = Terrain.WALL
        new_room.walkable[new_room.corner] = False

        if len(gamemap.rooms) != 0:
            for x, y in tunnel_between(new_room.center_xy, gamemap.rooms[-1].center_xy):
                new_room.tiles[x, y] = Terrain.EMPTY
                new_room.walkable[x, y] = True

        gamemap.add_room(new_room)

    gamemap.update_surface()

    return gamemap
