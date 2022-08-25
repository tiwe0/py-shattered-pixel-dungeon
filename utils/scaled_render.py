from dungeon import screen, pre_screen_middle, pre_screen_down, pre_screen_up, pre_screen
from utils.surface import get_scaled_surface_by_factor_with_cut
from pygame import Surface
from pygame.display import get_surface


class MultipleSurfaceManager:
    DOWN = 0
    MIDDLE = 1
    UP = 2

    _surfaces = {
        DOWN: None,
        MIDDLE: None,
        UP: None,
    }

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(cls).__new__()
        return cls._instance

    def __init__(self):
        real_screen = get_surface()
        for key, value in self._surfaces.items():
            if value is None:
                self._surfaces[key] = Surface((real_screen.get_width(), real_screen.get_height())).convert_alpha()


class CompressRender:

    @staticmethod
    def render():
        pre_screen.blit(pre_screen_down, (0, 0))
        pre_screen.blit(pre_screen_middle, (0, 0))
        pre_screen.blit(pre_screen_up, (0, 0))

    @staticmethod
    def clear():
        pre_screen_down.fill((0, 0, 0, 0))
        pre_screen_middle.fill((0, 0, 0, 0))
        pre_screen_up.fill((0, 0, 0, 0))
        pre_screen.fill((0, 0, 0, 0))
        screen.fill((0, 0, 0, 0))
