from dungeon.map import Map

test_map = Map(3, 4, 0)
print(test_map)

test_map.init_from_lst([
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
])

print(test_map)

print(test_map[2, 3])