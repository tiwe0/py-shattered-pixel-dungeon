import pygame
from pygame import Surface, Rect

from utils.typing import Position
from utils.surface import get_scaled_surface


class NinePatch:
    def __init__(self,
                 lt_1: 'Position', lt_2: 'Position',
                 rt_1: 'Position', rt_2: 'Position',
                 ld_1: 'Position', ld_2: 'Position',
                 rd_1: 'Position', rd_2: 'Position',
                 tile: 'Surface'
                 ):
        rect_lt = Rect(lt_1.x, lt_1.y, lt_2.x-lt_1.x, lt_2.y-lt_1.y)
        rect_mt = Rect(lt_2.x, rt_1.y, rt_1.x-lt_2.x, lt_2.y-rt_1.y)
        rect_rt = Rect(rt_1.x, rt_1.y, rt_2.x-rt_1.x, rt_2.y-rt_1.y)
        rect_ml = Rect(ld_1.x, lt_2.y, lt_2.x-ld_1.x, ld_1.y-lt_2.y)
        rect_mi = Rect(lt_2.x, lt_2.y, rd_1.x-lt_2.x, rd_1.y-lt_2.y)
        rect_mr = Rect(rd_1.x, rt_2.y, rt_2.x-rd_1.x, rd_1.y-rt_2.y)
        rect_ld = Rect(ld_1.x, ld_1.y, ld_2.x-ld_1.x, ld_2.y-ld_1.y)
        rect_md = Rect(ld_2.x, rd_1.y, rd_1.x-ld_2.x, ld_2.y-rd_1.y)
        rect_rd = Rect(rd_1.x, rd_1.y, rd_2.x-rd_1.x, rd_2.y-rd_1.y)
        self.tile = tile
        self.lt = tile.subsurface(rect_lt).copy().convert_alpha()
        self.mt = tile.subsurface(rect_mt).copy().convert_alpha()
        self.rt = tile.subsurface(rect_rt).copy().convert_alpha()
        self.ml = tile.subsurface(rect_ml).copy().convert_alpha()
        self.mi = tile.subsurface(rect_mi).copy().convert_alpha()
        self.mr = tile.subsurface(rect_mr).copy().convert_alpha()
        self.ld = tile.subsurface(rect_ld).copy().convert_alpha()
        self.md = tile.subsurface(rect_md).copy().convert_alpha()
        self.rd = tile.subsurface(rect_rd).copy().convert_alpha()

    def get_surface(self, middle_width: float, middle_height: float) -> 'Surface':
        surface = Surface(
            (self.lt.get_width()+middle_width+self.rt.get_width(),
             self.lt.get_height()+middle_height+self.ld.get_height(),)
        ).convert_alpha()
        surface.fill((0, 0, 0, 0))

        surface_mt = get_scaled_surface(self.mt, (middle_width, self.lt.get_height()))
        surface_ml = get_scaled_surface(self.ml, (self.lt.get_width(), middle_height))
        surface_mi = get_scaled_surface(self.mi, (middle_width, middle_height))
        surface_mr = get_scaled_surface(self.mr, (self.rt.get_width(), middle_height))
        surface_md = get_scaled_surface(self.md, (middle_width, self.ld.get_height()))

        surface.blits(blit_sequence=[
            (self.lt, (0, 0)),
            (surface_mt, (self.lt.get_width(), 0)),
            (self.rt, (self.lt.get_width()+middle_width, 0)),
            (surface_ml, (0, self.lt.get_height())),
            (surface_mi, (self.lt.get_width(), self.lt.get_height())),
            (surface_mr, (self.lt.get_width()+middle_width, self.lt.get_height())),
            (self.ld, (0, self.lt.get_height()+middle_height)),
            (surface_md, (self.lt.get_width(), self.lt.get_height()+middle_height)),
            (self.rd, (self.lt.get_width()+middle_width, self.lt.get_height()+middle_height)),
        ])
        return surface.convert_alpha()



