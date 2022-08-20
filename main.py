import pygame
from dungeon.input_handler import MainEventHandler
from dungeon.dsprite import DSprite, DAnimation, DSpriteSheetReader
from dungeon.assets import Assets
from dungeon.entity import Entity
from dungeon.game_map import gen_gamemap
from dungeon.engine import Engine
from utils.compute_fov import compute_fov


def main():
    map_width = 40
    map_height = 30
    pygame.init()
    screen = pygame.display.set_mode((map_width*32, map_height*32))
    pygame.display.set_caption('Test Stage')

    rogue_dsprite_sheet_reader = DSpriteSheetReader(Assets.Sprites.rogue, frame_width=12, frame_height=15)

    rogue_idle_animation = DAnimation(
        status='idle',
        frames=rogue_dsprite_sheet_reader,
        fps=1,
        key_frame=[0, 1, 0, 0],
        loop=True
    )

    rogue_run_animation = DAnimation(
        status='run',
        frames=rogue_dsprite_sheet_reader,
        fps=15,
        key_frame=[2, 3, 4, 5, 6, 7],
        loop=True
    )

    rogue_sprite = DSprite()
    rogue_sprite.add_animation(rogue_idle_animation)
    rogue_sprite.add_animation(rogue_run_animation)

    rogue = Entity(x=0, y=0, sprite=rogue_sprite)

    gamemap = gen_gamemap(map_width, map_height)
    gamemap.place_entity(entity=rogue, position=gamemap.rooms[-1].center_xy)
    rogue_sprite.entity = rogue

    engine = Engine(
        player=rogue,
        input_handler=MainEventHandler,
        gamemap=gamemap,
    )

    compute_fov(origin=(rogue.x, rogue.y), gamemap=gamemap, radius=7)

    gamemap.update_surface()

    gamemap.render()

    render_surface = pygame.transform.scale(
        screen,
        (screen.get_width()*2, screen.get_height()*2)
    )
    screen.fill((0, 0, 0))
    screen.blit(render_surface, (0, 0))

    pygame.display.flip()

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
