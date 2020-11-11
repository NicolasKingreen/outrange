"""
Version = 0.1.0dev5.11.2020
Out Range is a 2D PvP game where you can fight your friends using a bow.
"""

import sys

import pygame as pg

from world import World
from settings import Settings
from game_info import GameInfo


class OutRange:
    """
    Main game class.
    """

    def __init__(self):

        pg.init()
        self.settings = Settings()
        self.game_info = GameInfo()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode(self.settings.screen_resolution)
        pg.display.set_icon(pg.image.load("data/images/icon.png"))
        pg.display.set_caption("Out Range")

        self.world = World(self)

    def run(self):
        """Starts the game."""
        while True:
            frame_time = self.clock.tick()
            self._handle_events()
            self.world.update(frame_time)
            self._process_fps()
            self._update_screen()

    def close(self):
        """Closes the game."""
        sys.exit()

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close()
            elif event.type == pg.KEYDOWN:
                self._handle_keydown_event(event)
            elif event.type == pg.KEYUP:
                self._handle_keyup_event(event)
            # elif event.type == pg.MOUSEBUTTONDOWN:
            #     mouse_pos = pg.mouse.get_pos()
            #     mouse_x, mouse_y = mouse_pos
            #     self.world.game_objects[0].destination = (mouse_x - self.world.camera.x, mouse_y - self.world.camera.y)

    def _handle_keydown_event(self, event):
        if event.key == pg.K_ESCAPE:
            self.close()
        elif event.key == pg.K_k:
            self.settings.draw_debug = not self.settings.draw_debug
        elif event.key == pg.K_j:
            self.settings.draw_fps = not self.settings.draw_fps
        elif event.key == pg.K_a:
            self.world.player.movement_direction.x -= 1
        elif event.key == pg.K_d:
            self.world.player.movement_direction.x += 1
        elif event.key == pg.K_w:
            self.world.player.movement_direction.y -= 1
        elif event.key == pg.K_s:
            self.world.player.movement_direction.y += 1

    def _handle_keyup_event(self, event):
        if event.key == pg.K_a:
            self.world.player.movement_direction.x += 1
        elif event.key == pg.K_d:
            self.world.player.movement_direction.x -= 1
        elif event.key == pg.K_w:
            self.world.player.movement_direction.y += 1
        elif event.key == pg.K_s:
            self.world.player.movement_direction.y -= 1

    def _update_screen(self):
        self.world.draw(self.screen)
        if self.settings.draw_fps:
            self._draw_fps()
        pg.display.flip()

    def _process_fps(self):
        fps = int(self.clock.get_fps())
        self.game_info.add_record(fps)
        self.game_info.update()

    def _draw_fps(self):

        # Draw FPS
        fps_surface = self.settings.font16.render(f"fps: {self.game_info.current_fps}", True, (255, 255, 255))
        fps_rect = fps_surface.get_rect()
        fps_rect.topleft = self.settings.fps_position

        # Draw Anerage FPS
        avg_fps_surface = self.settings.font16.render(f"avg_fps: {self.game_info.avg_fps}", True, (255, 255, 255))
        avg_fps_rect = avg_fps_surface.get_rect()
        avg_fps_rect.topleft = fps_rect.bottomleft

        self.screen.blit(fps_surface, fps_rect)
        self.screen.blit(avg_fps_surface, avg_fps_rect)


if __name__ == "__main__":
    out_range = OutRange()
    out_range.run()
