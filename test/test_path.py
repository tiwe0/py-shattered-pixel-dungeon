from utils.path import Path
from utils.path import Position


test_case = [
    (1, 1), (1, 2), (1, 3), (2, 3), (3, 4), (3, 5),
    (4, 3), (5, 3)
]

test_case = [Position(x, y) for x, y in test_case]

print([p for p in Path.path_to(fov=test_case, start=Position(1, 1), end=Position(5, 3), strict_mode=False)])
