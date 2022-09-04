from typing import Any, Optional

import pygame.event
from pygame.event import Event
from pygame.locals import *

from dungeon.action import *

if TYPE_CHECKING:
    from dungeon.actor import Actor


class EventHandler:
    """事件处理器基类."""
    key_map = {}
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.current_action = None

    def dispatch_event(self, event: 'Event') -> 'Optional[Action]':
        """事件分发. `Event` -> `Action` """
        if event.type == KEYDOWN:
            action = self.key_map.get(event.key)
            return action

    def handle_event(self):
        """处理事件."""
        for event in pygame.event.get():
            action = self.dispatch_event(event)
            if action:
                self.current_action = action


# TODO 后续用单例模式重写, 并将按键映射抽象出来
class MainEventHandler(EventHandler):
    key_map = {
        # VI Movement
        K_y: ActorActionHeadTo(direction=(-1, -1)),
        K_u: ActorActionHeadTo(direction=(+1, -1)),
        K_h: ActorActionHeadTo(direction=(-1, 0)),
        K_j: ActorActionHeadTo(direction=(0, +1)),
        K_k: ActorActionHeadTo(direction=(0, -1)),
        K_l: ActorActionHeadTo(direction=(+1, 0)),
        K_b: ActorActionHeadTo(direction=(-1, +1)),
        K_n: ActorActionHeadTo(direction=(+1, +1)),
        K_PERIOD: ActorActionWait(),
        K_i: InventoryActionToggle(),

        # number Punch
        K_7: ActorActionHeadTo(direction=(-1, -1)),
        K_9: ActorActionHeadTo(direction=(+1, -1)),
        K_4: ActorActionHeadTo(direction=(-1, 0)),
        K_2: ActorActionHeadTo(direction=(0, +1)),
        K_8: ActorActionHeadTo(direction=(0, -1)),
        K_6: ActorActionHeadTo(direction=(+1, 0)),
        K_1: ActorActionHeadTo(direction=(-1, +1)),
        K_3: ActorActionHeadTo(direction=(+1, +1)),
        K_5: ActorActionWait(),

        K_ESCAPE: SystemActionEscape(),
    }

    def __init__(self):
        self.current_action: 'Optional[Action]' = None
        """主事件处理器."""
        self.player: 'Optional[Actor]' = None

    def dispatch_event(self, event: 'Event') -> 'Optional[Action]':
        if self.player.gamemap.engine.time_manager.is_busy:
            return None
        # 如果移动动画还没结束, 则屏蔽输入.
        if self.player.sprite.is_moving:
            return None
        # 点击 关闭 按钮.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # 按键按下, 返回按键对应的动作.
        return super(MainEventHandler, self).dispatch_event(event)


class InventoryEventHandler(EventHandler):
    key_map = {
        # 上一页, 下一页
        K_h: InventoryActionShiftPage(),
        K_l: InventoryActionShiftPage(),

        # 上一条，下一条
        K_j: InventoryActionShiftItem(),
        K_k: InventoryActionShiftItem(),

        # 下一个类目
        K_TAB: InventoryActionShiftCate(),

        # 选择当前 item
        K_SPACE: InventoryActionSelect(),

        # 切换模式
        K_i: InventoryActionToggle(),
    }

