from typing import Tuple, TYPE_CHECKING

from pygame import Surface

from dungeon.components import TileComponent
from dungeon.tileset.tiles_ui import Tiles
from utils.surface import get_scaled_surface

if TYPE_CHECKING:
    from dungeon.actor import Actor


class StatusPanel(TileComponent):
    def __init__(self, pos: Tuple[int, int] = (0, 0), **kwargs):
        tile = Tiles.Interface.status_panel
        super(StatusPanel, self).__init__(tile=tile, pos=pos, **kwargs)


# TODO 用元编程写HUDBar


class HealthBar(TileComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.health_bar
        super(HealthBar, self).__init__(tile=tile, **kwargs)
        self.health_ratio = 0
        self.pos = (30, 3)
        self.width = tile.get_width()
        self.height = tile.get_height()
        self.actor = None

    def attach_actor(self, actor: 'Actor'):
        self.actor = actor
        return self

    def before_render(self):
        self.health_ratio = (float(self.actor.hp) / self.actor.max_hp)

    def render(self) -> Surface:
        return get_scaled_surface(self.tile, (self.width * self.health_ratio, self.height))


class BagButton(TileComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.bag_button
        pos = (0, 198)
        # pos = (0, screen_height-tile.get_height())
        super(BagButton, self).__init__(tile=tile, pos=pos, **kwargs)


class WaitButton(TileComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.wait_button
        pos = (24, 198)
        # pos = (24, screen_height-tile.get_height())
        super(WaitButton, self).__init__(tile=tile, pos=pos, **kwargs)


class SearchButton(TileComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.search_button
        pos = (24 + 20, 198)
        # pos = (24+20, screen_height-tile.get_height())
        super(SearchButton, self).__init__(tile=tile, pos=pos, **kwargs)
