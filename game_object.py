class GameObject():

    def __init__(self, game_instance, name):

        self.game_instance = game_instance
        self.name = name

        self.position = (self.x, self.y) = 0., 0.
        self.rotation = (0, 0)
        self.scale = (1, 1)
