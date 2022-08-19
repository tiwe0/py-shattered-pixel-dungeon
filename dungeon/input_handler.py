from typing import Mapping, TYPE_CHECKING

import pygame.event

from dungeon.action import Action, Movement, Wait
from pygame.event import Event
from pygame.locals import *

if TYPE_CHECKING:
    from entity import Entity


class EventHandler:

    @classmethod
    def dispatch_event(cls, event: 'Event'):
        raise NotImplementedError()


class MainEventHandler(EventHandler):
    key_map = {
        # VI Movement
        K_y: Movement(direction=(-1, -1)),
        K_u: Movement(direction=(+1, -1)),
        K_h: Movement(direction=(-1, 0)),
        K_j: Movement(direction=(0, +1)),
        K_k: Movement(direction=(0, -1)),
        K_l: Movement(direction=(+1, 0)),
        K_b: Movement(direction=(-1, +1)),
        K_n: Movement(direction=(+1, +1)),
        K_PERIOD: Wait(),
        K_ESCAPE: Action,
    }
    entity: 'Entity'

    @classmethod
    def dispatch_event(cls, event: 'Event'):
        if cls.entity.sprite.is_moving:
            return None
        if event.type == KEYDOWN:
            action = cls.key_map.get(event.key)
            return action

    @classmethod
    def execute_action(cls, action: 'Action'):
        action.exec(cls.entity)

    @classmethod
    def handle_event(cls):
        for event in pygame.event.get():
            action = cls.dispatch_event(event)
            if action:
                cls.execute_action(action)
