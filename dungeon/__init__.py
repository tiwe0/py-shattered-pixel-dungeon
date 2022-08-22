from dungeon.sprites.sprites_factory import load_sprites_from_json, SpriteManager
import pygame
if not pygame.get_init():
    pygame.init()

pygame.init()
sprites_manager = SpriteManager("./meta/info.json")
