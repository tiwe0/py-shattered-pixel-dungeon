from typing import Tuple
import pygame


def load_image(filepath: str) -> pygame.Surface:
    surface = pygame.image.load(filepath)
    try:
        surface.convert_alpha()
    except Exception as e:
        pass
    return surface


def load_tile(filepath: str, pos: Tuple[int, int], size: Tuple[int, int]) -> pygame.Surface:
    surface = load_image(filepath)
    tile_surface = surface.subsurface(*pos, *size).copy()
    try:
        tile_surface.convert_alpha()
    except Exception as e:
        pass
    return tile_surface

