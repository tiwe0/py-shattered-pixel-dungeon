from utils.ninepatch import NinePatch
from utils.tile_load import load_tile
from utils.typing import Position


tile_scroll = load_tile("assets/interfaces/chrome.png", (32, 32), (32, 32))
ninepatch_scroll = NinePatch(
    lt_1=Position(0, 0), lt_2=Position(5, 11),
    rt_1=Position(27, 0), rt_2=Position(32, 11),
    ld_1=Position(0, 22), ld_2=Position(5, 32),
    rd_1=Position(27, 22), rd_2=Position(32, 32),
    tile=tile_scroll,
)

tile_frame = load_tile("assets/interfaces/chrome.png", (0, 0), (20, 20))
ninepatch_frame = NinePatch(
    lt_1=Position(0, 0), lt_2=Position(5, 5),
    rt_1=Position(15, 0), rt_2=Position(20, 5),
    ld_1=Position(0, 15), ld_2=Position(5, 20),
    rd_1=Position(15, 15), rd_2=Position(20, 20),
    tile=tile_frame,
)

tile_frame_silver = load_tile("assets/interfaces/chrome.png", (86, 0), (22, 22))
ninepatch_frame_silver = NinePatch(
    lt_1=Position(0, 0), lt_2=Position(6, 6),
    rt_1=Position(16, 0), rt_2=Position(22, 6),
    ld_1=Position(0, 16), ld_2=Position(6, 22),
    rd_1=Position(16, 16), rd_2=Position(22, 22),
    tile=tile_frame_silver
)

