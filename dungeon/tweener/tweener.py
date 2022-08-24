from typing import Tuple, TYPE_CHECKING

from pygame.time import Clock

from utils.position import Position

if TYPE_CHECKING:
    from dungeon.dsprite import DSprite


class Tweener:
    pass


class PosTweener(Tweener):
    def __init__(self, sprite: 'DSprite', target_pos: 'Tuple[int, int]', time_interval: 'float'):
        super(PosTweener, self).__init__()
        self.sprite = sprite
        self.origin_pos = sprite.pos
        self.target_pos = target_pos
        self.time_interval = time_interval
        self.time = 0.0
        self._clock = Clock()
        self._clock.tick()

    @property
    def elapsed(self):
        tick = self._clock.tick()
        return tick

    def activate(self):
        self.time += self.elapsed
        if self.time >= self.time_interval:
            frac = 1
        else:
            frac = float(self.time) / float(self.time_interval)
        pos = Position.linear(self.origin_pos, self.target_pos, frac)
        self.sprite.x, self.sprite.y = pos
        if frac == 1:
            self.sprite.pos_tweener = None
            self.sprite.status = 'idle'
