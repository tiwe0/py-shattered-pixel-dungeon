from typing import TYPE_CHECKING, Optional, Tuple, Set

from dungeon.entity import Entity
from dungeon.ai import AIWonder

if TYPE_CHECKING:
    from dungeon.components.HUD import HealthBar
    from dungeon.action import Action
    from dungeon.ai import AI, AIForDebug


class Actor(Entity):
    def __init__(self, hp: int, mp: int, san: int, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.current_action: 'Optional[Action]' = None
        self.max_hp, self.max_mp, self.max_san = hp, mp, san
        self._hp, self._mp, self._san = hp, mp, san
        self.health_bar: 'Optional[HealthBar]' = None
        self.ai: 'Optional[AI]' = AIWonder()
        self.fov: 'Set[Tuple[int, int]]' = set()

    def update_health_bar(self):
        if self.health_bar:
            self.health_bar.update_health_bar(self.hp // self.max_hp)

    def update_fov(self):
        pass

    def override_action(self):
        action_name = self.current_action.__class__.__name__.lower()
        return f'exec_{action_name}' in self.__dir__()

    def act(self):
        if self.current_action is None:
            return
        # check action is override or not.
        if self.override_action():
            action_name = self.current_action.__class__.__name__.lower()
            override_method = getattr(self, f'exec_{action_name}')
            override_method(self)
        else:
            self.current_action.exec(self)
        self.current_action = None

    def fetch_action(self):
        # must override for NPC, mobs...
        # maybe fetch action from its AI, set it to current_action
        # waiting to be executed.
        if self.is_player():
            # 这个实现不咋好
            self.engine.input_handler.consume_action()
        else:
            if self.ai:
                self.current_action = self.ai.fetch_action(self)

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

    def set_hp(self, value):
        self._hp = value

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
