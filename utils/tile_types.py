import numpy as np

tile_dtype = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("tile_id", np.int),
    ]
)
