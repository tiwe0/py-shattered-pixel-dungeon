from typing import List, Optional, Tuple

from pygame import Surface

from dungeon import pre_screen
from utils.surface import get_scaled_surface_by_factor_with_cut


class TileComponent:
    def __init__(self, *, scale: int = 1, tile: 'Optional[Surface]' = None, pos: 'Tuple[int, int]' = (0, 0)):
        self.children: 'List[TileComponent]' = []
        self.parent: 'Optional[TileComponent]' = None
        self.scale_factor = scale
        self.pos = pos

        # 初始化代码,
        # tile = None -> local_surface = new_surface()
        # tile = something -> local_surface = tile.copy()
        self._tile = tile
        if tile:
            self.local_surface = tile.copy()
        else:
            self.local_surface = Surface((pre_screen.get_width(), pre_screen.get_height())).convert_alpha()
            self.clear_local()

    @property
    def parent_surface(self) -> 'Surface':
        """
        根节点的父节点为 pre_screen.
        子节点的父节点为父节点的local_surface.
        :return:
        """
        if self.is_root():
            return pre_screen
        else:
            return self.parent.local_surface

    @property
    def tile(self):
        return self._tile

    @tile.setter
    def tile(self, value: Surface):
        """更新 tile 时, 会同时更新 local_surface."""
        self._tile = value
        self.local_surface = value.copy()

    def is_root(self) -> bool:
        return self.parent is None

    def clear_local(self):
        """清空当前组件的local_surface."""
        self.local_surface.fill((0, 0, 0, 0))

    def render_all(self):
        """
        1. 清空 render tree 的所有 local_surface, 并做预处理.
        2. 由底向上一次渲染.
        -> 1. 获取 render 函数的 surface.
        -> 2. 作一次 scale, 然后更新到父节点的 local_surface 上.
        :return:
        """
        self.clear_local()
        self.before_render()
        for child in self.children:
            child.render_all()
        rendered = self.render()
        self.update_parent(self.scale(rendered))

    def before_render(self):
        """默认的before trigger."""
        if self.tile:
            self.local_surface.blit(self.tile, (0, 0))

    def render(self):
        """默认的render函数."""
        return self.local_surface

    def scale(self, rendered: 'Surface') -> Surface:
        # TODO 这个方法可能会有性能问题
        if self.scale_factor == 1:
            return rendered
        return get_scaled_surface_by_factor_with_cut(rendered, self.scale_factor)

    def update_parent(self, update: 'Surface'):
        """将update更新到父组件上."""
        if update:
            self.parent_surface.blit(update, self.pos)

    def add_child(self, component: 'TileComponent'):
        """添加渲染子组件.
        这个方法支持链式调用."""
        self.children.append(component)
        component.parent = self
        return self
