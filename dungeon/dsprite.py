import copy
from typing import List, TYPE_CHECKING, Dict, Optional, Tuple

import pygame
from pygame.sprite import Sprite

from dungeon import pre_screen_middle
from dungeon.config import GRID_SIZE
from utils.typing import Position
from dungeon.tweener.tweener import PosTweener

if TYPE_CHECKING:
    from entity import Entity


class DAnimation:
    """负责动画渲染，绝大多数的动画最终均由该类负责渲染."""

    def __init__(self, status: str, frames: 'DSpriteSheetReader', fps: 'int', key_frame: 'List[int]', loop: 'bool'):
        """

        :param status: 动画名. DSprite 通常拥有若干 DAnimation实例, 这个参数帮助 DSprite 选择应当渲染的 DAnimation.
        :param frames: 该动画对应的 SpriteSheet. 这里已经加载为 `Surface` 列表. 该列表通常是全局唯一的, 不应当被复制.
        该列表也不应当知晓该动画.
        :param fps: 帧数.
        :param key_frame: 组成动画的关键帧索引, 该索引与 `frames` 对应.
        :param loop: 该动画是否循环播放.
        """
        self.status = status
        self.loop = loop
        self.frames = frames
        self.key_frame = key_frame
        self.delay = float(1.0 / fps) * 1000 if fps != 0 else 1000.0  # 由帧数计算而来, 控制动画速度.
        self.time: 'float' = 0.0
        # 对 `elapsed` 属性负责.
        self._timer: 'pygame.time.Clock' = pygame.time.Clock()
        self._timer.tick()
        # 当前帧索引, 对 `current_index` 负责, 主要用于决定当前渲染的动画.
        self._current_index = 0

    def __repr__(self):
        return f"DAnimation '{self.status}'"

    @property
    def elapsed(self):
        """流逝的时间量."""
        return self._timer.tick()

    @property
    def current_index(self):
        """当前帧索引."""
        return self._current_index

    @current_index.setter
    def current_index(self, value):
        """防止越界, 同时处理 loop 逻辑."""
        if self.loop:
            self._current_index = value % len(self.key_frame)
        else:
            self._current_index = min(value, len(self.key_frame) - 1)

    def update_index(self):
        """根据累积时间更新当前index."""
        self.time += self.elapsed
        if self.time > self.delay:
            self.time -= self.delay
            self.current_index += 1

    def get_current_frame(self, direction: str) -> pygame.Surface:
        """获取当前帧对应的图片, 并根据 `direction` 作相应的变换.

        :param direction: 表示方向的字符串, 'left' or 'right'.
        :return: 根据 index 与 direction 返回 Surface.
        """
        self.update_index()
        current_key = self.key_frame[self.current_index]
        return self.frames[current_key] if direction == 'right' \
            else pygame.transform.flip(self.frames[current_key], True, False)

    def render(self, sprite: 'DSprite') -> None:
        """ 核心渲染方法.
        渲染的思路都很一致, 先获取 screen, 再将 需要渲染的 Surface 直接渲染上去.
        该方法不对缩放负责.

        :param sprite: 主要用于判断方向.
        :return:
        """
        current_frame = self.get_current_frame(sprite.direction)
        pre_screen_middle.blit(current_frame, sprite.pos)


