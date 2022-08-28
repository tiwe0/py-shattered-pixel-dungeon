from typing import List, Optional, Tuple

from pygame import Surface

from dungeon import screen, pre_screen
from utils.surface import get_scaled_surface_by_factor_with_cut, get_scaled_surface_by_factor


class TileComponent:
    def __init__(self, *, scale: int = 1, tile: 'Optional[Surface]' = None, pos: 'Tuple[int, int]' = (0, 0)):
        self.children: 'List[TileComponent]' = []
        self.parent: 'Optional[TileComponent]' = None
        if tile:
            self.local_surface = tile
        else:
            self.local_surface = Surface((pre_screen.get_width(), pre_screen.get_height())).convert_alpha()
            self.clear_local()
        self.scale_factor = scale
        self.pos = pos

    def is_root(self) -> bool:
        return self.parent is None

    def clear_local(self):
        self.local_surface.fill((0, 0, 0, 0))

    @property
    def parent_surface(self):
        if self.is_root():
            return pre_screen
        else:
            return self.parent.local_surface

    def render_all(self):
        if self.is_root():
            self.clear_local()
        for child in self.children:
            child.render_all()
        rendered = self.render()
        self.update_parent(self.scale(rendered))

    def render(self):
        return self.local_surface

    def scale(self, rendered: 'Surface') -> Surface:
        # 这个方法可能会有性能问题
        if self.scale_factor == 1:
            return rendered
        return get_scaled_surface_by_factor_with_cut(rendered, self.scale_factor)

    def update_parent(self, update: 'Surface'):
        print(self.__class__.__name__)
        if update:
            self.parent_surface.blit(update, self.pos)

    def add_child(self, component: 'TileComponent'):
        self.children.append(component)
        component.parent = self
        return self
