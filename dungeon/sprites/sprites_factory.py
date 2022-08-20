from typing import TYPE_CHECKING, List, Dict
from dungeon.dsprite import DSpriteSheetReader, DSprite, DAnimation
from dungeon.assets import Assets
import json


class SpriteManager:
    def __init__(self, filepath):
        sprites = load_sprites_from_json(filepath)
        self._sprites_dict = {}
        for sprite in sprites:
            self._sprites_dict[sprite.name] = sprite

    def __getitem__(self, item):
        return self._sprites_dict.get(item, None)

    def sprites(self):
        return list(self._sprites_dict.keys())


def load_sprites_from_json(filepath: str):
    with open(filepath, mode="rt") as f:
        sprites_info = json.load(f)
    for sprite_info in sprites_info:
        try:
            sprite_cls = getattr(Assets, sprite_info['sprite'].split('.')[1])
            sprite_path = getattr(sprite_cls, sprite_info['sprite'].split('.')[-1])
            sprite = gen_sprites(
                filepath=sprite_path,
                width=int(sprite_info['width']),
                height=int(sprite_info['height']),
                animations=sprite_info['animations'],
                name=sprite_info['file']
            )
        except Exception as e:
            print(f"error while loading {sprite_info}, skip it.")
            print(f"{e}")
            print("-"*100)
            continue
        yield sprite


def gen_sprites(filepath: str, width: int, height: int, animations: List[Dict], name: str=''):
    sprite = DSprite(name=name)
    sprite_sheet = DSpriteSheetReader(
        filename=filepath,
        frame_width=int(width),
        frame_height=int(height),
    )
    for animation_info in animations:
        sprite.add_animation(DAnimation(
            status=animation_info['name'],
            fps=int(animation_info['fps']),
            loop=animation_info['loop'],
            key_frame=animation_info['frames'],
            frames=sprite_sheet,
        ))
    return sprite
