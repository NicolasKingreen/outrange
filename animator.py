import pygame as pg

class Animator():

    def __init__(self, game_object, images, default_duration=300):
        self.game_object = game_object
        self.scene_time = 0
        self.scenes = []
        for i, image in enumerate(images):
            self.scenes.append(Scene(i, image, default_duration))
        self.max_index = len(self.scenes) - 1

        self.current_index = 0

    def update(self, dt):
        self.scene_time += dt

        if self.game_object.movement_direction[0] < 0 and not self.game_object.looking_left:
            self.game_object.image = pg.transform.flip(self.game_object.image, True, False)
            self.game_object.looking_left = True
        elif self.game_object.movement_direction[0] > 0 and self.game_object.looking_left:
            self.game_object.image = pg.transform.flip(self.game_object.image, True, False)
            self.game_object.looking_left = False
        if self.scene_time >= self.scenes[self.current_index].duration:
            self._change_to_next_scene()

    def _change_to_next_scene(self):
        if self.current_index < self.max_index:
            self.current_index += 1
        else:
            self.current_index = 0
        self.game_object.image = self.scenes[self.current_index].image
        if self.game_object.looking_left:
            self.game_object.image = pg.transform.flip(self.game_object.image, True, False)
        self.scene_time = 0

class Scene():

    def __init__(self, index, image, duration):
        self.index = index
        self.image = image
        self.duration = duration
