import pygame
from pygame import Surface

if not pygame.get_init():
    pygame.init()

pygame.init()
map_width = 40
map_height = 40
screen = pygame.display.set_mode((map_width * 16, map_height * 16))
pre_screen = Surface((screen.get_width(), screen.get_height())).convert_alpha()
pygame.display.set_caption('Test Stage')
