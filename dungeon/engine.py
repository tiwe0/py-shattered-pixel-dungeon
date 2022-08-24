from typing import TYPE_CHECKING

from dungeon.time_manager import TimeManager

if TYPE_CHECKING:
    from dungeon.input_handler import MainEventHandler
    from dungeon.entity import Entity
    from dungeon.game_map import GameMap


class Engine:
    """负责集中管理、调度 事件处理器、动画渲染、地图、玩家等资源."""

    def __init__(
            self,
            player: 'Entity',
            input_handler: 'MainEventHandler',
            gamemap: 'GameMap',
            time_manager: 'TimeManager',
    ):
        """

        :param player: 玩家控制的实体.
        :param input_handler: 输入处理器.
        :param gamemap: 对应地图.
        """
        self.player: 'Entity' = player
        self.player.engine = self

        # 这里 input_handler 是个类, 因此初始化不太一样.
        self.input_handler: 'MainEventHandler' = input_handler
        self.input_handler.player = player

        # 这里 gamemap 是个实例, 因此初始化不太一样.
        self.gamemap: 'GameMap' = gamemap
        self.gamemap.engine = self

        self.time_manager: 'TimeManager' = time_manager
        self.time_manager.engine = self

    def handle_event(self):
        """事件处理委托给事件处理器."""
        self.input_handler.handle_event()

    def render(self):
        """渲染地图."""
        self.gamemap.render()
        # 渲染 UI
        # self.UI.render()

    def push_time(self):
        self.time_manager.run()

    def run(self):
        """引擎核心方法, 处理事件 + 渲染."""
        self.handle_event()
        self.push_time()
        self.render()
