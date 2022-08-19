import pygame
from dungeon.input_handler import MainEventHandler
from dungeon.dsprite import DSprite, DAnimation, DSpriteSheetReader
from dungeon.assets import DAssets
from dungeon.entity import Entity
from dungeon.game_map import gen_gamemap


def test_stage_with_handler():
    map_width = 80
    map_height = 40
    pygame.init()
    screen = pygame.display.set_mode((map_width*32, map_height*32))
    pygame.display.set_caption('Test Stage')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    rogue_dsprite_sheet_reader = DSpriteSheetReader(DAssets.Sprites.rogue, frame_width=12, frame_height=15)

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

    MainEventHandler.entity = rogue

    gamemap = gen_gamemap(map_width, map_height)
    gamemap.place_entity(entity=rogue, position=gamemap.rooms[-1].center_xy)
    rogue_sprite.entity = rogue

    while True:
        MainEventHandler.handle_event()

        gamemap.render()

        render_surface = pygame.transform.scale(
            screen,
            (screen.get_width()*2, screen.get_height()*2)
        )
        screen.fill((0, 0, 0))
        screen.blit(render_surface, (0, 0))

        pygame.display.flip()


test_stage_with_handler()
