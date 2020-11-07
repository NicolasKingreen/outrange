import math
import pygame as pg

from animator import Animator
from entity import Entity

class Player(Entity):

    def __init__(self, game_instance):

        super().__init__(game_instance, "player")

        self.rect = pg.Rect(self.game_instance.settings.screen_center, (64, 104))
        self._load_images_from_sprite_sheet("data/images/ranger.png")
        self.animator = Animator(self, self.images)
        self.rect.center = self.game_instance.settings.screen_center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.movement_direction = [0, 0]
        self.speed = 0.3
        self.hp = 36

        self._prep_name_label()

    def update(self, dt):

        self.name_rect.center = self.rect.centerx, self.rect.y - 16

        # print(f"Direction: ({self.movement_direction[0]}, {self.movement_direction[1]}); Location: ({self.rect.x}, {self.rect.y})\r", end="")

        if self.movement_direction[0] or self.movement_direction[1]:
            vector_size = math.sqrt(self.movement_direction[0] ** 2 + self.movement_direction[1] ** 2)
            normalized_movement_direction = self.movement_direction.copy()
            normalized_movement_direction[0] /= vector_size
            normalized_movement_direction[1] /= vector_size
            self.x += normalized_movement_direction[0] * self.speed * dt / 1
            self.y += normalized_movement_direction[1] * self.speed * dt / 1
            self.rect.topleft = (self.x, self.y)

        self.animator.update(dt)
