import pygame
if not pygame.get_init():
    pygame.init()

pygame.init()
map_width = 40
map_height = 30
screen = pygame.display.set_mode((map_width*32, map_height*32))
pre_screen = pygame.Surface((map_width*32, map_height*32)).convert_alpha()
pygame.display.set_caption('Test Stage')

