from typing import List
from dungeon.components import TileComponent
from dungeon.fonts import ipix_font
from pygame import Surface
from dungeon import pre_screen


class MessageLog(TileComponent):
    # 半角字符 7, 全角字符 12, 空格 5, 高度为 12.
    length_dict = {
        'half': 7,
        'full': 12,
        'space': 5,
    }

    def __init__(self, message: 'str', width: 'int', **kwargs):
        super(MessageLog, self).__init__(**kwargs)
        self.message = message
        self.local_surface = ipix_font.render(message, False, (255, 255, 255))


class MessageManager(TileComponent):
    def __init__(self, width: int, height: int, **kwargs):
        super(MessageManager, self).__init__(**kwargs)
        self.width, self.height = width, height
        self.message_history: List[MessageLog] = []

    def render(self):
        x, y = 0, 0
        self.clear_children()
        for message in self.message_history[-5:]:
            message.pos = (x, y)
            y += 13
            self.add_child(message)
        return self.local_surface

    def log(self, message: 'str'):
        self.message_history.append(MessageLog(message, self.width))

