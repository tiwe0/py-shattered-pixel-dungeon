from typing import Tuple, TYPE_CHECKING

import pygame
from pygame import Surface

from dungeon import screen_width, screen_height, GRID_SIZE, pre_screen_down, pre_screen_middle, pre_screen_up
from dungeon.tileset.fog_of_war import FogOfWar
from dungeon.tileset.tiles_map import TilesMap

if TYPE_CHECKING:
    from dungeon.gamemap import GameMap


class GameMapRender:
    """用于渲染地图.

    地图渲染元素分为两类：装饰类与非装饰类

    渲染的思路：

    1. 渲染非装饰类元素
    2. 渲染装饰类元素
    """

    def __init__(self, gamemap: 'GameMap'):
        self._gamemap = gamemap
        gamemap.gamemap_render = self
        self.width = gamemap.width
        self.height = gamemap.height
        self.surface_down: 'Surface' = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.surface_middle: 'Surface' = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.surface_up: 'Surface' = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.tiles_map = TilesMap()

    def clear_surfaces(self):
        self.surface_down.fill((0, 0, 0, 0))
        self.surface_middle.fill((0, 0, 0, 0))
        self.surface_up.fill((0, 0, 0, 0))

    def update_surface(self):
        self.clear_surfaces()
        for x in range(self.width):
            for y in range(self.height):
                if self.gamemap.explored[x, y]:
                    self.render_gamemap_tiles((x, y))
                else:
                    self.render_gamemap_fow((x, y))

    def render_gamemap_tiles(self, pos: Tuple[int, int]):
        gamemap = self.gamemap
        tiles_map = self.tiles_map
        if gamemap.visiting[pos]:
            self.render_gamemap_tiles_down_layer(pos)
            self.render_gamemap_tiles_up_layer(pos)
        else:
            down_tile = tiles_map.get_raised_tile_from_terrain(gamemap, pos, gamemap.get_tile(pos))
            self.blit_up(down_tile, pos)
            self.blit_up(FogOfWar.explored_surface, pos)
            up_tile = tiles_map.get_raised_tile_from_wall(gamemap, pos, gamemap.get_tile(pos))
            if up_tile:
                self.blit_up(up_tile, pos)

    def render_gamemap_tiles_down_layer(self, pos):
        down_tile = self.tiles_map.get_raised_tile_from_terrain(self.gamemap, pos, self.gamemap.get_tile(pos))
        self.blit_down(down_tile, pos)

    def render_gamemap_tiles_up_layer(self, pos):
        up_tile = self.tiles_map.get_raised_tile_from_wall(self.gamemap, pos, self.gamemap.get_tile(pos))
        if up_tile:
            self.blit_up(up_tile, pos)

    def render_gamemap_fow(self, pos):
        self.blit_up(FogOfWar.unknown_surface, pos)

    def blit_up(self, tile: 'Surface', pos: Tuple[int, int]):
        self.surface_up.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    def blit_middle(self, tile: 'Surface', pos: Tuple[int, int]):
        self.surface_middle.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    def blit_down(self, tile: 'Surface', pos: Tuple[int, int]):
        self.surface_down.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    def render(self):
        self.render_to_pre_screen_down()
        self.render_to_pre_screen_middle()
        self.render_to_pre_screen_up()

    def render_to_pre_screen_down(self):
        pre_screen_down.blit(self.surface_down, (0, 0))

    def render_to_pre_screen_middle(self):
        pre_screen_middle.blit(self.surface_middle, (0, 0))

    def render_to_pre_screen_up(self):
        pre_screen_up.blit(self.surface_up, (0, 0))

    @property
    def gamemap(self):
        return self._gamemap

    @gamemap.setter
    def gamemap(self, value: 'GameMap'):
        self._gamemap = value
        value.gamemap_render = self
