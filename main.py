import pygame
from typing import Type
from dungeon.sprites.sprites_factory import SpriteManager
from dungeon import map_width, map_height, pre_screen, screen
from dungeon.input_handler import MainEventHandler
from dungeon.entity import Entity
from dungeon.game_map import gen_gamemap
from dungeon.engine import Engine
from dungeon.components import Component
from dungeon.components.ui import StatusPanel
from dungeon.view_port import ViewPort

c = Component()
c.add(StatusPanel(scale=2))
sprites_manager = SpriteManager("./meta/info.json")


def main():
    rogue_sprite = sprites_manager['Bat'].clone()

    rogue = Entity(x=0, y=0, sprite=rogue_sprite)

    view_port = ViewPort(
        size=(pre_screen.get_width()//2, pre_screen.get_height()//2),
        render_pos=(0, 0),
        inner_size=(100, 100),
        target=rogue,
    )

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
        c.render_all()
        view_port.render()

        render_surface = pygame.transform.scale(
            pre_screen,
            (pre_screen.get_width()*2, pre_screen.get_height()*2)
        )
        pre_screen.fill((0, 0, 0))
        screen.blit(render_surface, (0, 0))

        pygame.display.flip()


if __name__ == '__main__':
    main()
