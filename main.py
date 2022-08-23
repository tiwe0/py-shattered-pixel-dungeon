import pygame
from typing import Type
from dungeon.sprites.sprites_factory import SpriteManager
from dungeon import map_width, map_height, pre_screen
from dungeon.input_handler import MainEventHandler
from dungeon.entity import Entity
from dungeon.game_map import gen_gamemap
from dungeon.engine import Engine
from dungeon.components import Component
from dungeon.components.HUD import StatusPanel, HealthBar
from dungeon.view_port import ViewPort
from dungeon.actor import Actor
from utils.scaled_render import ScaledRender

sprites_manager = SpriteManager("./meta/info.json")


def main():
    rogue_sprite = sprites_manager['Bat'].clone()

    rogue = Actor(x=0, y=0, sprite=rogue_sprite, hp=25, mp=30, san=10)

    gui_components = Component()
    gui_components.add_child(StatusPanel(scale=4).add_child(HealthBar().attach_actor(rogue)))

    view_port = ViewPort(
        size=(pre_screen.get_width()//2, pre_screen.get_height()//2),
        render_pos=(0, 0),
        inner_size=(100, 100),
        target=rogue,
        output_size=(pre_screen.get_width(), pre_screen.get_height()),
    )

    view_port.add_components(gui_components)

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
        view_port.render()
        ScaledRender.render(scale=1)

        pygame.display.flip()


if __name__ == '__main__':
    main()
