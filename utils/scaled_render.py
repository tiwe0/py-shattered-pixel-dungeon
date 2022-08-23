from dungeon import screen, pre_screen
from utils.surface import get_scaled_surface_by_factor_with_cut


class ScaledRender:

    @staticmethod
    def render(scale: int = 1):
        if scale == 1:
            screen.blit(pre_screen, (0, 0))
        else:
            scaled_screen = get_scaled_surface_by_factor_with_cut(pre_screen, factor=scale)
            screen.blit(scaled_screen, (0, 0))
        pre_screen.fill((0, 0, 0, 0))
