import numpy as np

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
