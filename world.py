import pygame as pg

from tile_map import TileMap
from grid import Grid
from player import Player
from npc import RangerNPC
from camera import Camera
from vector import Vector


class World():

    def __init__(self, game_instance):
        self.game_instance = game_instance

        self.width = 1440
        self.height = 1000

        self.bg_x = 0
        self.bg_y = 0
        self.bg_surface = pg.Surface((self.width, self.height))
        self.bg_surface.fill(self.game_instance.settings.bg_color)
        self.bg_rect = self.bg_surface.get_rect()

        # self.tile_map = TileMap(game_instance)
        self.game_objects = []
    
        self.player = Player(self, Vector(200, 200))
        self.add_object(self.player)
        self.add_object(RangerNPC(self, (100, 100)))

        self.camera = Camera(self, Vector(-200, -200))
        # self.grid = Grid(self)

    def add_object(self, game_object):
        self.game_objects.append(game_object)

    def update(self, frame_time):
        # self.grid.update()
        self.camera.update(frame_time)
        for game_object in self.game_objects:
            game_object.update(frame_time)

        self.bg_rect.x = self.bg_x -  self.camera.position.x
        self.bg_rect.y = self.bg_y - self.camera.position.y

        # print(f"({self.game_objects[0].x}, {self.game_objects[0].y}) => ({self.player.x}, {self.player.y})\r", end="")

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.bg_surface, self.bg_rect)
        # self.grid.draw(surface)
        # self.tile_map.draw(surface)
        for game_object in self.game_objects:
            game_object.draw(surface)
        if self.game_instance.settings.draw_debug:
            rel_cam_pos = self.game_instance.settings.screen_center
            pg.draw.line(surface, (34, 231, 34), rel_cam_pos, self.player.rect.center)
            pg.draw.circle(surface, (34, 34, 231), rel_cam_pos, 3)
            pg.draw.circle(surface, (231, 34, 34), rel_cam_pos, self.camera.ease_distance, 1)
