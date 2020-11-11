import math
import pygame as pg

from animator import Animator
from entity import Entity

class Player(Entity):
    """Player class."""

    SIZE = (64, 104)

    def __init__(self, world, position):

        super().__init__(world, "player", position)

        # self._load_images_from_sprite_sheet("data/images/ranger.png") 
        # self.animator = Animator(self, self.images)

        self.image = pg.image.load("data/images/ranger/idle.png")

        self.hp = 36

        self.speed = 0.3

        self._prep_name_label()

    def update(self, frame_time):


        # print(f"Direction: ({self.movement_direction[0]}, {self.movement_direction[1]}); Location: ({self.x}, {self.y})\r", end="")

        if self.movement_direction.x or self.movement_direction.y:
            self.position += self.movement_direction.get_normalised() * self.speed * frame_time

        super().update()
        self.name_rect.center = self.rect.centerx, self.rect.y - 16

        # self.animator.update(dt)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.world.game_instance.settings.draw_debug:
            surface.blit(self.name_surface, self.name_rect)
            pg.draw.rect(surface, (255, 0, 0), self.rect, 1)
