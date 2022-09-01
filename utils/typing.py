import numpy as np
from collections import namedtuple

map_tile_type = np.dtype(
    [
        ('tiles', np.int),
        ('weight', np.float),
        ('random', np.int),
        ('walkable', np.bool_),
        ('explored', np.bool_),
        ('visiting', np.bool_),
    ]
)

Position = namedtuple("Position", ["x", "y"])
Position.__add__ = lambda self, other: Position(x=self.x + other.x, y=self.y + other.y)
Position.__sub__ = lambda self, other: Position(x=self.x - other.x, y=self.y - other.y)


