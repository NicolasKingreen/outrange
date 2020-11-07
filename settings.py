from pygame import font

class Settings:

    def __init__(self):
        self.screen_resolution = self.screen_width, self.screen_height = (960, 800)
        self.screen_center = (self.screen_width // 2, self.screen_height // 2)

        self.fps_position = (0, 0)

        self.bg_color = (63, 158, 61)

        self.font = font.SysFont(None, 16)
        self.font32 = font.SysFont(None, 32)

        self.draw_debug = True
        self.draw_fps = True
