import random
from typing import Tuple, Iterator


def vline(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    x = start[0]
    y_min = min(start[1], end[1])
    y_max = max(start[1], end[1])
    for y in range(y_min, y_max + 1):
        yield x, y


def hline(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    y = start[1]
    x_min = min(start[0], end[0])
    x_max = max(start[0], end[0])
    for x in range(x_min, x_max + 1):
        yield x, y


def line(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:
        corner = tuple([x1, y2])
        yield from vline(start, corner)
        yield from hline(corner, end)
    else:
        corner = tuple([x2, y1])
        yield from hline(start, corner)
        yield from vline(corner, end)
