import pygame as pg
from game_object import GameObject
from vector import Vector

class Entity(GameObject):
    """
    That class represents every entity in the game.
    Actually, those that move and have hitpoints.

    rect is where the sprite is drawn
    x is the position in the world
    """

    def __init__(self, world, name, position):
        super().__init__(world, name, position)
        self.rect = pg.Rect(self.position.as_tuple(), self.SIZE)
        self.hp = 5

        self.movement_direction = Vector(0, 0)
        self.speed = 0.

    def _prep_name_label(self):
        self.name_surface = self.world.game_instance.settings.font16.render(
            f"{self.name} ({self.hp})", True, (255, 255, 255))
        self.name_rect = self.name_surface.get_rect()
        self.name_rect.center = self.rect.centerx, self.rect.y - 32

    def update(self):

        # Updates drawn position
        self.rect.center = self.position.as_tuple()
        self.rect.x -= self.world.camera.position.x
        self.rect.y -= self.world.camera.position.y
        self.name_rect.center = self.rect.centerx, self.rect.y - 32

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.world.game_instance.settings.draw_debug:
            surface.blit(self.name_surface, self.name_rect)
            pg.draw.rect(surface, (255, 0, 0), self.rect, 1)

    # def __repr__(self):
    #     return f"{self.name} ({self.rect.x}, {self.rect.y})"
