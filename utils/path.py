from collections import namedtuple, deque
from typing import List, Any, Set
from dungeon.gamemap import GameMap

Position = namedtuple("Position", ["x", "y"])
Position.__add__ = lambda self, other: Position(x=self.x+other.x, y=self.y+other.y)


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
        positions = [pos+direction for direction in cls.directions_pos]
        return [position for position in positions if gamemap.walkable[position]]

    @classmethod
    def path_walkable_direction(cls, gamemap: 'GameMap', pos: 'Position'):
        return [d for d in cls.directions_pos if gamemap.walkable[d+pos]]

    @classmethod
    def path_to(cls, fov: 'Set[Position]', start: 'Position', end: 'Position', strict_mode: bool = False) -> list[tuple[Any, Any, int, int]]:
        if strict_mode:
            path = cls._path_to_strict_mode(fov=fov, start=start, end=end)
        else:
            path = cls._path_to_unstrict_mode(fov=fov, start=start, end=end)
        return path

    @classmethod
    def _path_to_strict_mode(cls, fov: 'Set[Position]', start: 'Position', end: 'Position'):
        return cls._path_to_with_directions(fov=fov, start=start, end=end, directions=cls.directions_pos_strict)

    @classmethod
    def _path_to_unstrict_mode(cls, fov: 'Set[Position]', start: 'Position', end: 'Position'):
        return cls._path_to_with_directions(fov=fov, start=start, end=end, directions=cls.directions_pos)

    @classmethod
    def _path_to_with_directions(cls, fov: 'Set[Position]', start: 'Position', end: 'Position', directions: 'List[Position]'):
        q = deque([start])
        track = {start: None}

        while len(q) != 0:
            current = q.pop()

            if current == end:
                break

            for next_pos in [current+d for d in directions]:
                if next_pos in fov and next_pos not in track.keys():
                    q.append(next_pos)
                    track[next_pos] = current

        if end not in track.keys():
            return None

        result = []
        back = end
        while back != start:
            result.append(back)
            back = track[back]
        return reversed(result)

