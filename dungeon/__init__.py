import pygame
from pygame import Surface

from dungeon.config import GRID_SIZE
from dungeon.time_manager import TimeManager

if not pygame.get_init():
    pygame.init()

time_manager = TimeManager()
pygame.init()
map_width = 40
map_height = 40
screen = pygame.display.set_mode((map_width * GRID_SIZE, map_height * GRID_SIZE))
pre_screen = Surface((screen.get_width(), screen.get_height())).convert_alpha()
pygame.display.set_caption('Test Stage')
pygame.mouse.set_visible(False)
