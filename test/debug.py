from typing import Tuple, Iterable

from pygame import Surface

from dungeon import GRID_SIZE, pre_screen


class DebugRender:
    red = Surface((GRID_SIZE, GRID_SIZE))
    red.fill((255, 0, 0))
    red.set_alpha(150)

    green = Surface((GRID_SIZE, GRID_SIZE))
    green.fill((0, 255, 0))
    green.set_alpha(150)

    blue = Surface((GRID_SIZE, GRID_SIZE))
    blue.fill((0, 0, 255))
    green.set_alpha(150)

    color_map = {
        'red': red,
        'green': green,
        'blue': blue,
    }

    @classmethod
    def render_tile_block(cls, tile: 'Surface', pos: Tuple[int, int]):
        pre_screen.blit(tile, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE))

    @classmethod
    def render_tile_blocks(cls, tile: 'Surface', positions: Iterable[Tuple[int, int]]):
        for pos in positions:
            cls.render_tile_block(tile, pos)

    @classmethod
    def render_color_block(cls, color: 'str', pos: Tuple[int, int]):
        c = cls.color_map[color]
        cls.render_tile_block(c, pos)

    @classmethod
    def render_color_blocks(cls, color: 'str', positions: Iterable[Tuple[int, int]]):
        for pos in positions:
            cls.render_color_block(color, pos)
