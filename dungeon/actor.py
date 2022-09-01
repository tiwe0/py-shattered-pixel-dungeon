import heapq
from typing import TYPE_CHECKING, Optional, Tuple, Set, List

from dungeon.entity import Entity
from dungeon.ai import AIWonder, AIAttack
from dungeon.components.message_manager import MessageManager
from utils.compute_fov import FOV
from test.debug import DebugRender

if TYPE_CHECKING:
    from dungeon.components.HUD import HealthBar
    from dungeon.action import Action
    from dungeon.ai import AI, AIForDebug
    from dungeon.gamemap import Position


class Actor(Entity):

    def __init__(self, hp: int, mp: int, san: int, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.current_action: 'Optional[Action]' = None
        self.max_hp, self.max_mp, self.max_san = hp, mp, san
        self._hp, self._mp, self._san = hp, mp, san
        self.health_bar: 'Optional[HealthBar]' = None
        self.ai: 'Optional[AI]' = AIWonder()
        self.fov: 'Optional[FOV]' = None
        self.fov_set: 'Optional[Set[Tuple[int, int]]]' = None
        self.radius: int = 7
        self.path_to_walk: 'List[Position]' = []
        self.buffs = []

    def update_fov(self):
        self.fov_set = self.fov.compute_fov(self.xy, self.radius)

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
        self.update_fov()
        self.current_action = None
        for buff in self.buffs:
            buff.act(self)

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
                # debug
                MessageManager.instance.log(f"current action: {self.ai.__class__.__name__}")

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

    def die(self):
        self.status = 'die'
        # self.sprite.die()

    def render(self):
        super(Actor, self).render()
