from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dungeon.entity import Entity
    from dungeon.input_handler import MainEventHandler
    from dungeon.game_map import GameMap


class Engine:
    def __init__(
            self,
            player: 'Entity',
            input_handler: 'MainEventHandler',
            gamemap: 'GameMap'
    ):
        self.player: 'Entity' = player
        self.input_handler: 'MainEventHandler' = input_handler
        self.input_handler.player = player
        self.gamemap: 'GameMap' = gamemap
        self.gamemap.engine = self

    def handle_event(self):
        self.input_handler.handle_event()

    def render(self):
        self.gamemap.render()

    def run(self):
        self.handle_event()
        self.render()