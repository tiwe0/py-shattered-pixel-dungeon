from typing import Tuple, TYPE_CHECKING, Optional
from dungeon.dsprite import DSpriteSheetReader
from dungeon.tileset.terrain import Terrain

if TYPE_CHECKING:
    from dungeon.gamemap.__init__ import GameMap
    from pygame import Surface


def cr(row: int, col: int) -> int:
    return (row-1)*16+col-1


class Tiles:

    _instances = {
        'sewers': None,
        'prison': None,
        'caves': None,
        'city': None,
        'halls': None,
    }

    tiles_dict = {
        "sewers": DSpriteSheetReader("assets/environment/tiles_sewers.png", frame_width=16, frame_height=16),
        "prison": DSpriteSheetReader("assets/environment/tiles_prison.png", frame_width=16, frame_height=16),
        "city": DSpriteSheetReader("assets/environment/tiles_city.png", frame_width=16, frame_height=16),
        "halls": DSpriteSheetReader("assets/environment/tiles_halls.png", frame_width=16, frame_height=16),
        "caves": DSpriteSheetReader("assets/environment/tiles_caves.png", frame_width=16, frame_height=16),
    }

    # GROUND
    wall_stitchable_list = [
        Terrain.WALL, Terrain.WALL_DECO, Terrain.SECRET_DOOR,
        Terrain.LOCKED_EXIT, Terrain.UNLOCKED_EXIT, Terrain.BOOKSHELF
    ]

    door_tiles_list = [
        Terrain.DOOR, Terrain.LOCKED_DOOR, Terrain.CRYSTAL_DOOR, Terrain.OPEN_DOOR
    ]

    floor_tiles_list = [
        Terrain.WATER,
    ]

    NULL_TILE = -1

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

    # 直接查询
    direct_tiles_dict = {
        Terrain.EMPTY: FLOOR,
        Terrain.GRASS: GRASS,
        Terrain.EMPTY_WELL: EMPTY_WELL,
        Terrain.ENTRANCE: ENTRANCE,
        Terrain.EXIT: EXIT,
        Terrain.EMBERS: EMBERS,
        Terrain.PEDESTAL: PEDESTAL,
        Terrain.EMPTY_SP: FLOOR_SP,

        Terrain.SECRET_TRAP: FLOOR,
        Terrain.TRAP: FLOOR,
        Terrain.INACTIVE_TRAP: FLOOR,

        Terrain.EMPTY_DECO: FLOOR_DECO,
        Terrain.LOCKED_EXIT: LOCKED_EXIT,
        Terrain.UNLOCKED_EXIT: UNLOCKED_EXIT,
        Terrain.WELL: WELL,
    }

    # 可替换
    common_alt_tiles_dict = {
        FLOOR: FLOOR_ALT_1,
        GRASS: GRASS_ALT,
        FLAT_WALL: FLAT_WALL_ALT,
        EMBERS: EMBERS_ALT,
        FLAT_WALL_DECO: FLAT_WALL_DECO_ALT,
        FLOOR_SP: FLOOR_SP_ALT,
        FLOOR_DECO: FLOOR_DECO_ALT,

        FLAT_BOOKSHELF: FLAT_BOOKSHELF_ALT,
        FLAT_HIGH_GRASS: FLAT_HIGH_GRASS_ALT,
        FLAT_FURROWED_GRASS: FLAT_FURROWED_ALT,

        RAISED_WALL: RAISED_WALL_ALT,
        RAISED_WALL_DECO: RAISED_WALL_DECO_ALT,
        RAISED_WALL_BOOKSHELF: RAISED_WALL_BOOKSHELF_ALT,

        RAISED_HIGH_GRASS: RAISED_HIGH_GRASS_ALT,
        RAISED_FURROWED_GRASS: RAISED_FURROWED_ALT,
        HIGH_GRASS_OVERHANG: HIGH_GRASS_OVERHANG_ALT,
        FURROWED_OVERHANG: FURROWED_OVERHANG_ALT,
    }

    @classmethod
    def is_door_tile(cls, tile: int):
        return tile in cls.door_tiles_list

    @classmethod
    def is_wall_stitchable(cls, tile: int):
        return tile in cls.wall_stitchable_list

    @classmethod
    def compute_wall_overhang_tile(cls, tile: int, right_below: int, below: int, left_below: int) -> int:
        """
        计算应当使用的 WallOverhang 贴图.
        :param tile: 当前位置材质.
        :param right_below: 右下角材质.
        :param below: 下方材质.
        :param left_below: 左下角材质.
        :return: 返回应当使用的贴图索引.
        """
        # 先根据当前位置的材质找到对应的贴图基索引.
        if tile == Terrain.DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG
        elif tile == Terrain.OPEN_DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG_OPEN
        elif tile == Terrain.LOCKED_DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG_LOCKED
        elif tile == Terrain.CRYSTAL_DOOR:
            visual = cls.DOOR_SIDEWAYS_OVERHANG_CRYSTAL
        elif below == Terrain.BOOKSHELF:
            visual = cls.WALL_OVERHANG_WOODEN
        else:
            visual = cls.WALL_OVERHANG

        # 再根据左下和右下的材质计算偏移量.
        if not cls.is_wall_stitchable(right_below):
            visual += 1
        if not cls.is_wall_stitchable(left_below):
            visual += 2

        return visual

    @classmethod
    def compute_internal_wall_tile(cls, tile: int, right: int, right_below: int, below: int, left_below: int, left: int) -> int:
        # 通向先计算基础贴图
        if tile == Terrain.BOOKSHELF or below == Terrain.BOOKSHELF:
            result = cls.WALL_INTERNAL_WOODEN
        else:
            result = cls.WALL_INTERNAL

        # 计算偏移.
        if not cls.is_wall_stitchable(right):
            result += 1
        if not cls.is_wall_stitchable(right_below):
            result += 2
        if not cls.is_wall_stitchable(left_below):
            result += 4
        if not cls.is_wall_stitchable(left):
            result += 8

        return result

    @classmethod
    def compute_raised_wall_tile(cls, tile: int, right: int, below: int, left: int,) -> int:
        # 计算基
        result = 0
        if below == -1 or cls.is_wall_stitchable(below):
            return -1
        elif cls.is_door_tile(below):
            result = cls.RAISED_WALL_DOOR
        elif tile == Terrain.WALL or tile == Terrain.SECRET_DOOR:
            result = cls.RAISED_WALL
        elif tile == Terrain.WALL_DECO:
            result = cls.RAISED_WALL_DECO
        elif tile == Terrain.BOOKSHELF:
            result = cls.RAISED_WALL_BOOKSHELF

        # 计算偏移.
        if not cls.is_wall_stitchable(right):
            result += 1
        if not cls.is_wall_stitchable(left):
            result += 2

        return result

    @classmethod
    def compute_raised_door_tile(cls, tile: int, below: int):
        if cls.is_wall_stitchable(below):
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

    @classmethod
    def compute_raised_tile_from_terrain(cls, gamemap: 'GameMap', pos: Tuple[int, int], tile: int):
        x, y = pos

        # 处理直接与可替换.
        visual = cls.direct_tiles_dict.get(tile, -1)
        if visual != -1:
            return visual if gamemap.random[pos] > 0.5 else cls.common_alt_tiles_dict.get(visual, visual)

        if cls.is_door_tile(tile):
            return cls.compute_raised_door_tile(tile, gamemap.get_tile((x, y-1)))
        elif cls.is_wall_stitchable(tile):
            return cls.compute_raised_wall_tile(tile, gamemap.get_tile((x+1, y)), gamemap.get_tile((x, y+1)), gamemap.get_tile((x-1, y)))
        elif tile == Terrain.SIGN:
            return cls.RAISED_SIGN
        elif tile == Terrain.STATUE:
            return cls.RAISED_STATUE
        elif tile == Terrain.STATUE_SP:
            return cls.RAISED_STATUE_SP
        elif tile == Terrain.ALCHEMY:
            return cls.RAISED_ALCHEMY_POT
        elif tile == Terrain.BARRICADE:
            return cls.RAISED_BARRICADE
        elif tile == Terrain.HIGH_GRASS:
            return tile if gamemap.random[pos] > 0.5 else cls.common_alt_tiles_dict.get(tile, tile)
        elif tile == Terrain.FURROWED_GRASS:
            return tile if gamemap.random[pos] > 0.5 else cls.common_alt_tiles_dict.get(tile, tile)
        else:
            # TODO check
            print(pos)
            return cls.NULL_TILE

    @classmethod
    def compute_raised_tile_from_wall(cls, gamemap: 'GameMap', pos: Tuple[int, int], tile: int):
        x, y = pos
        if cls.is_wall_stitchable(tile):
            if y + 1 < gamemap.height and not cls.is_wall_stitchable(gamemap.get_tile((x, y + 1))):
                tile_ = gamemap.get_tile((x, y+1))
                if tile_ == Terrain.DOOR:
                    return cls.DOOR_SIDEWAYS
                elif tile_ == Terrain.LOCKED_DOOR:
                    return cls.DOOR_SIDEWAYS_LOCKED
                elif tile_ == Terrain.CRYSTAL_DOOR:
                    return cls.DOOR_SIDEWAYS_CRYSTAL
                elif tile_ == Terrain.OPEN_DOOR:
                    return -1
            else:
                # 计算墙内
                return cls.compute_internal_wall_tile(
                    tile, gamemap.get_tile((x+1, y)), gamemap.get_tile((x+1, y+1)), gamemap.get_tile((x, y+1)), gamemap.get_tile((x-1, y+1)), gamemap.get_tile((x-1, y))
                )

        if y + 1 < gamemap.height and cls.is_wall_stitchable(gamemap.get_tile((x, y + 1))):
            return cls.compute_wall_overhang_tile(
                tile, gamemap.get_tile((x+1, y+1)), gamemap.get_tile((x, y+1)), gamemap.get_tile((x-1, y+1)),
            )

        # 计算 wall_overhang
        if y + 1 < gamemap.height and cls.is_wall_stitchable(gamemap.get_tile((x, y + 1))):
            return cls.compute_wall_overhang_tile(
                tile, gamemap.get_tile((x+1, y+1)), gamemap.get_tile((x, y+1)), gamemap.get_tile((x-1, y+1))
            )

        return -1

    def __new__(cls, tileset: 'str' = 'sewers'):
        if cls._instances[tileset] is None:
            cls._instances[tileset] = super().__new__(cls)
        return cls._instances[tileset]

    def __init__(self, tileset: 'str' = 'sewers'):
        self.tileset = self.tiles_dict[tileset]

    def __getitem__(self, tile_code: int) -> 'Surface':
        return self.tileset[tile_code]

    def get_raised_tile_from_terrain(self, gamemap: 'GameMap', pos: Tuple[int, int], tile: int) -> 'Surface':
        raised_tile = self.compute_raised_tile_from_terrain(gamemap, pos, tile)
        return self[raised_tile]

    def get_raised_tile_from_wall(self, gamemap: 'GameMap', pos: Tuple[int, int], tile: int) -> 'Optional[Surface]':
        raised_tile_from_wall = self.compute_raised_tile_from_wall(gamemap, pos, tile)
        if raised_tile_from_wall == -1:
            return None
        return self[raised_tile_from_wall]

    def get_raised_door_tile(self, tile: int, below: int) -> 'Surface':
        raised_door_tile = self.compute_raised_door_tile(tile, below)
        return self[raised_door_tile]

    def get_wall_overhang_tile(self, tile: int, right_below: int, below: int, left_below: int) -> 'Surface':
        wall_overhang_tile = self.compute_wall_overhang_tile(tile, right_below, below, left_below)
        return self[wall_overhang_tile]

    def get_internal_wall_tile(self, tile: int, right: int, right_below: int, below: int, left_below: int, left: int) \
            -> 'Surface':
        internal_wall_tile = self.compute_internal_wall_tile(tile, right, right_below, below, left_below, left)
        return self[internal_wall_tile]

    def get_raised_wall_tile(self, tile: int, right: int, below: int, left: int,) -> 'Surface':
        raised_wall_tile = self.compute_raised_wall_tile(tile, right, below, left)
        return self[raised_wall_tile]
