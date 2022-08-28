from dungeon.tileset.tiles_map import Tiles
from dungeon.gamemap import GameMap


class GameMapRender:
    """用于渲染地图.

    地图渲染元素分为两类：装饰类与非装饰类

    渲染的思路：

    1. 渲染非装饰类元素
    2. 渲染装饰类元素
    """
    def __init__(self, gamemap: 'GameMap', tiles: 'Tiles'):
        self.gamemap = gamemap
        gamemap.gamemap_render = self
        self.tiles = tiles
        self.width: int = gamemap.width

    def render_wall(self):
        pass

    def render_floor(self):
        pass

    def render_upper(self):
        pass