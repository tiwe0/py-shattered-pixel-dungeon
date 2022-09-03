from dungeon.components import TextComponent, TextContainerComponent


class MessageLog(TextComponent):
    pass


class MessageManager(TextContainerComponent):
    instance: 'MessageManager' = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
