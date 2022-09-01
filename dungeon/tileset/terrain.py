from utils.typing import map_tile_type
import numpy as np


class Terrain:
    CHASM = 0
    EMPTY = 1
    GRASS = 2
    EMPTY_WELL = 3
    WALL = 4
    DOOR = 5
    OPEN_DOOR = 6
    ENTRANCE = 7
    EXIT = 8
    EMBERS = 9
    LOCKED_DOOR = 10
    CRYSTAL_DOOR = 31
    PEDESTAL = 11
    WALL_DECO = 12
    BARRICADE = 13
    EMPTY_SP = 14
    HIGH_GRASS = 15
    FURROWED_GRASS = 30
    SECRET_DOOR = 16
    SECRET_TRAP = 17
    TRAP = 18
    INACTIVE_TRAP = 19
    EMPTY_DECO = 20
    LOCKED_EXIT = 21
    UNLOCKED_EXIT = 22
    SIGN = 23
    WELL = 24
    STATUE = 25
    STATUE_SP = 26
    BOOKSHELF = 27
    ALCHEMY = 28
    WATER = 29

    info = {
        # EXAMPLE           (tiles,          weight,    random, walkable, explored, visiting),
        # not walkable
        CHASM:              (CHASM,          np.inf,    0,      False, False, False),
        LOCKED_DOOR:        (LOCKED_DOOR,    np.inf,    0,      True,  False, False),
        CRYSTAL_DOOR:       (CRYSTAL_DOOR,   np.inf,    0,      True,  False, False),
        LOCKED_EXIT:        (LOCKED_EXIT,    np.inf,    0,      True,  False, False),
        UNLOCKED_EXIT:      (UNLOCKED_EXIT,  np.inf,    0,      True,  False, False),
        STATUE:             (STATUE,         np.inf,    0,      True,  False, False),
        STATUE_SP:          (STATUE_SP,      np.inf,    0,      True,  False, False),
        BOOKSHELF:          (BOOKSHELF,      np.inf,    0,      True,  False, False),

        # walkable
        EMPTY:              (EMPTY,          1,         0,      True, False, False),
        GRASS:              (GRASS,          1,         0,      True, False, False),
        EMPTY_WELL:         (EMPTY_WELL,     1,         0,      True, False, False),
        WALL:               (WALL,           1,         0,      True, False, False),
        DOOR:               (DOOR,           1,         0,      True, False, False),
        OPEN_DOOR:          (OPEN_DOOR,      1,         0,      True, False, False),
        ENTRANCE:           (ENTRANCE,       1,         0,      True, False, False),
        EXIT:               (EXIT,           1,         0,      True, False, False),
        EMBERS:             (EMBERS,         1,         0,      True, False, False),
        PEDESTAL:           (PEDESTAL,       1,         0,      True, False, False),
        WALL_DECO:          (WALL_DECO,      1,         0,      True, False, False),
        BARRICADE:          (BARRICADE,      1,         0,      True, False, False),
        EMPTY_SP:           (EMPTY_SP,       1,         0,      True, False, False),
        HIGH_GRASS:         (HIGH_GRASS,     1,         0,      True, False, False),
        FURROWED_GRASS:     (FURROWED_GRASS, 1,         0,      True, False, False),
        SECRET_DOOR:        (SECRET_DOOR,    1,         0,      True, False, False),
        SECRET_TRAP:        (SECRET_TRAP,    1,         0,      True, False, False),
        TRAP:               (TRAP,           1,         0,      True, False, False),
        INACTIVE_TRAP:      (INACTIVE_TRAP,  1,         0,      True, False, False),
        EMPTY_DECO:         (EMPTY_DECO,     1,         0,      True, False, False),
        SIGN:               (SIGN,           1,         0,      True, False, False),
        WELL:               (WELL,           1,         0,      True, False, False),
        ALCHEMY:            (ALCHEMY,        1,         0,      True, False, False),
        WATER:              (WATER,          1,         0,      True, False, False),
    }

    @classmethod
    def get_map_tile(cls, tile_code: int):
        return np.array(cls.info[tile_code], dtype=map_tile_type)
