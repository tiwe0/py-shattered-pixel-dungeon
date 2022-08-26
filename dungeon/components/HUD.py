from typing import Tuple, TYPE_CHECKING

from pygame import Surface

from dungeon import screen_width, screen_height
from dungeon.components import Component
from dungeon.tileset.tiles_ui import Tiles
from utils.surface import get_scaled_surface

if TYPE_CHECKING:
    from dungeon.actor import Actor


class HUDComponent(Component):

    def __init__(self, tile: 'Surface', pos: Tuple[int, int] = (0, 0), **kwargs):
        super(HUDComponent, self).__init__(**kwargs)
        self._tile: 'Surface' = tile
        self.pos = pos

    @property
    def tile(self) -> Surface:
        return self.before_render()

    @property
    def width(self):
        return self._tile.get_width()

    @property
    def height(self):
        return self._tile.get_height()

    def before_render(self) -> Surface:
        return self._tile

    def render(self) -> None:
        self.pre_surface.blit(self.tile, self.pos)


class StatusPanel(HUDComponent):
    def __init__(self, pos: Tuple[int, int] = (0, 0), **kwargs):
        tile = Tiles.Interface.status_panel
        super(StatusPanel, self).__init__(tile=tile, pos=pos, **kwargs)


# TODO 用元编程写HUDBar


class HealthBar(HUDComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.health_bar
        super(HealthBar, self).__init__(tile=tile, **kwargs)
        self.health_ratio = 1.0
        self.pos = (30, 3)

    def attach_actor(self, actor: 'Actor'):
        actor.heal_bar = self
        return self

    def update_health_bar(self, ratio: float):
        self.health_ratio = ratio

    def before_render(self) -> Surface:
        return get_scaled_surface(self._tile, (self.width * self.health_ratio, self.height))

class BagButton(HUDComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.bag_button
        super(BagButton, self).__init__(tile=tile, **kwargs)
        self.pos = (0, screen_height-tile.get_height())

class WaitButton(HUDComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.wait_button
        super(WaitButton, self).__init__(tile=tile, **kwargs)
        self.pos = (24, screen_height-tile.get_height())

class SearchButton(HUDComponent):
    def __init__(self, **kwargs):
        tile = Tiles.Interface.search_button
        super(SearchButton, self).__init__(tile=tile, **kwargs)
        self.pos = (24+20, screen_height-tile.get_height())
