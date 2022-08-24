import pygame
from dungeon import map_width, map_height, pre_screen
from dungeon.sprites.sprites_factory import SpriteManager
from dungeon.input_handler import MainEventHandler
from dungeon.game_map import gen_gamemap
from dungeon.engine import Engine
from dungeon.components import Component
from dungeon.components.HUD import StatusPanel, HealthBar
from dungeon.view_port import ViewPort
from dungeon.time_manager import TimeManager
from dungeon.actor import Actor
from utils.scaled_render import ScaledRender
from utils.tile_load import load_image_with_alpha
from utils.surface import get_scaled_surface_by_factor

sprites_manager = SpriteManager("./meta/info.json")
cursor = get_scaled_surface_by_factor(load_image_with_alpha("./assets/gdx/cursor_mouse.png"), 2)


def main():
    rogue_sprite = sprites_manager['Bat'].clone()

    rogue = Actor(x=0, y=0, sprite=rogue_sprite, hp=25, mp=30, san=10)

    gui_components = Component()
    gui_components.add_child(StatusPanel(scale=2).add_child(HealthBar().attach_actor(rogue)))

    view_port = ViewPort(
        size=(pre_screen.get_width()//2, pre_screen.get_height()//2),
        render_pos=(0, 0),
        inner_size=(10, 10),
        target=rogue,
        output_size=(pre_screen.get_width(), pre_screen.get_height()),
    )
    view_port.add_components(gui_components)

    input_handler = MainEventHandler()

    gamemap = gen_gamemap(map_width, map_height)
    gamemap.place_entity(entity=rogue, position=gamemap.rooms[-1].center_xy)

    time_manager = TimeManager()
    time_manager.add_actor(rogue)

    engine = Engine(
        player=rogue,
        input_handler=input_handler,
        gamemap=gamemap,
        time_manager=time_manager,
    )

    gamemap.update_map()

    while True:

        engine.run()
        view_port.render()
        pre_screen.blit(cursor, pygame.mouse.get_pos())
        ScaledRender.render(scale=1)


        pygame.display.flip()


if __name__ == '__main__':
    main()
