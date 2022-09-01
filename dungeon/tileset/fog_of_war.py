from pygame import Color
from pygame import Surface

from dungeon.config import GRID_SIZE


class FogOfWar:
    explored = Color(0xCC, 0x99, 0x55, a=20)
    unknown = Color(0, 0, 0, 0)
    transparent = Color(0, 0, 0, a=0)

    # explored but not visiting
    explored_surface = Surface((GRID_SIZE, GRID_SIZE))
    explored_surface.fill(explored)
    explored_surface.set_alpha(100)

    unknown_surface = Surface((GRID_SIZE, GRID_SIZE))
    unknown_surface.fill(unknown)
