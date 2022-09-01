from typing import List, Any, Set, TYPE_CHECKING, Iterator
from utils.typing import Position
import heapq

if TYPE_CHECKING:
    from utils.compute_fov import FOV

# AI *


class PathFinder:
    directions = [
        (+0, -1), (-1, +0), (+1, +0), (+0, +1),
        (+1, -1), (-1, -1), (-1, +1), (+1, +1),
    ]

    directions_pos = [Position(x=x, y=y) for x, y in directions]

    directions_strict = [
        (+0, -1), (+0, +1), (-1, +0), (+1, +0),
    ]

    directions_pos_strict = [Position(x=x, y=y) for x, y in directions_strict]

    weight = 1

    gamemap = None

    @classmethod
    def path_walkable(cls, pos: 'Position') -> list[tuple[Any, Any, int, int]]:
        """寻找周围8格中可走格子."""
        positions = [pos + direction for direction in cls.directions_pos]
        return [position for position in positions if cls.gamemap.walkable[position]]

    @classmethod
    def path_walkable_direction(cls, pos: 'Position'):
        """寻找周围8格中可走方向."""
        return [d for d in cls.directions_pos if cls.gamemap.walkable[d + pos]]

    @classmethod
    def neighbor_general(cls, pos: 'Position', directions: 'List[Position]') -> 'Iterator[Position]':
        for d in directions:
            next_position = d + pos
            if next_position in cls.gamemap:
                yield d + pos

    @classmethod
    def neighbor(cls, pos: 'Position') -> 'Iterator[Position]':
        yield from cls.neighbor_general(pos=pos, directions=cls.directions_pos)

    @classmethod
    def neighbor_strict(cls, pos: 'Position') -> 'Iterator[Position]':
        yield from cls.neighbor_general(pos=pos, directions=cls.directions_pos_strict)

    @classmethod
    def heuristic(cls, a: 'Position', b: 'Position') -> int:
        x1, y1 = a
        x2, y2 = b
        return abs(x1 - x2) + abs(y1 - y2)

    @classmethod
    def a_star_general(cls, start: 'Position', end: 'Position', direction: 'List[Position]'):
        q = [(0, start)]
        heapq.heapify(q)
        came_from = {
            start: None,
        }
        cost_so_far = {
            start: 0,
        }

        while len(q) != 0:
            _, current = heapq.heappop(q)

            if current == end:
                break

            for _next in cls.neighbor_general(current, direction):
                new_cost = cost_so_far[current] + cls.gamemap.weight[_next]
                if _next not in cost_so_far.keys() or new_cost < cost_so_far[_next]:
                    cost_so_far[_next] = new_cost
                    priority = new_cost + cls.heuristic(_next, end)
                    heapq.heappush(q, (priority, _next))
                    came_from[_next] = current

        return came_from, cost_so_far

    @classmethod
    def a_star(cls, start: 'Position', end: 'Position', strict_mode: 'bool'):
        if strict_mode:
            direction = cls.directions_pos_strict
        else:
            direction = cls.directions_pos
        return cls.a_star_general(start=start, end=end, direction=direction)

    @classmethod
    def reconstruct_path(cls, path_dict, start, end):
        current = end
        path = []
        while current != start:
            path.append(current)
            current = path_dict[current]
        # path.append(start)
        return reversed(path)

    @classmethod
    def path_to(cls, start: 'Position', end: 'Position') -> Iterator[Position]:
        came_from, _ = cls.a_star(start, end, False)
        return cls.reconstruct_path(came_from, start, end)
