import pygame as pg

from component import Component

from animator import Animator


class Sprite:

    def __init__(self, game_object, size):
        self.game_object = game_object
        self.width, self.height = size
        self.looking_left = True
        self.rect = self.image.get_rect()

    def _load_images(self, sprite_sheet_path):
        # Loads Idle Images Sequence
        self.idle_images = self._load_images_set(sprite_sheet_path + "/idle.png")
        # Loads Moving Images Sequence
        self.moving_images = self._load_images_set(sprite_sheet_path + "/moving.png")

    def _load_images_set(self, path):
        images = []
        try:
            sprite_sheet = pg.image.load(path)
            images_number = sprite_sheet.get_rect().width // self.width
            for i in range(images_number):
                images.append(sprite_sheet.subsurface(i * self.width, 0, self.width, self.height))
        except:
            print(f"Image is not found ({path})")
        return images

    def draw(self, surface):
        if self.looking_left:
            surface.blit(self.image, self.rect)
        else:
            flipped_image = pg.trasform.flip(self.image, True, False)
            surface.blit(flipped_image, self.rect)
