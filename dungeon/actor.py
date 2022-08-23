from dungeon.entity import Entity
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from dungeon.components.HUD import HealthBar


class Actor(Entity):
    def __init__(self, hp: int, mp: int, san: int, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.max_hp, self.max_mp, self.max_san = hp, mp, san
        self._hp, self._mp, self._san = hp, mp, san
        self.health_bar: 'Optional[HealthBar]' = None

    def update_health_bar(self):
        if self.health_bar:
            self.health_bar.update_health_bar(self.hp//self.max_hp)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        value = max(value, 0)
        value = min(value, self.max_hp)
        self._hp = value
        if self._hp == 0:
            # die
            pass
        if self.is_player():
            pass
        # trigger to render hp bar


    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        value = max(value, 0)
        value = min(value, self.max_mp)
        self._mp = value
        # trigger to
        if self.is_player():
            pass
        # trigger to render hp bar

    @property
    def san(self):
        return self._san

    @san.setter
    def san(self, value):
        value = max(value, 0)
        value = min(value, self.max_san)
        self._san = value
        if self._san == 0:
            # die
            pass
        if self.is_player():
            pass
        # trigger to render san bar

