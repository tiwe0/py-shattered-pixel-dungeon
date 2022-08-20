from dungeon.assets import Assets
from dungeon.dsprite import DSpriteSheetReader
from dungeon.dsprite import DAnimation, DSprite
from dungeon.entity import Entity
from test.test_stage import test_stage

rogue_dsprite_sheet_reader = DSpriteSheetReader(Assets.Sprites.rogue, frame_width=12, frame_height=15)

rogue_idle_animation = DAnimation(
    status='idle',
    frames=rogue_dsprite_sheet_reader,
    fps=1,
    key_frame=[0, 1, 0, 0],
    loop=True
)

rogue_run_animation = DAnimation(
    status='run',
    frames=rogue_dsprite_sheet_reader,
    fps=10,
    key_frame=[2, 3, 4, 5, 6, 7],
    loop=True
)

rogue_sprite = DSprite()
rogue_sprite.add_animation(rogue_idle_animation)
rogue_sprite.add_animation(rogue_run_animation)

rogue = Entity(x=0, y=0, sprite=rogue_sprite)
rogue.status = "run"
rogue.move(direction=(1, 1))


def test_func(screen):
    rogue.render()


test_stage(test_func)

