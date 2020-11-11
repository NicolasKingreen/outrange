import pygame as pg


class Grid:

    CELL_SIZE = (48, 20)

    def __init__(self, world):
        self.camera = world.camera
        self.x = 0
        self.y = 0
        self.width = world.width
        self.height = world.height
        self.draw_x = 0
        self.draw_y = 0
        self.rows = world.height // 20
        self.columns = world.width // 48

    def update(self):
        self.draw_x = self.x - self.camera.x
        self.draw_y = self.y - self.camera.y

    def draw(self, surface):
        for column in range(self.columns):
            pg.draw.line(surface, (90, 90, 90), (self.draw_x + column * 48, self.draw_y), (self.draw_x + column * 48, self.draw_y + self.height), 2)
        for row in range(self.rows):
            pg.draw.line(surface, (90, 90, 90), (self.draw_x, self.draw_y + row * 20), (self.draw_x + self.width, self.draw_y + row * 20), 2)