import pygame
from utils.compute_fov import compute_fov
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from dungeon.game_map import GameMap
    from dungeon.dsprite import DSprite
    from dungeon.engine import Engine


class Entity:
    def __init__(self, x: int = 0, y: int = 0, sprite: 'DSprite'=None):
        self.x = x
        self.y = y
        self.status = ""
        sprite.entity = self
        self.sprite = sprite
        self.gamemap: 'GameMap' = None
        self.engine: 'Engine' = None

    @property
    def xy(self):
        return self.x, self.y

    @property
    def pos(self):
        return 16*self.x, 16*self.y

    def render(self):
        self.sprite.render()

    def is_player(self):
        return self == self.gamemap.player()

    def move(self, direction: 'Tuple[int, int]'):
        dx, dy = direction
        self.x += dx
        self.y += dy
        if self.is_player():
            compute_fov(origin=(self.x, self.y), gamemap=self.gamemap, radius=7)
            self.gamemap.update_surface()
        # maybe add some trigger
        self.sprite.move(direction)
