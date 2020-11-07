import sys
from random import randint

import pygame as pg

from world import World
from tile_map import TileMap
from player import Player
from npc import RangerNPC
from settings import Settings
from game_info import GameInfo
from camera import Camera


class OutRange:
    """Game class"""

    def __init__(self):
        self._init_system()
        self._init_screen()

        self.world = World(self)
        self.tile_map = TileMap(self)

        self.player = Player(self)
        self.camera = Camera(self)
        self.npcs = [
            RangerNPC(self, (randint(0, self.settings.screen_width), randint(0, self.settings.screen_height))),
            RangerNPC(self, (randint(0, self.settings.screen_width), randint(0, self.settings.screen_height))),
            RangerNPC(self, (randint(0, self.settings.screen_width), randint(0, self.settings.screen_height)))
        ]

        self.game_objects = []
        self.game_objects.append(self.player)
        self.game_objects.extend(self.npcs)

    def _init_system(self):
        pg.init()
        self.settings = Settings()
        self.game_info = GameInfo()
        self.clock = pg.time.Clock()

    def _init_screen(self):
        self.screen = pg.display.set_mode(self.settings.screen_resolution)
        pg.display.set_icon(pg.image.load("data/images/icon.png"))
        pg.display.set_caption("Out Range")

    def run(self):
        """Starts the game."""
        while True:
            dt = self.clock.tick()
            self._handle_events()
            for game_object in self.game_objects:
                game_object.update(dt)
            self._process_fps()
            # print(f"{self.game_objects}\r", end="")
            self._update_screen()

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._handle_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._handle_keyup_events(event)

    def _handle_keydown_events(self, event):
        if event.key == pg.K_ESCAPE:
            sys.exit()
        elif event.key == pg.K_k:
            self.settings.draw_debug = not self.settings.draw_debug
        elif event.key == pg.K_j:
            self.settings.draw_fps = not self.settings.draw_fps
        elif event.key == pg.K_a:
            self.player.movement_direction[0] -= 1
        elif event.key == pg.K_d:
            self.player.movement_direction[0] += 1
        elif event.key == pg.K_w:
            self.player.movement_direction[1] -= 1
        elif event.key == pg.K_s:
            self.player.movement_direction[1] += 1

    def _handle_keyup_events(self, event):
        if event.key == pg.K_a:
            self.player.movement_direction[0] += 1
        elif event.key == pg.K_d:
            self.player.movement_direction[0] -= 1
        elif event.key == pg.K_w:
            self.player.movement_direction[1] += 1
        elif event.key == pg.K_s:
            self.player.movement_direction[1] -= 1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.tile_map.draw(self.screen)
        self.game_objects.sort(key=lambda x: x.rect.centery)
        # print(f"{self.game_objects}\r", end="")
        for game_object in self.game_objects:
            game_object.draw(self.screen)
        if self.settings.draw_fps:
            self._display_fps()
        pg.display.flip()

    def _process_fps(self):
        fps = int(self.clock.get_fps())
        self.game_info.add_record(fps)
        self.game_info.update()

    def _display_fps(self):

        fps_surface = self.settings.font.render(f"fps: {self.game_info.current_fps}", True, (255, 255, 255))
        fps_rect = fps_surface.get_rect()
        fps_rect.topleft = self.settings.fps_position

        avg_fps_surface = self.settings.font.render(f"avg_fps: {self.game_info.avg_fps}", True, (255, 255, 255))
        avg_fps_rect = avg_fps_surface.get_rect()
        avg_fps_rect.topleft = fps_rect.bottomleft

        self.screen.blit(fps_surface, fps_rect)
        self.screen.blit(avg_fps_surface, avg_fps_rect)


if __name__ == "__main__":
    out_range = OutRange()
    out_range.run()

# %%
