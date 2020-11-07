import pygame as pg
from random import randint

from game_object import GameObject

TILE_WIDTH = 48
TILE_HEIGHT = 20

class TileMap:

    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.tiles_in_a_screen_row = self.game_instance.screen.get_rect().width // TILE_WIDTH
        self.tiles_in_a_screen_column = self.game_instance.screen.get_rect().height // TILE_HEIGHT

        self._load_tiles_from_sprite_sheet("data/images/tiles.png")
        self.tiles = []
        for i in range(14):
            for count in range(14 - i):
                self.tiles.append(Tile(self.game_instance, self.tile_images[i]))
        for tile in self.tiles:
            tile.set_at(TILE_WIDTH * randint(0, self.tiles_in_a_screen_row), TILE_HEIGHT * randint(0, self.tiles_in_a_screen_column))

    def _load_tiles_from_sprite_sheet(self, sprite_sheet_path):
        sprite_sheet = pg.image.load(sprite_sheet_path)
        tiles_in_a_row = sprite_sheet.get_rect().width // TILE_WIDTH
        tiles_in_a_column = sprite_sheet.get_rect().height // TILE_HEIGHT
        self.tile_images = []
        for tile_x in range(tiles_in_a_row):
            for tile_y in range(tiles_in_a_column):
                self.tile_images.append(sprite_sheet.subsurface((tile_x * TILE_WIDTH, tile_y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)))

    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface)


class Tile(GameObject):

    def __init__(self, game_instance, image):
        super().__init__(game_instance, "tile")
        self.image = image
        self.rect = pg.Rect((-TILE_WIDTH, -TILE_HEIGHT), (TILE_WIDTH, TILE_HEIGHT))

    def set_at(self, x, y):
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # pg.draw.rect(surface, (255, 0, 0), self.rect, 1)

    def __repr__(self):
        return f"Tile at ({self.rect.x}, {self.rect.y})"
