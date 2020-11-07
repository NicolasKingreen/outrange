import pygame as pg
from game_object import GameObject

class Entity(GameObject):

    def __init__(self, game_instance, name):
        super().__init__(game_instance, name)
        self.image = None
        self.images = []
        self.rect = pg.Rect(self.game_instance.settings.screen_center, (1, 1))
        self.looking_left = False
        self.hp = 5
        self.speed = 0.
        self.id = 0

    def _load_images_from_sprite_sheet(self, sprite_sheet_path):
        sprite_sheet = pg.image.load(sprite_sheet_path)
        sprites_amount = sprite_sheet.get_rect().width // self.rect.width
        for i in range(sprites_amount):
            sprite = sprite_sheet.subsurface(pg.Rect(self.rect.width * i, 0, self.rect.width, self.rect.height))
            self.images.append(sprite)
        self.image = self.images[0]

    def _scale_images_2x(self):
        if self.images:
            scaled_images = []
            self.scale = (x * 2 for x in self.scale)
            for image in self.images:
                scaled_images.append(pg.transform.scale2x(image))
            self.images = scaled_images
            self.rect = self.images[0].get_rect()

    def _prep_name_label(self):
        self.name_surface = self.game_instance.settings.font.render(f"{self.name} ({self.hp})", True, (255, 255, 255))
        self.name_rect = self.name_surface.get_rect()
        self.name_rect.center = self.rect.centerx, self.rect.y - 32

    def update(self):
        self.name_rect.center = self.rect.centerx, self.rect.y - 32

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.game_instance.settings.draw_debug:
            surface.blit(self.name_surface, self.name_rect)
            pg.draw.rect(surface, (255, 0, 0), self.rect, 1)

    def __repr__(self):
        return f"{self.name} ({self.x}, {self.y})"
