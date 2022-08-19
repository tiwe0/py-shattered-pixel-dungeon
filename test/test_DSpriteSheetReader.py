from dungeon.dsprite import DSpriteSheetReader
import pygame
from test.test_stage import test_stage
from dungeon.assets import DAssets

frame_width = 15
frame_height = 15

test_dspritesheetreader = DSpriteSheetReader(DAssets.Sprites.bat, frame_width, frame_height)


def test_func(screen):
    x = 0
    for sur in test_dspritesheetreader:
        screen.blit(sur, (x, x))
        x += 16


test_stage(test_func)
