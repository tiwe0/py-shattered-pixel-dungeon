from io import StringIO
from typing import List, Optional, Tuple

from pygame import Surface

from dungeon import pre_screen
from dungeon.fonts import ark_font
from utils.typing import Position
from utils.surface import get_scaled_surface_by_factor_with_cut, get_scaled_surface_by_factor
from utils.ninepatch import NinePatch


class Component:
    def __init__(self, *, scale: int = 1, pos: 'Position' = Position(0, 0), activate: 'bool' = True):
        self.children: 'List[TileComponent]' = []
        self.parent: 'Optional[TileComponent]' = None
        self.scale_factor = scale
        self.pos = pos

        self.local_surface = Surface((pre_screen.get_width(), pre_screen.get_height())).convert_alpha()
        self.clear_local()

        self.activate = activate

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
        self.render_self()
        if self.activate:
            for child in self.children:
                child.render_all()
            self.update_parent(self.scale(self.local_surface))

    def before_render(self):
        pass

    def render_self(self):
        """默认的before trigger."""
        rendered = self.render()
        self.local_surface.blit(rendered, (0, 0))

    def render(self):
        """默认的render函数."""
        return self.local_surface

    def scale(self, rendered: 'Surface') -> Surface:
        # TODO 这个方法可能会有性能问题
        if self.scale_factor == 1:
            return rendered
        return get_scaled_surface_by_factor(rendered, self.scale_factor)

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


class TileComponent(Component):
    """TODO Render 总体逻辑没问题, 但是细节有点问题, 架构需要调整一下."""
    def __init__(self, tile: 'Optional[Surface]' = None, **kwargs):
        super(TileComponent, self).__init__(**kwargs)
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
    def tile(self):
        return self._tile

    @tile.setter
    def tile(self, value: Surface):
        """更新 tile 时, 会同时更新 local_surface."""
        self._tile = value
        self.local_surface = value.copy()

    def render(self):
        """默认的render函数."""
        if self.tile:
            return self.tile
        return self.local_surface


class NinePatchComponent(Component):
    def __init__(self, ninepatch: 'NinePatch', width: 'float', height: 'float', activate: 'bool', **kwargs):
        super(NinePatchComponent, self).__init__(**kwargs)
        self.ninepatch: 'NinePatch' = ninepatch
        self.width = width
        self.height = height
        self.activate = activate

    def render(self):
        return self.ninepatch.get_surface(middle_width=self.width, middle_height=self.height)


class TextComponent(TileComponent):
    # 半角字符 7, 全角字符 12, 空格 5, 高度为 12.
    length_dict = {
        'half': 6,
        'full': 12,
    }

    half_word = "abdcefghijklmnopqrstuvwxyz" \
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                " -_.()/\\<>0123456789"

    def __init__(self, message: 'str', width: 'Optional[int]' = None, **kwargs):
        super(TextComponent, self).__init__(**kwargs)
        self.message = message
        if width:
            self.width = width
            self.tile = self.generate_tile()
        else:
            self.tile = ark_font.render(message, False, kwargs.get('color', (255, 255, 255))).convert_alpha()
            self.width = self.tile.get_width()

    def generate_tile(self) -> 'Surface':
        """根据message生成相应的贴图."""
        split_message = []

        def split_rec(message_left):
            current_length = 0
            for index in range(len(message_left)):
                if message_left[index] in self.half_word:
                    current_length += 6
                else:
                    current_length += 12
                if current_length > self.width:
                    split_message.append(message_left[:index])
                    split_rec(message_left[index:])
                    break
                if index == len(message_left) - 1:
                    split_message.append(message_left[:index])

        split_rec(self.message)
        message_tile = Surface((self.width, len(split_message) * 13 - 1)).convert_alpha()
        y = 0
        for message_index in range(len(split_message)):
            font_surface = ark_font.render(split_message[message_index], False, (255, 255, 255))
            message_tile.blit(font_surface, (0, y))
            y += 13
        return message_tile

    @property
    def height(self):
        return self.tile.get_height()


class TextContainerComponent(TileComponent):
    def __init__(self, width: int, height: int, **kwargs):
        super(TextContainerComponent, self).__init__(**kwargs)
        self.width, self.height = width, height
        self.message_history: List[TextComponent] = []

    def render_self(self):
        x, y = 0, 0
        self.children = []
        for message in self.message_history[-5:]:
            message.pos = (x, y)
            y += (message.height + 1)
            self.add_child(message)

    def log(self, *args, **kwargs):
        with StringIO() as output:
            print(*args, file=output, **kwargs)
            message = output.getvalue()
        self.message_history.append(TextComponent(message, self.width))

