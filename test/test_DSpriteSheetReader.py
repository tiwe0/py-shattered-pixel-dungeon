from dungeon.assets import Assets
from dungeon.dsprite import DSpriteSheetReader
from test.test_stage import test_stage

frame_width = 15
frame_height = 15

test_dspritesheetreader = DSpriteSheetReader(Assets.Sprites.bat, frame_width, frame_height)


def test_func(screen):
    x = 0
    for sur in test_dspritesheetreader:
        screen.blit_middle(sur, (x, x))
        x += 16


test_stage(test_func)
