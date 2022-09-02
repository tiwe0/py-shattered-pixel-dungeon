from typing import Tuple


class Position:
    @classmethod
    def linear(cls, origin_pos: Tuple[int, int], target_pos: Tuple[int, int], percentage: 'float') -> Tuple[float, float]:
        o_x, o_y = origin_pos
        t_x, t_y = target_pos
        return o_x + (t_x - o_x) * percentage, o_y + (t_y - o_y) * percentage

    @classmethod
    def bounce(cls, origin_pos: Tuple[int, int], target_pos: Tuple[int, int], percentage: 'float') -> Tuple[float, float]:
        if percentage <= 0.5:
            return cls.linear(origin_pos=origin_pos, target_pos=target_pos, percentage=2*percentage)
        else:
            return cls.linear(origin_pos=target_pos, target_pos=origin_pos, percentage=2*percentage-1.0)
