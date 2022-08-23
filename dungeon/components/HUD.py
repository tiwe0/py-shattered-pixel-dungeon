from typing import Tuple
import pygame
from pygame import Surface

from dungeon import pre_screen
from dungeon.components import Component
from dungeon.tileset.tiles_ui import Tiles


class HUDComponent(Component):

    def __init__(self, tile: 'Surface', pos: Tuple[int, int] = (0, 0), **kwargs):
        super(HUDComponent, self).__init__(**kwargs)
        self.tile: 'Surface' = tile
        self.pos = pos

    def render(self):
        self.pre_surface.blit(self.tile, self.pos)


class StatusPanel(HUDComponent):
    def __init__(self, pos: Tuple[int, int] = (0, 0), **kwargs):
        tile = Tiles.Interface.status_panel
        super(StatusPanel, self).__init__(tile=tile, pos=pos, **kwargs)