class DSprite(Sprite):
    """Sprite 类, 主要负责追踪 `Entity` 实例 并管理对应的 `DAnimation`."""

    def __init__(self, name: str = '', width: int = GRID_SIZE, height: int = GRID_SIZE,
                 offset_grid: 'Tuple[int, int]' = (GRID_SIZE, GRID_SIZE)):
        """初始化函数.

        :param name: 名称, 主要用于加载与调试.
        :param width: 宽度.
        :param height: 高度.
        :param offset_grid: 偏移, 负责将 DSprite 微调, 默认为 x 微调到中心, y 微调到靠底部上移 1 px.
        """
        super().__init__()  # 这里貌似没有用到父类, 后续考虑删除.
        self.x, self.y = 0, 0
        self.name = name
        self.width = width
        self.height = height
        self.direction = 'right'
        self.status = 'idle'  # 用于找到正确的动画.
        self.offset: 'Position' = self.compute_offset(offset_grid)

        # 所有动画保存在字典中. 注意, 所有同类 DSprite 公用同一组动画.
        self.animation: 'Dict[str, DAnimation]' = {}
        # 位置调分器, 用于处理移动.
        self.pos_tweeners: 'List[PosTweener]' = []
        self.die_tweener: 'Optional[DieTweener]' = None

        self._entity = None

    def __repr__(self):
        return f"DSprite '{self.name}' -> {self.entity}"

    def compute_offset(self, offset_grid: Tuple[int, int]) -> 'Position':
        """计算偏移量."""
        grid_width, grid_height = offset_grid
        offset_x, offset_y = (grid_width - self.width) // 2, (grid_height - self.height - 1)
        return Position(x=offset_x, y=offset_y)

    def clone(self):
        """DSprite 会在游戏开始时批量加载, 但每个 Entity实例 都应该由对应的 DSprite 实例, 因此这里实现一个 clone 方法.
        但该方法可能有问题, 因为所有的 DSprite 公用同一组 DAnimation.
        (貌似问题不大)."""
        clone = copy.copy(self)
        return clone

    @property
    def is_moving(self):
        """根据位置调分器判断该Sprite是否在移动.
        移动就必定有位置调分器, 反之亦然, 这是等价条件."""
        if not self.pos_tweeners:
            return False
        else:
            return True

    @property
    def entity(self):
        """主要是为了setter方法."""
        return self._entity

    @entity.setter
    def entity(self, value: 'Entity'):
        """设置 entity 时, 自动更新对应的渲染位置."""
        self._entity = value
        self.update_pos()

    @property
    def current_animation(self):
        # 获取当前动画
        return self[self.status]

    @property
    def pos(self):
        """返回偏移后的位置."""
        return Position(x=self.x + self.offset[0], y=self.y + self.offset[1])

    def update_pos(self):
        """手动更新位置."""
        self.x, self.y = GRID_SIZE * self.entity.x, GRID_SIZE * self.entity.y

    def __getitem__(self, item: str):
        return self.animation.get(item, None)

    @property
    def xy(self):
        return Position(x=self.x, y=self.y)

    def before_render(self):
        """render 前的钩子函数."""
        # 激活 位置调分器, 以更新位置.
        if self.pos_tweeners:
            for pos_tweener in self.pos_tweeners:
                pos_tweener.activate()

    def render(self):
        """渲染函数, 主要负责调用钩子调整属性, 然后将渲染委托给 DAnimation."""
        self.before_render()
        self.current_animation.render(sprite=self)  # 动画不知道 DSprite 的存在, 因此需要当成参数传入.

    def add_animation(self, animation: 'DAnimation'):
        """添加动画, 注意, 动画不应当知晓 DSprite 的存在, 否则 clone 方法会出问题."""
        self.animation[animation.status] = animation

    def move(self, direction: 'Tuple[int, int]'):
        """移动."""
        self.status = 'run'  # 切换到 run 动画.
        self.entity.time_manager.is_busy = True
        target_pos = self.x + GRID_SIZE * direction[0], self.y + GRID_SIZE * direction[1]  # 计算目标位置.
        # 生成 位置调分器. 移动结束后, 该调分器负责将 该 DSprite 状态切换为 'idle'.
        self.pos_tweeners.append(PosTweener(self, target_pos, 200))
        # 更新自己的方向.
        if direction[0] > 0:
            self.direction = 'right'
        elif direction[0] < 0:
            self.direction = 'left'


class DSpriteSheetReader:
    """SpriteSheet读取器, 主要负责动画的读取, 因为这些图片大小和间隔往往都固定.
    对于不规则的Sprite读取, 使用 load_image."""

    def __init__(self, filename: 'str', frame_width: 'int', frame_height: 'int', row: 'int' = -1, col: 'int' = -1):
        """

        :param filename: 文件路径.
        :param frame_width: 每个方框的宽度.
        :param frame_height: 每个方向的高度.
        :param row: 行数. -1 表示根据 `frame_height` 自动计算.
        :param col: 列数. -1 表示根据 `frame_width` 自动计算.
        """
        self.surface_sheet = DSpriteSheetReader.read_sheet(
            filename=filename,
            frame_width=frame_width,
            frame_height=frame_height,
            row=row,
            col=col,
        )
        self.filename = filename
        self.frame_width = frame_width
        self.frame_height = frame_height

    def __repr__(self):
        return f"<DSpriteSheetReader {self.filename}| frame: [width: {self.frame_width}, height: {self.frame_height}]>"

    @classmethod
    def read_sheet(
            cls,
            filename: 'str',
            frame_width: 'int',
            frame_height: 'int',
            row: 'int' = 1,
            col: 'int' = -1
    ) -> 'List[pygame.Surface]':
        """ 实际的实现.

        :param filename: 文件路径.
        :param frame_width: 每个方框的宽度.
        :param frame_height: 每个方向的高度.
        :param row: 行数. -1 表示根据 `frame_height` 自动计算.
        :param col: 列数. -1 表示根据 `frame_width` 自动计算.
        """
        surface_total = pygame.image.load(filename)

        # 尝试使用 convert_alpha 提高渲染性能.
        try:
            surface_total.convert_alpha()
        except Exception as e:
            print("warning: not convert.")

        if col == -1:
            col = int(surface_total.get_width() // frame_width)

        if row == -1:
            row = int(surface_total.get_height() // frame_height)

        surface_sheet: 'List[pygame.Surface]' = []
        rect = pygame.Rect(0, 0, frame_width, frame_height)

        for r in range(row):
            for c in range(col):
                surface_sheet.append(surface_total.subsurface(rect).copy().convert_alpha())
                rect.move_ip(frame_width, 0)
            rect.move_ip(-frame_width * col, frame_height)

        return surface_sheet

    def __getitem__(self, item: 'int') -> 'pygame.Surface':
        item = int(item)
        return self.surface_sheet[item]

    def __iter__(self):
        return iter(self.surface_sheet)
