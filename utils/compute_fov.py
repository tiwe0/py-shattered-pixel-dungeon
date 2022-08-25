import math
from fractions import Fraction
from typing import Tuple, TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from dungeon.gamemap.__init__ import GameMap


def round_ties_up(n):
    return math.floor(n + 0.5)


def round_ties_down(n):
    return math.ceil(n - 0.5)


def slope(tile: Tuple[int, int]):
    row_depth, col = tile
    return Fraction(2 * col - 1, 2 * row_depth)


def is_symmetric(row: 'Row', tile: 'Tuple[int, int]'):
    row_depth, col = tile
    return (
            row.depth * row.start_slope <= col <= row.depth * row.end_slope
    )


class Quadrant:
    north = 0
    east = 1
    south = 2
    west = 3

    def __init__(self, cardinal: int, origin: Tuple[int, int]):
        self.cardinal = cardinal
        self.ox, self.oy = origin

    def transform(self, tile: Tuple[int, int]) -> Tuple[int, int]:
        row, col = tile
        if self.cardinal == self.north:
            return self.ox + col, self.oy - row
        if self.cardinal == self.south:
            return self.ox + col, self.oy + row
        if self.cardinal == self.east:
            return self.ox + row, self.oy - col
        if self.cardinal == self.west:
            return self.ox - row, self.oy + col


class Row:

    def __init__(self, depth: int, start_slope: Fraction, end_slope: Fraction):
        self.depth = depth
        self.start_slope = start_slope
        self.end_slope = end_slope

    def tiles(self):
        min_col = round_ties_up(self.depth * self.start_slope)
        max_col = round_ties_down(self.depth * self.end_slope)
        for col in range(min_col, max_col + 1):
            yield self.depth, col

    def next(self):
        return Row(
            self.depth + 1,
            self.start_slope,
            self.end_slope,
        )


def compute_fov(origin: Tuple[int, int], radius: int, gamemap: 'GameMap'):

    new_fov = np.full((gamemap.width, gamemap.height), fill_value=False, order='F')

    mark_visible(new_fov, origin)

    for i in range(4):
        quadrant = Quadrant(i, origin)

        def reveal(tile: Tuple[int, int]):
            x, y = quadrant.transform(tile)
            mark_visible(new_fov, (x, y))

        def is_wall(tile: Tuple[int, int]):
            if tile is None:
                return False
            x, y = quadrant.transform(tile)
            return is_blocking(gamemap.walkable, (x, y))

        def is_floor(tile: Tuple[int, int]):
            if tile is None:
                return False
            x, y = quadrant.transform(tile)
            return not is_blocking(gamemap.walkable, (x, y))

        def scan(row: Row, current_radius: int):
            try:
                if current_radius >= radius:
                    return
                prev_tile = None
                for tile in row.tiles():
                    if is_wall(tile) or is_symmetric(row, tile):
                        reveal(tile)
                    if is_wall(prev_tile) and is_floor(tile):
                        row.start_slope = slope(tile)
                    if is_floor(prev_tile) and is_wall(tile):
                        new_row = row.next()
                        new_row.end_slope = slope(tile)
                        scan(new_row, current_radius+1)
                    prev_tile = tile
                if is_floor(prev_tile):
                    scan(row.next(), current_radius+1)
            except Exception:
                return

        first_row = Row(1, Fraction(-1), Fraction(1))
        scan(first_row, 0)
    return new_fov


def is_blocking(gamemap: 'GameMap', pos: Tuple[int, int]):
    return not gamemap[pos]


def mark_visible(gamemap: 'GameMap', pos: Tuple[int, int]):
    gamemap[pos] = True
