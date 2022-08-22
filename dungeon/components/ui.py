from typing import Tuple
import pygame
from pygame import Surface

from dungeon import pre_screen
from dungeon.components import Component
from dungeon.tileset.tiles_ui import Tiles


class HUDComponent(Component):

    def __init__(self, tile: 'Surface', pos: Tuple[int, int] = (0, 0), scale: int = 1):
        super(HUDComponent, self).__init__()
        self.tile: 'Surface' = tile
        self.x, self.y = pos
        self.scale = scale

    @property
    def width(self):
        return self.tile.get_width()

    @property
    def height(self):
        return self.tile.get_height()

    @property
    def size(self):
        return self.width, self.height

    def scaled_size(self):
        return self.scale*self.width, self.scale*self.height

    def render(self):
        scaled_tile = pygame.Surface(self.scaled_size()).convert_alpha()
        pygame.transform.scale(self.tile, self.scaled_size(), scaled_tile)
        pre_screen.blit(scaled_tile, (self.x, self.y))


class StatusPanel(HUDComponent):
    def __init__(self, pos: Tuple[int, int] = (0, 0), scale: int = 1):
        tile = Tiles.Interface.status_panel
        super(StatusPanel, self).__init__(tile=tile, pos=pos, scale=scale)
