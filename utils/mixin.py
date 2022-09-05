import pygame

from dungeon import GRID_SIZE
from utils.typing import Position


class MixInRenderable:
    def render(self):
        pass


class MixInTimer:
    def __init__(self):
        self._timer: 'pygame.time.Clock' = pygame.time.Clock()
        self._timer.tick()

    @property
    def elapsed(self) -> 'float':
        return self._timer.tick()


class MixInXY:
    def __init__(self, x=0, y=0, width=0, height=0, offset_gird: 'Position' = Position(x=GRID_SIZE, y=GRID_SIZE)):
        self.x, self.y = x, y
        self.pos_x, self.pos_y = GRID_SIZE * x, GRID_SIZE * y
        self.width = width
        self.height = height
        self.offset_grid = offset_gird

    @property
    def xy(self) -> 'Position':
        return Position(x=self.x, y=self.y)

    @property
    def pos(self) -> 'Position':
        return GRID_SIZE * self.xy

    @property
    def offset(self) -> 'Position':
        grid_width, grid_height = self.offset_grid
        offset_x = (grid_width - self.width) // 2
        offset_y = grid_height - self.height - 1
        return Position(x=offset_x, y=offset_y)

    @property
    def pos_offset(self) -> 'Position':
        return self.pos+self.offset


class MixInAct:
    def __init__(self):
        self.current_action = None

    def override_action(self):
        action_name = self.current_action.__class__.__name__.lower()
        return f'exec_{action_name}' in self.__dir__()

    def update_fov(self):
        pass

    def act(self) -> 'bool':
        if self.current_action is None:
            return False
        if self.override_action():
            action_name = self.current_action.__class__.__name__.lower()
            override_method = getattr(self, f'exec_{action_name}')
            override_method(self)
        else:
            self.current_action.exec(self)
        self.update_fov()
        self.current_action = None

