from vector import Vector

class GameObject():

    def __init__(self, world, name, position=Vector(0, 0)):

        self.world = world
        self.name = name

        self.position = position
        self.rotation = (0, 0)
        self.scale = (1, 1)
