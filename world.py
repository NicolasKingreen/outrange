class World():

    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.game_objects = []
        self.width = 2000
        self.height = 2000

    def draw(self, surface):
        surface.fill(self.game_instance.settings.bg_color)
        for game_object in self.game_objects:
            game_object.draw(surface)
