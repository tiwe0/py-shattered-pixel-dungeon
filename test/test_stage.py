import pygame
from pygame.locals import *


def test_stage(func):
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Test Stage')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        func(screen)
        render_surface = pygame.transform.scale(screen, (screen.get_width() * 4, screen.get_height() * 4))
        screen.blit(render_surface, (0, 0))

        pygame.display.flip()

        screen.fill((250, 250, 250))
