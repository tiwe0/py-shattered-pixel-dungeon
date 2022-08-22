import pygame
from dungeon import sprites_manager
from dungeon.input_handler import MainEventHandler
from dungeon.entity import Entity
from dungeon.game_map import gen_gamemap
from dungeon.engine import Engine
from utils.compute_fov import compute_fov


def main():
    map_width = 40
    map_height = 30
    screen = pygame.display.set_mode((map_width*32, map_height*32))
    pygame.display.set_caption('Test Stage')

    rogue_sprite = sprites_manager['Thief'].clone()

    rogue = Entity(x=0, y=0, sprite=rogue_sprite)

    gamemap = gen_gamemap(map_width, map_height)
    gamemap.place_entity(entity=rogue, position=gamemap.rooms[-1].center_xy)

    engine = Engine(
        player=rogue,
        input_handler=MainEventHandler,
        gamemap=gamemap,
    )

    gamemap.update_map()

    while True:

        engine.run()

        render_surface = pygame.transform.scale(
            screen,
            (screen.get_width()*2, screen.get_height()*2)
        )
        screen.fill((0, 0, 0))
        screen.blit(render_surface, (0, 0))

        pygame.display.flip()


if __name__ == '__main__':
    main()
