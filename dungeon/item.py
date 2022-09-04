from typing import Optional
from pygame import Surface
from dungeon.entity import Entity


class Item(Entity):
    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.weight = 1
        self.tile: 'Optional[Surface]' = None
        self.category: 'str' = ''


class Potion(Item):
    pass

