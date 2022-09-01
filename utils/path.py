from collections import namedtuple, deque
from typing import List, Any, Set, TYPE_CHECKING, Iterator
from dungeon.gamemap import GameMap
import heapq

if TYPE_CHECKING:
    from utils.compute_fov import FOV

Position = namedtuple("Position", ["x", "y"])
Position.__add__ = lambda self, other: Position(x=self.x + other.x, y=self.y + other.y)


class Path:
    directions = [
        (+1, -1), (-1, -1), (-1, +1), (+1, +1),
        (+0, -1), (-1, +0), (+1, +0), (+0, +1),
    ]

    directions_pos = [Position(x=x, y=y) for x, y in directions]

    directions_strict = [
        (+0, -1), (+0, +1), (-1, +0), (+1, +0),
    ]

    directions_pos_strict = [Position(x=x, y=y) for x, y in directions_strict]

    @classmethod
    def path_walkable(cls, gamemap: 'GameMap', pos: 'Position') -> list[tuple[Any, Any, int, int]]:
        """寻找周围8格中可走格子."""
        positions = [pos + direction for direction in cls.directions_pos]
        return [position for position in positions if gamemap.walkable[position]]

    @classmethod
    def path_walkable_direction(cls, gamemap: 'GameMap', pos: 'Position'):
        """寻找周围8格中可走方向."""
        return [d for d in cls.directions_pos if gamemap.walkable[d + pos]]

    @classmethod
    def path_to(cls, fov: 'FOV', start: 'Position', end: 'Position', strict_mode: bool = False) -> list[
        tuple[Any, Any, int, int]]:
        """寻路算法."""
        if strict_mode:
            path = cls._path_to_strict_mode(fov=fov, start=start, end=end)
        else:
            path = cls._path_to_unstrict_mode(fov=fov, start=start, end=end)
        if path:
            return path
        else:
            return []

    @classmethod
    def _path_to_strict_mode(cls, fov: 'FOV', start: 'Position', end: 'Position'):
        return cls._path_to_with_directions(fov=fov, start=start, end=end, directions=cls.directions_pos_strict)

    @classmethod
    def _path_to_unstrict_mode(cls, fov: 'FOV', start: 'Position', end: 'Position'):
        return cls._path_to_with_directions(fov=fov, start=start, end=end, directions=cls.directions_pos)

    @classmethod
    def _path_to_with_directions(cls, fov: 'FOV', start: 'Position', end: 'Position', directions: 'List[Position]'):
        fov_set = fov.to_set()
        q = deque([start])
        visited = []
        track = {start: None}

        while len(q) != 0:
            current = q.popleft()

            if current == end:
                break

            for next_pos in [current + d for d in directions]:
                if next_pos in fov_set and next_pos not in visited and not fov.is_blocking(next_pos):
                    q.append(next_pos)
                    track[next_pos] = current
            visited.append(current)

        if end not in track.keys():
            return None

        result = []
        back = end
        while back != start:
            result.append(back)
            back = track[back]
        return reversed(result)


# AI *

class PathAIStar:
    directions = [
        (+1, -1), (-1, -1), (-1, +1), (+1, +1),
        (+0, -1), (-1, +0), (+1, +0), (+0, +1),
    ]

    directions_pos = [Position(x=x, y=y) for x, y in directions]

    directions_strict = [
        (+0, -1), (+0, +1), (-1, +0), (+1, +0),
    ]

    directions_pos_strict = [Position(x=x, y=y) for x, y in directions_strict]

    weight = 1

    gamemap = None

    @classmethod
    def neighbor(cls, pos: 'Position') -> 'Iterator[Position]':
        for d in cls.directions_pos:
            next_position = d + pos
            if next_position in cls.gamemap:
                yield d + pos

    @classmethod
    def neighbor_strict(cls, pos: 'Position') -> 'Iterator[Position]':
        for d in cls.directions_pos_strict:
            next_position = d + pos
            if next_position in cls.gamemap:
                yield d + pos

    @classmethod
    def heuristic(cls, a: 'Position', b: 'Position') -> int:
        x1, y1 = a
        x2, y2 = b
        return abs(x1 - x2) + abs(y1 - y2)

    @classmethod
    def a_star(cls, start: 'Position', end: 'Position'):
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

            for _next in cls.neighbor(current):
                new_cost = cost_so_far[current] + cls.gamemap.weight[_next]
                if _next not in cost_so_far.keys() or new_cost < cost_so_far[_next]:
                    cost_so_far[_next] = new_cost
                    priority = new_cost + cls.heuristic(_next, end)
                    heapq.heappush(q, (priority, _next))
                    came_from[_next] = current

        return came_from, cost_so_far

    @classmethod
    def reconstruct_path(cls, path_dict, start, end):
        current = end
        path = []
        while current != start:
            path.append(current)
            current = path_dict[current]
        path.append(start)
        return reversed(path)
