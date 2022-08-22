from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from dungeon.entity import Entity
    from dungeon.input_handler import MainEventHandler
    from dungeon.game_map import GameMap


class Engine:
    """负责集中管理、调度 事件处理器、动画渲染、地图、玩家等资源."""
    def __init__(
            self,
            player: 'Entity',
            input_handler: 'Type',
            gamemap: 'GameMap'
    ):
        """

        :param player: 玩家控制的实体.
        :param input_handler: 输入处理器.
        :param gamemap: 对应地图.
        """
        self.player: 'Entity' = player

        # 这里 input_handler 是个类, 因此初始化不太一样.
        self.input_handler: 'Type' = input_handler
        self.input_handler.player = player

        # 这里 gamemap 是个实例, 因此初始化不太一样.
        self.gamemap: 'GameMap' = gamemap
        self.gamemap.engine = self

    def handle_event(self):
        """事件处理委托给事件处理器."""
        self.input_handler.handle_event()

    def render(self):
        """渲染地图."""
        self.gamemap.render()
        # 渲染 UI
        # self.UI.render()

    def run(self):
        """引擎核心方法, 处理事件 + 渲染."""
        self.handle_event()
        self.render()
