from pygame import Color
from pygame import Surface

class FogOfWar:
    explored = Color(0xCC, 0x99, 0x55, a=20)

    # explored but not visiting
    explored_surface = Surface((16, 16))
    explored_surface.fill(explored)
    explored_surface.set_alpha(100)

