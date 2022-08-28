from typing import List, TYPE_CHECKING
from dungeon.components import TileComponent
from dungeon.fonts import ipix_font


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
        self.tile = ipix_font.render(message, True, (255, 255, 255))


class MessageManager(TileComponent):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, width: int, height: int, **kwargs):
        super(MessageManager, self).__init__(**kwargs)
        self.width, self.height = width, height
        self.message_history: List[MessageLog] = []

    def before_render(self):
        x, y = 0, 0
        self.children = []
        for message in self.message_history[-5:]:
            message.pos = (x, y)
            y += 13
            self.add_child(message)

    def log(self, message: 'str'):
        self.message_history.append(MessageLog(message, self.width))

