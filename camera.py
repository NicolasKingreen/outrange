from game_object import GameObject
from vector import Vector


class Camera(GameObject):
    """Camera class that follows the player and make other entities draw relative to it."""

    def __init__(self, world, position):
        super().__init__(world, "camera", position)
        self.zoom = 1
        self.speed = self.world.player.speed
        self.ease_distance = 10
        self.destination = Vector(0, 0)
        self.movement_direction = Vector(0, 0)

    def update(self, frame_time):
        self.destination = self.world.player.position
        rel_pos = self.position + self.world.game_instance.settings.screen_center
        distance = rel_pos.get_distance_to(self.destination)
        if distance > self.ease_distance:
            self.movement_direction = (self.destination - rel_pos).get_normalised()
            self.position += self.movement_direction * self.speed * frame_time
        # print(f"{rel_pos} => {self.destination} = {round(distance, 1)} with {self.movement_direction}\r", end="")

