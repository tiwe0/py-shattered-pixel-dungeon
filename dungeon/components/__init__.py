from typing import List, Optional

from pygame import Surface

from dungeon import screen, pre_screen
from utils.surface import get_scaled_surface_by_factor_


class Component:
    def __init__(self, *, scale: int = 1):
        self.children: 'List[Component]' = []
        self.parent: 'Optional[Component]' = None
        self.pre_surface = Surface((pre_screen.get_width(), pre_screen.get_height())).convert_alpha()
        self.scale_factor = scale
        pass

    @property
    def is_root(self) -> bool:
        return self.parent is None

    @property
    def parent_surface(self) -> 'Surface':
        if self.is_root:
            return pre_screen
        else:
            return self.parent.pre_surface

    def render_all(self):
        self.clear_pre_surface()
        self.render()
        for child in self.children:
            child.render_all()
        self.scale()
        self.parent_surface.blit(self.pre_surface, (0, 0))

    def scale(self):
        if self.scale_factor == 1:
            return
        self.pre_surface = get_scaled_surface_by_factor_(self.pre_surface, self.scale_factor)

    def clear_pre_surface(self):
        self.pre_surface.fill((0, 0, 0, 0))

    def render(self):
        """要渲染到self.pre_surface上."""
        pass

    def set_scale(self, scale: int):
        self.scale_factor = scale
        return self

    def add_child(self, component: 'Component'):
        self.children.append(component)
        component.parent = self
        return self
