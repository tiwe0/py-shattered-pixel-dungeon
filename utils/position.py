from typing import Tuple
class Position:
    @classmethod
    def linear(cls, origin_pos: Tuple[int, int], target_pos: Tuple[int, int], frac: 'float') -> Tuple[int, int]:
        o_x, o_y = origin_pos
        t_x, t_y = target_pos
        return o_x+(t_x-o_x)*frac, o_y+(t_y-o_y)*frac