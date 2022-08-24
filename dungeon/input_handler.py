import sys
from typing import TYPE_CHECKING, Optional

import pygame.event
from pygame.event import Event
from pygame.locals import *

from dungeon.action import Action, MovementAction, WaitAction, EscapeAction

if TYPE_CHECKING:
    from dungeon.actor import Actor


class EventHandler:
    """事件处理器基类."""

    def dispatch_event(self, event: 'Event') -> 'Optional[Action]':
        """事件分发. `Event` -> `Action` """
        raise NotImplementedError()


# TODO 后续用单例模式重写, 并将按键映射抽象出来
class MainEventHandler(EventHandler):
    key_map = {
        # VI Movement
        K_y: MovementAction(direction=(-1, -1)),
        K_u: MovementAction(direction=(+1, -1)),
        K_h: MovementAction(direction=(-1, 0)),
        K_j: MovementAction(direction=(0, +1)),
        K_k: MovementAction(direction=(0, -1)),
        K_l: MovementAction(direction=(+1, 0)),
        K_b: MovementAction(direction=(-1, +1)),
        K_n: MovementAction(direction=(+1, +1)),
        K_PERIOD: WaitAction(),

        # number Movement
        K_7: MovementAction(direction=(-1, -1)),
        K_9: MovementAction(direction=(+1, -1)),
        K_4: MovementAction(direction=(-1, 0)),
        K_2: MovementAction(direction=(0, +1)),
        K_8: MovementAction(direction=(0, -1)),
        K_6: MovementAction(direction=(+1, 0)),
        K_1: MovementAction(direction=(-1, +1)),
        K_3: MovementAction(direction=(+1, +1)),
        K_5: WaitAction(),

        K_ESCAPE: EscapeAction(),
    }

    def __init__(self):
        self.current_action_for_player: 'Optional[Action]' = None
        """主事件处理器."""
        self.player: 'Optional[Actor]' = None

    def set_action(self, action: 'Action'):
        self.current_action_for_player = action

    def consume_action(self):
        self.player.current_action = self.current_action_for_player
        self.current_action_for_player = None

    def dispatch_event(self, event: 'Event'):
        # if self.player.gamemap.engine.time_manager.is_busy:
        #     return None
        # 如果移动动画还没结束, 则屏蔽输入.
        if self.player.sprite.is_moving:
            return None
        # 点击 关闭 按钮.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # 按键按下, 返回按键对应的动作.
        if event.type == KEYDOWN:
            action = self.key_map.get(event.key)
            return action

    def handle_event(self):
        """处理事件."""
        for event in pygame.event.get():
            action = self.dispatch_event(event)
            if action:
                self.set_action(action)
