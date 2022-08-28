import pygame
from dungeon import map_width, map_height, pre_screen_middle, screen, pre_screen
from dungeon.fonts import ipix_font
from dungeon.sprites.sprites_factory import SpriteManager
from dungeon.input_handler import MainEventHandler
from dungeon.gamemap import gen_gamemap
from dungeon.engine import Engine
from dungeon.components.message_manager import MessageManager
from dungeon.components import TileComponent
from dungeon.components.HUD import StatusPanel, HealthBar, BagButton, WaitButton, SearchButton
from dungeon.view_port import ViewPort
from dungeon.time_manager import TimeManager
from dungeon.actor import Actor
from utils.scaled_render import CompressRender
from utils.tile_load import load_image_with_alpha
from utils.surface import get_scaled_surface_by_factor

sprites_manager = SpriteManager("./meta/info.json")
cursor = get_scaled_surface_by_factor(load_image_with_alpha("./assets/gdx/cursor_mouse.png"), 2)


def main():
    rogue_sprite = sprites_manager['Bat'].clone()
    rogue = Actor(x=0, y=0, sprite=rogue_sprite, hp=25, mp=30, san=10)

    mob_sprite = sprites_manager['Thief'].clone()
    mob = Actor(x=0, y=0, sprite=mob_sprite, hp=2, mp=2, san=10)
    mob.game_time = 2

    message_manager = MessageManager(width=200, height=60, pos=(400, 600))

    gui_components = TileComponent(scale=3)
    gui_components.add_child(StatusPanel().add_child(HealthBar().attach_actor(rogue)))
    gui_components.add_child(BagButton())
    gui_components.add_child(WaitButton())
    gui_components.add_child(SearchButton())

    message_manager.log("test 1")
    message_manager.log("test 2")
    message_manager.log("test 3")

    view_port = ViewPort(
        size=(pre_screen_middle.get_width() // 2, pre_screen_middle.get_height() // 2),
        # size=(pre_screen_middle.get_width(), pre_screen_middle.get_height()),
        render_pos=(0, 0),
        inner_size=(10, 10),
        target=rogue,
        output_size=(pre_screen_middle.get_width(), pre_screen_middle.get_height()),
    )
    view_port.add_components(gui_components)

    input_handler = MainEventHandler()

    gamemap = gen_gamemap(map_width, map_height)
    gamemap.place_entity(entity=rogue, position=gamemap.rooms[-1].center_xy)
    gamemap.place_entity(entity=mob, position=(gamemap.rooms[-1].center_xy[0]+1, gamemap.rooms[-1].center_xy[1]+1))

    time_manager = TimeManager()
    time_manager.add_actor(rogue)
    time_manager.add_actor(mob)

    engine = Engine(
        player=rogue,
        input_handler=input_handler,
        gamemap=gamemap,
        time_manager=time_manager,
    )

    gamemap.update_map()

    while True:

        engine.run()
        CompressRender.render()
        view_port.render()
        message_manager.render_all()
        pre_screen.blit(cursor, pygame.mouse.get_pos())

        screen.blit(pre_screen, (0, 0))

        pygame.display.flip()

        CompressRender.clear()


if __name__ == '__main__':
    main()
