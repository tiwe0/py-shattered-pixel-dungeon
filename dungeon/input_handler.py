import sys
from typing import TYPE_CHECKING, Optional


import pygame.event
from dungeon.action import Action, MovementAction, WaitAction, EscapeAction
from pygame.event import Event
from pygame.locals import *

if TYPE_CHECKING:
    from entity import Entity


class EventHandler:
    """事件处理器基类."""

    @classmethod
    def dispatch_event(cls, event: 'Event') -> 'Optional[Action]':
        """事件分发. `Event` -> `Action` """
        raise NotImplementedError()


class MainEventHandler(EventHandler):
    """主事件处理器."""
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
    player: 'Entity'

    @classmethod
    def dispatch_event(cls, event: 'Event'):
        # 如果移动动画还没结束, 则屏蔽输入.
        if cls.player.sprite.is_moving:
            return None
        # 按键按下, 返回按键对应的动作.
        if event.type == KEYDOWN:
            action = cls.key_map.get(event.key)
            return action
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    @classmethod
    def execute_action(cls, action: 'Action'):
        # 将action作用在player上.
        action.exec(cls.player)

    @classmethod
    def handle_event(cls):
        """处理事件."""
        for event in pygame.event.get():
            action = cls.dispatch_event(event)
            if action:
                cls.execute_action(action)
