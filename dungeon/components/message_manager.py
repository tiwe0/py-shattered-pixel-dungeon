from io import StringIO
from typing import List

from pygame import Surface

from dungeon.components import TileComponent
from dungeon.fonts import ark_font


class MessageLog(TileComponent):
    # 半角字符 7, 全角字符 12, 空格 5, 高度为 12.
    length_dict = {
        'half': 6,
        'full': 12,
    }

    half_word = "abdcefghijklmnopqrstuvwxyz" \
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                " -_.()/\\<>0123456789"

    def __init__(self, message: 'str', width: 'int', **kwargs):
        super(MessageLog, self).__init__(**kwargs)
        self.message = message
        self.width = width
        self.tile = self.generate_tile()

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


class MessageManager(TileComponent):
    instance: 'MessageManager' = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, width: int, height: int, **kwargs):
        super(MessageManager, self).__init__(**kwargs)
        self.width, self.height = width, height
        self.message_history: List[MessageLog] = []

    def before_render(self):
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
        self.message_history.append(MessageLog(message, self.width))
