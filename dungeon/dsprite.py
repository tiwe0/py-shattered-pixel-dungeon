from typing import List, TYPE_CHECKING, Mapping, Optional, Tuple
import pygame
from pygame.sprite import Sprite
from dungeon.tweener.tweener import PosTweener

if TYPE_CHECKING:
    from entity import Entity


class DSprite(Sprite):
    """Sprite class for dungeon."""
    def __init__(self):
        super().__init__()
        self._entity = None
        self.x = 0
        self.y = 0
        self.animation: 'Mapping[str, DAnimation]' = {}
        self.pos_tweener: 'Optional[PosTweener]' = None
        self.direction = 'right'
        self.status = 'idle'

    @property
    def is_moving(self):
        if self.pos_tweener is None:
            return False
        else:
            return True

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, value: 'Entity'):
        self._entity = value
        self.x = value.x * 16
        self.y = value.y * 16

    @property
    def current_animation(self):
        return self[self.status]

    @property
    def pos(self):
        return self.x, self.y

    def __getitem__(self, item: str):
        return self.animation.get(item, None)

    def before_render(self):
        if self.pos_tweener:
            self.pos_tweener.activate()

    def render(self):
        # trigger before
        self.before_render()
        self.current_animation.render()

    def add_animation(self, animation: 'DAnimation'):
        self.animation[animation.status] = animation
        animation.sprite = self

    def move(self, direction: 'Tuple[int, int]'):
        self.status = 'run'
        target_pos = self.x+16*direction[0], self.y+16*direction[1]
        self.pos_tweener = PosTweener(self, target_pos, 200)
        if direction[0] > 0:
            self.direction = 'right'
        elif direction[0] < 0:
            self.direction = 'left'


class DAnimation:
    def __init__(self, status: str, frames: 'List[pygame.Surface]', fps: 'int', key_frame: 'List[int]', loop: 'bool'):
        self.status = status
        self.loop = loop
        self.frames = frames
        self.key_frame = key_frame
        self.delay = float(1.0/fps) * 1000
        self.sprite: 'Optional[DSprite]' = None
        self.time: 'float' = 0.0
        self._timer: 'pygame.time.Clock' = pygame.time.Clock()
        self._timer.tick()
        self._current_index = 0

    @property
    def elapsed(self):
        return self._timer.tick()

    @property
    def direction(self):
        return self.sprite.direction

    @property
    def current_index(self):
        return self._current_index

    @current_index.setter
    def current_index(self, value):
        if self.loop:
            self._current_index = value % len(self.key_frame)
        else:
            self._current_index = min(value, len(self.key_frame)-1)

    def update_index(self):
        self.time += self.elapsed
        if self.time > self.delay:
            self.time -= self.delay
            self.current_index += 1

    def get_current_frame(self):
        self.update_index()
        current_key = self.key_frame[self.current_index]
        return self.frames[current_key] if self.direction == 'right' else pygame.transform.flip(self.frames[current_key], True, False)

    def render(self) -> None:
        current_frame = self.get_current_frame()
        screen = pygame.display.get_surface()
        screen.blit(current_frame, self.sprite.pos)


class DSpriteSheetReader:
    def __init__(self, filename: 'str', frame_width: 'int', frame_height: 'int', row: 'int' = 1, col: 'int' = -1):
        self.surface_sheet = DSpriteSheetReader.read_sheet(
            filename=filename,
            frame_width=frame_width,
            frame_height=frame_height,
            row=row,
            col=col,
        )

    @classmethod
    def read_sheet(
            cls,
            filename: 'str',
            frame_width: 'int',
            frame_height: 'int',
            row: 'int' = 1,
            col: 'int' = -1
    ) -> 'List[pygame.Surface]':
        surface_total = pygame.image.load(filename)
        # 确保图片能整除
        # assert (surface_total.get_width() % frame_width) == 0
        # assert (surface_total.get_height() % frame_height) == 0

        if col == -1:
            col = int(surface_total.get_width() // frame_width)

        surface_sheet: 'List[pygame.Surface]' = []
        rect = pygame.Rect(0, 0, frame_width, frame_height)

        for r in range(row):
            for c in range(col):
                surface_sheet.append(surface_total.subsurface(rect).copy())
                rect.move_ip(frame_width, 0)
            rect.move_ip(-frame_width*col, frame_height)

        return surface_sheet

    def __getitem__(self, item: 'int') -> 'pygame.Surface':
        return self.surface_sheet[item]

    def __iter__(self):
        return iter(self.surface_sheet)
