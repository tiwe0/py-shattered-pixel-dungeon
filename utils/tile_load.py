from typing import Tuple
import pygame


def load_image_with_alpha(filepath: str) -> pygame.Surface:
    surface = pygame.image.load(filepath)
    surface = surface.convert_alpha()
    return surface


def load_tile(filepath: str, pos: Tuple[int, int], size: Tuple[int, int]) -> pygame.Surface:
    surface = load_image_with_alpha(filepath)
    tile_surface = surface.subsurface(*pos, *size).copy()
    return tile_surface

