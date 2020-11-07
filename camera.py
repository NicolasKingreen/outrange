
class Camera():

    def __init__(self, game_instance):
        self.game_instance = game_instance
        self.x, self.y = self.game_instance.player.x, self.game_instance.player.y

    def update(self):
        self.x = self.game_instance.player.x
        self.y = self.game_instance.player.y
