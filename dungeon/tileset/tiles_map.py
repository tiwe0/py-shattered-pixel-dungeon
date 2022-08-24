from typing import Tuple, TYPE_CHECKING
from dungeon.dsprite import DSpriteSheetReader
from dungeon.tileset.terrain import Terrain

if TYPE_CHECKING:
    from dungeon.game_map import GameMap
    from pygame import Surface

tiles_sewers = DSpriteSheetReader("assets/environment/tiles_sewers.png", frame_width=16, frame_height=16)


def cr(row: int, col: int) -> int:
    return (row-1)*16+col-1


assert cr(1, 1) == 0
assert cr(1, 5) == 4
assert cr(4, 2) == 49


class Tiles:
    # GROUND
    wall_stitcheable_list = [
                         Terrain.WALL, Terrain.WALL_DECO, Terrain.SECRET_DOOR,
                         Terrain.LOCKED_EXIT, Terrain.UNLOCKED_EXIT, Terrain.BOOKSHELF
                            ]

    door_tiles_list = [
                   Terrain.DOOR, Terrain.LOCKED_DOOR, Terrain.CRYSTAL_DOOR, Terrain.OPEN_DOOR
                      ]

    floor_tiles_list = [
                    Terrain.WATER,
                       ]

    @classmethod
    def get_tile(cls, tile: int) -> 'Surface':
        return tiles_sewers[tile]

    @classmethod
    def door_tile(cls, tile: int):
                              return tile in cls.door_tiles_list

    @classmethod
    def wall_stitcheable(cls, tile: int):
                                     return tile in cls.wall_stitcheable_list

    @classmethod
    def stitch_WallOverhang_tile(cls, tile: int, right_below: int, below: int, left_below: int) -> int:
        if tile == Terrain.DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG
        elif tile == Terrain.OPEN_DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG_OPEN
        elif tile == Terrain.LOCKED_DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG_OPEN
        elif tile == Terrain.CRYSTAL_DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG_LOCKED
        elif below == Terrain.BOOKSHELF:
            visual = cls.WALL_OVERHANG_WOODEN
        else:
            visual = cls.WALL_OVERHANG

        if not cls.wall_stitcheable(right_below):
            visual += 1
        if not cls.wall_stitcheable(left_below):
            visual += 2

        return visual

    @classmethod
    def stitch_InternalWall_tile(cls, tile: int, right: int, right_below: int, below: int, left_below: int, left: int) -> int:
        if tile == Terrain.BOOKSHELF or below == Terrain.BOOKSHELF:
            result = cls.WALL_INTERNAL_WOODEN
        else:
            result = cls.WALL_INTERNAL

        if not cls.wall_stitcheable(right):
            right += 1
        if not cls.wall_stitcheable(right_below):
            result += 2
        if not cls.wall_stitcheable(left_below):
            result += 4
        if not cls.wall_stitcheable(left):
            result += 8

        return result

    @classmethod
    def get_RaisedWall_tile(cls, tile: int, pos: Tuple[int, int], right: int, below: int, left: int,) -> int:
        if below == -1 or cls.wall_stitcheable(below):
            return -1
        elif cls.door_tile(below):
            result = cls.RAISED_WALL_DOOR
        elif tile == Terrain.WALL or tile == Terrain.SECRET_DOOR:
            result = cls.RAISED_WALL
        elif tile == Terrain.WALL_DECO:
            result = cls.RAISED_WALL_DECO
        elif tile == Terrain.BOOKSHELF:
            result = cls.RAISED_WALL_BOOKSHELF
        else:
            return -1

        # TODO

        if not cls.wall_stitcheable(right):
            result += 1
        if not cls.wall_stitcheable(left):
            result += 2

        return result

    @classmethod
    def get_RaisedDoor_tile(cls, tile: int, below: int):
        if cls.wall_stitcheable(below):
            return cls.RAISED_DOOR_SIDEWAYS
        elif tile == Terrain.DOOR:
            return cls.RAISED_DOOR
        elif tile == Terrain.OPEN_DOOR:
            return cls.RAISED_DOOR_OPEN
        elif tile == Terrain.LOCKED_DOOR:
            return cls.RAISED_DOOR_LOCKED
        elif tile == Terrain.CRYSTAL_DOOR:
            return cls.RAISED_DOOR_CRYSTAL
        else:
            return -1

    GROUND = cr(1, 1)
    FLOOR = GROUND+0
    FLOOR_DECO = GROUND+1
    GRASS = GROUND+2
    EMBERS = GROUND+3
    FLOOR_SP = GROUND+4

    FLOOR_ALT_1 = GROUND+6
    FLOOR_DECO_ALT = GROUND+7
    GRASS_ALT = GROUND+8
    EMBERS_ALT = GROUND+9
    FLOOR_SP_ALT = GROUND+10

    FLOOR_ALT_2 = GROUND+12

    ENTRANCE = GROUND+16
    EXIT = GROUND+17
    WELL = GROUND+18
    EMPTY_WELL = GROUND+19
    PEDESTAL = GROUND+20

    # Chasm
    CHASM_index = cr(4, 1)
    CHASM = CHASM_index+0
    CHASM_FLOOR = CHASM_index+1
    CHASM_FLOOR_SP = CHASM_index+2
    CHASM_WALL = CHASM_index+3
    CHASM_WALL_SP = CHASM_index+4

    # Flat Tiles
    FLAT_WALLS = cr(5, 1)
    FLAT_WALL = FLAT_WALLS+0
    FLAT_WALL_DECO = FLAT_WALLS+1
    FLAT_BOOKSHELF = FLAT_WALLS+2

    FLAT_WALL_ALT = FLAT_WALLS+4
    FLAT_WALL_DECO_ALT = FLAT_WALLS+5
    FLAT_BOOKSHELF_ALT = FLAT_WALLS+6

    FLAT_DOORS = cr(6, 1)
    FLAT_DOOR = FLAT_DOORS+0
    FLAT_DOOR_OPEN = FLAT_DOORS+1
    FLAT_DOOR_LOCKED = FLAT_DOORS+2
    FLAT_DOOR_CRYSTAL = FLAT_DOORS+3
    UNLOCKED_EXIT = FLAT_DOORS+4
    LOCKED_EXIT = FLAT_DOORS+5

    FLAT_OTHER = cr(7, 1)
    FLAT_SIGN = FLAT_OTHER+0
    FLAT_STATUE = FLAT_OTHER+1
    FLAT_STATUE_SP = FLAT_OTHER+2
    FLAT_ALCHEMY_POT = FLAT_OTHER+3
    FLAT_BARRICADE = FLAT_OTHER+4
    FLAT_HIGH_GRASS = FLAT_OTHER+5
    FLAT_FURROWED_GRASS = FLAT_OTHER+6

    FLAT_HIGH_GRASS_ALT = FLAT_OTHER+8
    FLAT_FURROWED_ALT = FLAT_OTHER+9

    # Raised Tiles
    # Raised Walls
    RAISED_WALLS = cr(8, 1)
    RAISED_WALL = RAISED_WALLS+0
    RAISED_WALL_DECO = RAISED_WALLS+4
    RAISED_WALL_DOOR = RAISED_WALLS+8
    RAISED_WALL_BOOKSHELF = RAISED_WALLS+12

    RAISED_WALL_ALT = RAISED_WALLS+16
    RAISED_WALL_DECO_ALT = RAISED_WALLS+20
    RAISED_WALL_BOOKSHELF_ALT = RAISED_WALLS+28

    # Raised Doors
    RAISED_DOORS = cr(10, 1)
    RAISED_DOOR = RAISED_DOORS+0
    RAISED_DOOR_OPEN = RAISED_DOORS+1
    RAISED_DOOR_LOCKED = RAISED_DOORS+2
    RAISED_DOOR_CRYSTAL = RAISED_DOORS+3
    RAISED_DOOR_SIDEWAYS = RAISED_DOORS+4

    # Raised Other
    RAISED_OTHER = cr(11, 1)
    RAISED_SIGN = RAISED_OTHER+0
    RAISED_STATUE = RAISED_OTHER+1
    RAISED_STATUE_SP = RAISED_OTHER+2
    RAISED_ALCHEMY_POT = RAISED_OTHER+3
    RAISED_BARRICADE = RAISED_OTHER+4
    RAISED_HIGH_GRASS = RAISED_OTHER+5
    RAISED_FURROWED_GRASS = RAISED_OTHER+6

    RAISED_HIGH_GRASS_ALT = RAISED_OTHER+9
    RAISED_FURROWED_ALT = RAISED_OTHER+10

    # Raised Tiles Upper
    # +1for open right, +2 for open right-below, +4 for open left-below, +8 for open left.

    # Raised Walls
    WALLS_INTERNAL = cr(12, 1)

    WALL_INTERNAL = WALLS_INTERNAL+0
    WALL_INTERNAL_WOODEN = WALLS_INTERNAL+16

    WALLS_OVERHANG = cr(14, 1)
    WALL_OVERHANG = WALLS_OVERHANG+0
    DOOR_SIDEWAYS_OVERHANG = WALLS_OVERHANG+4
    DOOR_SIDEWAYS_OVERHANG_OPEN = WALLS_OVERHANG+8
    DOOR_SIDEWAYS_OVERHANG_LOCKED = WALLS_OVERHANG+12
    DOOR_SIDEWAYS_OVERHANG_CRYSTAL = WALLS_OVERHANG+16
    WALL_OVERHANG_WOODEN = WALLS_OVERHANG+20

    DOOR_OVERHANG = WALLS_OVERHANG+25
    DOOR_OVERHANG_OPEN = WALLS_OVERHANG+26
    DOOR_OVERHANG_CRYSTAL = WALLS_OVERHANG+27
    DOOR_SIDEWAYS = WALLS_OVERHANG+28
    DOOR_SIDEWAYS_LOCKED = WALLS_OVERHANG+29
    DOOR_SIDEWAYS_CRYSTAL = WALLS_OVERHANG+30

    STATUE_OVERHANG = WALLS_OVERHANG+32
    ALCHEMY_POT_OVERHANG = WALLS_OVERHANG+33
    BARRICADE_OVERHANG = WALLS_OVERHANG+34
    HIGH_GRASS_OVERHANG = WALLS_OVERHANG+35
    FURROWED_OVERHANG = WALLS_OVERHANG+36

    HIGH_GRASS_OVERHANG_ALT = WALLS_OVERHANG+38
    FURROWED_OVERHANG_ALT = WALLS_OVERHANG+39





