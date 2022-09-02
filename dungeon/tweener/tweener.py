from typing import Tuple, TYPE_CHECKING

from pygame.time import Clock

from utils.position import Position

if TYPE_CHECKING:
    from dungeon.dsprite import DSprite


class Tweener:
    def __init__(self, time_interval: float):
        self.time_interval = time_interval
        self.time = 0.0
        self._clock = Clock()
        self._clock.tick()

    @property
    def elapsed(self) -> 'float':
        tick = self._clock.tick()
        return tick

    @property
    def percentage(self) -> 'float':
        frac = float(self.time) / float(self.time_interval)
        return 1 if frac >= 1 else frac

    def reset(self):
        self.time = 0.0

    def activate(self):
        self.time += self.elapsed
        self.activate_interval()
        if self.percentage == 1:
            self.activate_post()

    def activate_interval(self):
        pass

    def activate_post(self):
        pass


class PosTweener(Tweener):
    def __init__(self, sprite: 'DSprite', target_pos: 'Tuple[int, int]', time_interval: 'float'):
        super(PosTweener, self).__init__(time_interval)
        self.sprite = sprite
        self.origin_pos = sprite.xy
        self.target_pos = target_pos

    def activate_interval(self):
        pos = Position.linear(self.origin_pos, self.target_pos, self.percentage)
        self.sprite.x, self.sprite.y = pos

    def activate_post(self):
        self.sprite.pos_tweeners.remove(self)
        self.sprite.status = 'idle'
        self.sprite.entity.time_manager.is_busy = False


class BounceTweener(PosTweener):
    def activate_interval(self):
        pos = Position.bounce(self.origin_pos, self.target_pos, self.percentage)
        self.sprite.x, self.sprite.y = pos
