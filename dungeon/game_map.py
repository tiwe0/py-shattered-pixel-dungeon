import numpy as np
import random
from typing import Tuple, Iterator, List, TYPE_CHECKING, Set, Optional
import pygame
from dungeon.assets import Assets
from dungeon.dsprite import DSpriteSheetReader
from utils.line import line

if TYPE_CHECKING:
    from entity import Entity
    from dungeon.engine import Engine

# for test
tmp_test_tiles = DSpriteSheetReader(Assets.Environment.tiles_sewers, frame_width=16, frame_height=16, row=4)
wall_tile = tmp_test_tiles[48]
floor_tile = tmp_test_tiles[0]

tmp_hero_tiles = DSpriteSheetReader(Assets.Sprites.rogue, frame_width=12, frame_height=15, row=7)
hero_tile = tmp_hero_tiles[0]


class GameMap:
    max_room = 30
    min_room_width = 5
    min_room_height = 5
    max_room_width = 9
    max_room_height = 9

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=1, order='F')
        self.walkable = np.full((width, height), fill_value=False, order='F')
        self.visible = np.full((width, height), fill_value=False, order='F')
        self.entities: 'Set[Entity]' = set()
        self.surface: 'pygame.Surface' = pygame.Surface((width*16, height*16))
        self.rooms: 'List[RectangularRoom]'
        self.engine: 'Engine'

    def player(self):
        return self.engine.player
    def update_surface(self):
        self.surface.fill((0, 0, 0))
        for c in range(self.width):
            for r in range(self.height):
                if self.visible[c, r]:
                    if self.tiles[c, r] == 1:
                        self.surface.blit(wall_tile, (c*16, r*16))
                    else:
                        self.surface.blit(floor_tile, (c*16, r*16))

    def get_entities_in_xy(self, xy: Tuple[int, int]):
        for entity in self.entities:
            if entity.xy == xy:
                return entity
        return None

    def render(self, scale: 'int' = 1):
        screen = pygame.display.get_surface()
        screen.blit(self.surface, (0, 0))
        for entity in self.entities:
            entity.render()

    def place_entity(self, *, entity: 'Entity', position: 'Tuple[int, int]'):
        self.entities.add(entity)
        entity.x, entity.y = position
        entity.gamemap = self


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1, self.y1 = x, y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center_xy(self) -> Tuple[int, int]:
        return self.x1+self.width//2, self.y1+self.height//2

    @property
    def inner(self) -> Tuple[slice, slice]:
        return slice(self.x1+1, self.x2), slice(self.y1+1, self.y2)

    def intersects(self, other_room: 'RectangularRoom') -> bool:
        return (
            self.x1 <= other_room.x2
            and self.x2 >= other_room.x1
            and self.y1 <= other_room.y2
            and self.y2 >= other_room.y1
        )


def tunnel_between(
        start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    yield from line(start, end)


def gen_gamemap(map_width: int, map_height: int):
    gamemap = GameMap(map_width, map_height)
    rooms_list: 'List[RectangularRoom]' = []

    for i in range(gamemap.max_room):
        room_width = random.randint(gamemap.min_room_width, gamemap.max_room_width)
        room_height = random.randint(gamemap.min_room_height, gamemap.max_room_height)
        room_x = random.randint(0, gamemap.width-room_width)
        room_y = random.randint(0, gamemap.height-room_height)
        new_room = RectangularRoom(room_x, room_y, room_width, room_height)

        if any(new_room.intersects(r) for r in rooms_list):
            continue

        gamemap.tiles[new_room.inner] = 0
        gamemap.walkable[new_room.inner] = True

        if len(rooms_list) != 0:
            for x, y in tunnel_between(new_room.center_xy, rooms_list[-1].center_xy):
                gamemap.tiles[x, y] = 0
                gamemap.walkable[x, y] = True

        rooms_list.append(new_room)

    gamemap.rooms = rooms_list
    gamemap.update_surface()

    return gamemap
