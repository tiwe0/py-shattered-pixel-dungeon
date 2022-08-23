import pygame
from typing import Tuple
from pygame import Surface


def get_scaled_surface_(source: Surface, size: Tuple[int, int]):
    scaled_surface = Surface(size).convert_alpha()
    pygame.transform.scale(source, size, scaled_surface)
    source.blit(scaled_surface, (0, 0))
    return source


def get_scaled_surface_by_factor_(source: Surface, factor: int):
    size = factor*source.get_width(), factor*source.get_height()
    return get_scaled_surface_(source, size)


def get_scaled_surface_with_cut(source: Surface, size: Tuple[int, int]):
    scaled_surface = Surface(size).convert_alpha()
    pygame.transform.scale(source, size, scaled_surface)
    return scaled_surface.subsurface(0, 0, source.get_width(), source.get_height())


def get_scaled_surface_by_factor_with_cut(source: Surface, factor: int):
    size = factor*source.get_width(), factor*source.get_height()
    return get_scaled_surface_with_cut(source, size)


def get_scaled_surface(source: Surface, size: Tuple[int, int]):
    scaled_surface = Surface(size).convert_alpha()
    pygame.transform.scale(source, size, scaled_surface)
    return scaled_surface


def get_scaled_surface_by_factor(source: Surface, factor: int):
    size = factor*source.get_width(), factor*source.get_height()
    return get_scaled_surface(source, size)

